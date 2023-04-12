from transformers import pipeline

sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", revision="af0f99b")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
tagger = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


@app.get("/ai/summarize")
def get_summary(text: str):
    """Summarize text using BART model."""
    return summarizer(text)


@app.get("/ai/sentiment")
def get_sentiment(text: str):
    """Get sentiment of text using DistilBERT model."""
    return sentiment(text)


@app.get("/ai/tags")
def get_tags(text: str, labels: str):
    """Get tags of text using BART model."""
    return tagger(
        text,
        candidate_labels=labels.split(",")
    )
