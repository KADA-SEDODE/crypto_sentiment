import praw
import pandas as pd
import os
from datetime import datetime

# 📌 Configuration de l'API Reddit (remplace par tes propres credentials)
reddit = praw.Reddit(
    client_id="E7oYGUF7r2R4fYVMI-FTZw",  # Ton Client ID 
    client_secret="ZBXN8T8IFXAEJFnE65KXCpF-_-2yxQ",  # Ton Client Secret 
    user_agent="crypto_scraper",
)

# 📌 Liste des cryptos et des subreddits pertinents
cryptos = [
    "Bitcoin", "Ethereum", "Binance Coin", "Solana", "XRP", "Cardano", "Dogecoin",
    "Polygon", "Polkadot", "Tether", "Litecoin", "Chainlink", "Uniswap", "Avalanche",
    "Cosmos", "Shiba Inu", "Stellar", "TRON", "Near Protocol", "Algorand", "Toncoin",
    "Arbitrum", "Aptos", "Optimism", "VeChain"
]

subreddits = ["cryptocurrency", "bitcoin", "ethereum", "altcoin", "cryptomarkets"]

# 📌 Fonction pour scraper les posts Reddit
def scrape_reddit(crypto, subreddits, limit=100):
    """Scrape les meilleurs posts Reddit pour une crypto donnée"""
    articles = []
    
    for subreddit_name in subreddits:
        print(f"🔍 Scraping r/{subreddit_name} pour {crypto}...")

        subreddit = reddit.subreddit(subreddit_name)

        # 🔹 Chercher les posts les plus pertinents du dernier mois
        for post in subreddit.search(crypto, sort="top", time_filter="month", limit=limit):
            if not post.stickied and not post.over_18:  # 🔹 Exclure les posts épinglés et NSFW
                articles.append({
                    "title": post.title,
                    "date": datetime.utcfromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
                    "description": post.selftext if post.selftext else "No Description",
                    "subreddit": subreddit_name,
                    "upvotes": post.score,
                    "comments": post.num_comments,
                    "crypto": crypto,
                    "url": post.url
                })
    
    return articles

# 📌 Scraper Reddit pour toutes les cryptos
all_articles = []

for crypto in cryptos:
    articles = scrape_reddit(crypto, subreddits, limit=50)
    all_articles.extend(articles)

# 📌 Enregistrer les résultats en CSV
df_reddit = pd.DataFrame(all_articles)
os.makedirs("data/raw", exist_ok=True)
df_reddit.to_csv("data/raw/reddit_articles.csv", index=False, encoding="utf-8")

print("✅ Scraping Reddit terminé. Données enregistrées dans data/raw/reddit_articles.csv")
