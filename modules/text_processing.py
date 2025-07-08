import re
import pandas as pd

def clean_text(text):
    """Basic text cleaning"""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'\@\w+|\#', '', text)  # Remove mentions and hashtags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

def preprocess_data(df):
    """Process the entire dataframe"""
    df['clean_text'] = df['text'].apply(clean_text)
    return df