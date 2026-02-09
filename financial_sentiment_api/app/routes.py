from fastapi import APIRouter
from datetime import datetime
from app.schemas import TextInput, SentimentResponse
from app.services.sentiment import analyze_financial_sentiment




router = APIRouter()



@router.get("/health")
def health():
    return {"status": "ok"}



@router.post("/analyze",response_model=SentimentResponse)
def analyze_text(payload: TextInput):
    result = analyze_financial_sentiment(payload.text)
    result['timestamp'] = datetime.utcnow()
    return result

