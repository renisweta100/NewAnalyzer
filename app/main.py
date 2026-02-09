from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Financial Sentiment Analyzer API",
    description="Analyzes sentiment of financial text",
    version="1.0.0"
)

app.include_router(router)
