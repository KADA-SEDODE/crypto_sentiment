from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np  # Ajoute cette ligne en haut de ton fichier
import re
import spacy
import torch
import matplotlib.pyplot as plt   
import seaborn as sns 
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
from src.scraping.crypto_prices import get_historical_prices
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
import io
import json

from pathlib import Path

# le dossier racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Remonte 3 niveaux vers la racine

# les répertoires des données
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

#  les fichiers spécifiques
CRYPTO_NEWS_CLEANED = RAW_DATA_DIR / "crypto_news_cleaned.csv"
CRYPTO_PRICES_HISTORICAL = RAW_DATA_DIR / "crypto_prices_historical_11.csv"
CRYPTO_NEWS_SENTIMENTS = RAW_DATA_DIR / "crypto_news_sentiments.csv"
PORTFOLIO_STATISTICS = RAW_DATA_DIR / "portfolio_statistics.json"
GRAPH_CUMULATIVE_RETURNS = RAW_DATA_DIR / "cumulative_returns.png"


router = APIRouter()

# Charger le modèle NLP (CryptoBERT)
model_name = "ElKulako/cryptobert"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=128, truncation=True, padding='max_length')

# Charger le modèle SpaCy
spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

# Fonction de nettoyage du texte
def preprocess_text(text):
    text = re.sub(r'http\S+|www.\S+', '', text)  # Supprimer les URLs
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)  # Supprimer caractères spéciaux
    text = text.lower()
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(tokens)

# Endpoint : Fusionner & Nettoyer les articles
@router.get("/get_crypto_data")
def get_crypto_data():
    try:
        # Charger les fichiers de news
        
        cryptos = ["Binance_Coin","Bitcoin","Cardano","Dogecoin","Ethereum","Litecoin","shiba_inu","Solana","Tether","TRON","XRP"]
        dfs = [pd.read_csv(RAW_DATA_DIR / f"articles_{crypto}.csv") for crypto in cryptos]
        df_crypto = pd.concat(dfs, ignore_index=True)
        
        # Nettoyer les données
        df_crypto = df_crypto.dropna(subset=["description"])
        df_crypto["cleaned_description"] = df_crypto["description"].apply(preprocess_text)
        return df_crypto.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")

# Endpoint : Analyser les sentiments avec CryptoBERT
@router.post("/analyze_sentiment")
def analyze_sentiment():
    try:
        df_crypto = pd.read_csv(CRYPTO_NEWS_CLEANED)
        #  Limiter aux 500 derniers articles pour éviter un traitement trop long
        df_crypto = df_crypto.tail(500)

        # Traiter les textes en batchs de 16 pour accélérer le pipeline
        texts = df_crypto["cleaned_description"].tolist()
        sentiments = pipe(texts, batch_size=16, truncation=True)  # Batching
        
        #  Ajouter les résultats au DataFrame
        df_crypto["sentiment"] = sentiments

        return df_crypto.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


# Endpoint : Calcul des rendements des portefeuilles
@router.get("/compute_portfolio_returns")
def compute_portfolio_returns():
    try:
        # Charger les prix et sentiments
        crypto_prices = pd.read_csv(CRYPTO_PRICES_HISTORICAL)
        df_sentiments = pd.read_csv(CRYPTO_NEWS_SENTIMENTS)
        # Initialisation des rendements des stratégies
        portfolio_returns = {"HML 1/3": [], "HML 5%": [], "Proportional": []}

        # Boucle sur chaque jour de données
        for date in df_sentiments["date_only"].unique():
            daily_data = df_sentiments[df_sentiments["date_only"] == date]
            sorted_data = daily_data.sort_values(by="sentiment_daily", ascending=False)

            # Stratégie HML 1/3
            top_1_3 = sorted_data.iloc[:len(sorted_data) // 3]
            bottom_1_3 = sorted_data.iloc[-len(sorted_data) // 3:]

            top_1_3 = top_1_3[top_1_3["Open"] > 0]
            bottom_1_3 = bottom_1_3[bottom_1_3["Open"] > 0]

            if not top_1_3.empty and not bottom_1_3.empty:
                long_return_1_3 = (top_1_3["Close"] / top_1_3["Open"] - 1).mean()
                short_return_1_3 = (bottom_1_3["Close"] / bottom_1_3["Open"] - 1).mean()
                portfolio_returns["HML 1/3"].append(long_return_1_3 - short_return_1_3)
            else:
                portfolio_returns["HML 1/3"].append(0)

            # Stratégie HML 5%
            top_5 = sorted_data.iloc[:max(1, int(len(sorted_data) * 0.05))]
            bottom_5 = sorted_data.iloc[-max(1, int(len(sorted_data) * 0.05)):]

            top_5 = top_5[top_5["Open"] > 0]
            bottom_5 = bottom_5[bottom_5["Open"] > 0]

            if not top_5.empty and not bottom_5.empty:
                long_return_5 = (top_5["Close"] / top_5["Open"] - 1).mean()
                short_return_5 = (bottom_5["Close"] / bottom_5["Open"] - 1).mean()
                portfolio_returns["HML 5%"].append(long_return_5 - short_return_5)
            else:
                portfolio_returns["HML 5%"].append(0)

            # Stratégie Proportional
            if not daily_data.empty and "sentiment_daily" in daily_data.columns:
                proportional_return = (daily_data["sentiment_daily"] * (daily_data["Close"] / daily_data["Open"] - 1)).sum()
                portfolio_returns["Proportional"].append(proportional_return)
            else:
                portfolio_returns["Proportional"].append(0)

        #  Vérification des valeurs extrêmes (inf ou NaN)
        for key in portfolio_returns:
            print(f"{key} - Max:", max(portfolio_returns[key], default="Aucune valeur"))
            print(f"{key} - Min:", min(portfolio_returns[key], default="Aucune valeur"))

        #  Correction des valeurs inf et NaN
        for key in portfolio_returns:
            portfolio_returns[key] = [0 if (np.isnan(x) or np.isinf(x)) else x for x in portfolio_returns[key]]

        return portfolio_returns

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")

#  Endpoint pour récupérer les statistiques de performance du portefeuille
@router.get("/data/portfolio_statistics")
def get_portfolio_statistics():
    try:
        with open(PORTFOLIO_STATISTICS, "r") as f:
            stats_data = json.load(f)
        return stats_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")

#  Endpoint pour afficher le graphique des rendements cumulés

@router.get("/plot_cumulative_returns")
def get_cumulative_returns_plot():
    """
    Renvoie l'image du graphique de rendements cumulés stockée.
    """
    if GRAPH_CUMULATIVE_RETURNS.exists():
        return FileResponse(GRAPH_CUMULATIVE_RETURNS, media_type="image/png")
