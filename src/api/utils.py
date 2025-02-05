from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

# Charger CryptoBERT une seule fois pour éviter le rechargement à chaque requête
def load_cryptobert():
    model_name = "ElKulako/cryptobert"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
    return TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=128, truncation=True, padding='max_length')

# Fonction pour normaliser les noms de cryptos
def normalize_crypto_name(crypto: str) -> str:
    crypto_mapping = {
        "Ethereum": "ETH", "Bitcoin": "BTC", "Solana": "SOL",
        "Cardano": "ADA", "XRP": "XRP", "Dogecoin": "DOGE",
        "BNB": "BNB", "Polkadot": "DOT", "Polygon": "MATIC",
        "Tether": "USDT"
    }
    return crypto_mapping.get(crypto, crypto.upper())  # Retourne le mapping ou le nom en majuscules

# Fonction pour gérer les erreurs API (ex: crypto inconnue, texte vide)
def handle_api_error(detail: str, status_code: int = 400):
    from fastapi import HTTPException
    raise HTTPException(status_code=status_code, detail=detail)
