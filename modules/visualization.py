import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sentiment_trend(df):
    """Plot sentiment over time"""
    plt.figure(figsize=(10, 6))
    df['date'] = df['created_at'].dt.date
    daily_sentiment = df.groupby('date')['sentiment'].mean().reset_index()
    
    sns.lineplot(data=daily_sentiment, x='date', y='sentiment')
    plt.title('Sentiment Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

def plot_sentiment_distribution(df):
    """Plot sentiment distribution"""
    plt.figure(figsize=(8, 6))
    df['sentiment_category'] = df['sentiment'].apply(
        lambda x: 'Positive' if x > 0.1 else 'Negative' if x < -0.1 else 'Neutral'
    )
    sns.countplot(data=df, x='sentiment_category', order=['Negative', 'Neutral', 'Positive'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Category')
    plt.ylabel('Count')
    return plt