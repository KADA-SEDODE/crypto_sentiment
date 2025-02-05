from fastapi import APIRouter, HTTPException
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
from .models import TextRequest, SentimentResponse

# Charger le modèle CryptoBERT une seule fois
model_name = "ElKulako/cryptobert"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=128, truncation=True, padding='max_length')

router = APIRouter()

@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: TextRequest):
    """
    Endpoint pour analyser le sentiment d'un texte donné.
    """
    if not request.description.strip():
        raise HTTPException(status_code=400, detail="Le texte d'entrée ne peut pas être vide.")
    
    try:
        # Prédiction du sentiment
        prediction = pipe(request.description)[0]
        return SentimentResponse(
            label=prediction["label"],
            score=prediction["score"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'analyse du sentiment : {str(e)}")
