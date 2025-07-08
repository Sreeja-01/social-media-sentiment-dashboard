import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load .env file to get Twitter API bearer token
load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")

import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load .env file to get Twitter API bearer token
load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")

def get_twitter_data(query, max_tweets):
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    url = (
        f"https://api.twitter.com/2/tweets/search/recent?"
        f"query={query}&max_results={min(max_tweets, 100)}&tweet.fields=created_at,text"
    )

    # 🔍 DEBUG PRINTS
    print(f"🔍 Querying: {query}")
    print(f"🔐 Token starts with: {bearer_token[:10]}")
    print("📡 Sending request...")

    response = requests.get(url, headers=headers)

    # 🔍 API response info
    print("🔁 Status Code:", response.status_code)
    print("🧾 Response:", response.text)

    # If error
    if response.status_code != 200:
        print("❌ Failed to fetch tweets.")
        return pd.DataFrame()

    # Parse and return tweets
    data = response.json().get("data", [])
    if not data:
        print("⚠️ No tweets found for this query.")
        return pd.DataFrame()

    return pd.DataFrame(data)
