from pydantic import BaseModel
from typing import List, Optional

# Modèle pour la requête de scraping
class ScrapeRequest(BaseModel):
    crypto: str  # Nom de la crypto à scraper
    source: str  # Source du scraping ('reddit' ou 'crypto.news')
    limit: Optional[int] = 10  # Nombre d'articles à récupérer (par défaut 10)

# Modèle pour la réponse de scraping
class ScrapeResponse(BaseModel):
    crypto: str
    source: str
    articles: List[dict]  # Liste des articles scrappés

# Modèle pour la requête d'analyse de sentiment
class TextRequest(BaseModel):
    description: str  # Texte à analyser

# Modèle pour la réponse de l'analyse de sentiment
class SentimentResponse(BaseModel):
    label: str  # Bullish, Neutral ou Bearish
    score: float  # Score de confiance
