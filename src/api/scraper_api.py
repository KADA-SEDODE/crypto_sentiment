from fastapi import APIRouter, HTTPException
from .models import ScrapeRequest, ScrapeResponse
from src.scraping.scraping_5cryptos import scrape_articles  # Import du scraping existant

router = APIRouter()

@router.post("/scrape", response_model=ScrapeResponse)
def scrape_data(request: ScrapeRequest):
    """
    Endpoint pour déclencher le scraping sur demande.
    """
    if request.source not in ["reddit", "crypto.news"]:
        raise HTTPException(status_code=400, detail="Source invalide. Choisissez 'reddit' ou 'crypto.news'.")
    
    try:
        # Exécuter le scraping avec les paramètres fournis
        articles = scrape_articles(base_url="https://crypto.news", query=request.crypto, max_pages=request.limit)
        
        return ScrapeResponse(
            crypto=request.crypto,
            source=request.source,
            articles=articles[:request.limit]  # Limite appliquée
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du scraping : {str(e)}")
