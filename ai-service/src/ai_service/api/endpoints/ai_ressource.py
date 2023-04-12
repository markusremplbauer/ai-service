from fastapi import APIRouter
from transformers import pipeline

router = APIRouter()

sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
tagger = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


@router.get("/sentiment")
def get_sentiment(text: str):
    """Get sentiment of text using DistilBERT model."""
    return sentiment(text)


@router.get("/summarize")
def get_summary(text: str):
    """Summarize text using BART model."""
    return summarizer(text)


@router.get("/tags")
def get_tags(text: str, labels: str):
    """Get tags of text using BART model."""
    return tagger(
        text,
        candidate_labels=labels.split(",")
    )
