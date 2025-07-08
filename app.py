import streamlit as st
from modules.data_collection import get_twitter_data
from modules.text_processing import preprocess_data
from modules.sentiment_analysis import add_sentiment_scores
from modules.visualization import plot_sentiment_trend, plot_sentiment_distribution
import pandas as pd


from dotenv import load_dotenv  # 1. Import first
load_dotenv()                  # 2. Load .env BEFORE API calls
from modules.data_collection import get_twitter_data
# Streamlit UI
st.set_page_config(page_title="Healthcare Sentiment Dashboard", layout="wide")
st.title("🏥 Healthcare Social Media Sentiment Dashboard")

# Sidebar inputs
with st.sidebar:
    st.header("Parameters")
    query = st.text_input("Search for healthcare topics/hashtags", "#mentalhealth")
    tweet_count = st.slider("Number of tweets to analyze", 50, 500, 100)
    st.markdown("""
    **Note:**  
    - Free tier allows ~100 tweets every 15 minutes.  
    - Avoid frequent reloads to prevent rate limits.
    """)

# Main analysis pipeline
if st.sidebar.button("Analyze Sentiment"):
    with st.spinner("Fetching and analyzing tweets..."):
        # Step 1: Fetch data
        raw_data = get_twitter_data(query, tweet_count)
        
        if not raw_data.empty:
            # Step 2: Clean and analyze
            processed_data = preprocess_data(raw_data)
            analyzed_data = add_sentiment_scores(processed_data)
            
            # Display results
            st.success("Analysis complete!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Sentiment Trend Over Time")
                st.pyplot(plot_sentiment_trend(analyzed_data))
            
            with col2:
                st.subheader("Sentiment Distribution")
                st.pyplot(plot_sentiment_distribution(analyzed_data))
            
            st.subheader("Sample Tweets")
            st.dataframe(
                analyzed_data[['text', 'sentiment']].head(10),
                height=300,
                use_container_width=True
            )
        else:
            st.error("Failed to fetch tweets. Possible reasons:")
            st.markdown("""
            - API rate limit exceeded (wait 15 minutes)  
            - Invalid Twitter API credentials  
            - No tweets found for the query
            """)