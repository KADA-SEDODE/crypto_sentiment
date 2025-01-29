from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer
import pandas as pd
import os

# Charger le modèle CryptoBERT
model_name = "ElKulako/cryptobert"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=512, truncation=True)

# Fonction pour analyser les sentiments avec gestion des cas particuliers
def analyze_sentiment_with_threshold(text, threshold=0.55):
    if not isinstance(text, str) or not text.strip():
        return "Invalid", 0.0  # Texte vide ou non valide
    result = pipe([text[:512]])[0]  # Limiter à 512 tokens
    if result['score'] < threshold:
        return "Uncertain", result['score']  # Texte ambigu ou faible confiance
    return result['label'], result['score']

# Charger les données d'un fichier
def process_file(file_path, output_path, threshold=0.55):
    print(f"📂 Chargement du fichier : {file_path}")
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Fichier chargé avec {len(df)} lignes.")

        # Analyse des sentiments
        print("🔍 Analyse des sentiments en cours...")
        df[['sentiment_label', 'sentiment_score']] = df['description'].apply(
            lambda x: pd.Series(analyze_sentiment_with_threshold(x, threshold))
        )

        # Sauvegarder les résultats enrichis
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"✅ Sentiments analysés et sauvegardés dans {output_path}.")

    except Exception as e:
        print(f"❌ Erreur lors du traitement du fichier : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Dossier des fichiers d'entrée et de sortie
    input_files = {
        "Bitcoin": "data/raw/articles_bitcoin.csv",
        "Ethereum": "data/raw/articles_ethereum.csv",
        "Binance": "data/raw/articles_bnb.csv",
        "Solana": "data/raw/articles_solana.csv",
        "XRP": "data/raw/articles_xrp.csv",
    }

    output_folder = "data/processed/"
    threshold = 0.55  # Seuil de confiance pour les sentiments

    # Traiter chaque fichier
    for crypto, file_path in input_files.items():
        output_path = os.path.join(output_folder, f"articles_{crypto.lower()}_with_sentiments.csv")
        process_file(file_path, output_path, threshold)

    print("🎉 Analyse des sentiments terminée pour toutes les cryptos !")
