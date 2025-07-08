from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    """Basic sentiment analysis using TextBlob"""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def add_sentiment_scores(df):
    """Add sentiment scores to dataframe"""
    df['sentiment'] = df['clean_text'].apply(analyze_sentiment)
    return df

def categorize_sentiment(score):
    """Categorize sentiment into positive, neutral, negative"""
    if score > 0.1:
        return 'Positive'
    elif score < -0.1:
        return 'Negative'
    else:
        return 'Neutral'