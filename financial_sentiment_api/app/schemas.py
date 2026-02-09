from pydantic import BaseModel
from datetime import datetime

class TextInput(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float
    score : float
    model: str
    timestamp: datetime
