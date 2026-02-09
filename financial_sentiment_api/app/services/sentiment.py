from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

MODEL_NAME = "yiyanghkust/finbert-tone"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def analyze_financial_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)

    probs = F.softmax(outputs.logits, dim=-1)
    sentiment_idx = torch.argmax(probs, dim=1).item()

    labels = ["neutral", "positive", "negative"]

    return {
        "sentiment": labels[sentiment_idx],
        "confidence": float(probs[0][sentiment_idx]),
        "model": "FinBERT"
    }
