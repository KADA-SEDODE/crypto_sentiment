from fastapi import FastAPI
from src.api.scraper_api import router as scraper_router
from src.api.predict_api import router as predict_router

# Création de l'instance FastAPI
app = FastAPI(
    title="Crypto Sentiment API",
    description="Une API permettant d'interagir avec le scraping et l'analyse de sentiment sur les cryptomonnaies.",
    version="1.0"
)

# Index Endpoint
@app.get("/")
def index():
    return {
        "message": "Bienvenue sur l'API Crypto Sentiment!",
        "documentation": "/docs",
        "endpoints": ["/health", "/scrape", "/predict"]
    }

# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "OK"}

# Inclusion des routes des autres fichiers
app.include_router(scraper_router, prefix="/scrape")
app.include_router(predict_router, prefix="/predict")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
