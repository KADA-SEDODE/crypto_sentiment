import praw
import pandas as pd
import time
import os

# 🔹 Connexion à Reddit
reddit = praw.Reddit(
    client_id="E7oYGUF7r2R4fYVMI-FTZw",
    client_secret="ZBXN8T8IFXAEJFnE65KXCpF-_-2yxQ",
    user_agent="crypto_scraper",
    username="Aromatic_Departure38",  # Ton nom d'utilisateur Reddit
    password="Sabinekodjori1963marv"  # Ton mot de passe Reddit
)

# 🔹 Associer chaque crypto à ses subreddits spécifiques
crypto_subreddits = {
    "Bitcoin": ["CryptoCurrency", "CryptoMarkets"],
    "Ethereum": ["CryptoCurrency", "CryptoMarkets"],
    "Binance Coin": ["CryptoCurrency", "CryptoMarkets"],
    "Solana": ["CryptoCurrency", "CryptoMarkets"],
    "XRP": ["ripple", "CryptoCurrency"],
    "Cardano": ["cardano", "CryptoCurrency"],
    "Dogecoin": ["dogecoin", "CryptoCurrency"],
    "Tether": ["CryptoCurrency", "CryptoMarkets"],
    "Litecoin": ["litecoin", "CryptoCurrency"],
    "Shiba Inu": ["SHIBArmy", "CryptoCurrency"],
    "TRON": ["Tronix", "CryptoCurrency"],
}

# 🔹 Dossier de sauvegarde
output_dir = "data/reddit_data"
os.makedirs(output_dir, exist_ok=True)

# 🔹 Scraper chaque crypto et sauvegarder un fichier par crypto
for crypto, subreddits in crypto_subreddits.items():
    print(f"🔍 Scraping Reddit pour {crypto}...")

    all_posts = []  # Stocker les posts de cette crypto

    for subreddit_name in subreddits:
        print(f"🔹 Scraping dans {subreddit_name}...")

        try:
            subreddit = reddit.subreddit(subreddit_name)

            for post in subreddit.search(crypto, sort="hot", time_filter="year", limit=1000):
                all_posts.append({
                    "crypto": crypto,
                    "subreddit": subreddit_name,
                    "title": post.title,
                    "score": post.score,
                    "comments": post.num_comments,
                    "created": pd.to_datetime(post.created_utc, unit="s"),
                    "url": post.url
                })
            
            time.sleep(2)  # Pause pour éviter un blocage API Reddit

        except Exception as e:
            print(f"⚠️ Erreur avec {subreddit_name} pour {crypto}: {e}")

    # 🔹 Convertir en DataFrame
    df_reddit = pd.DataFrame(all_posts)

    # 🔹 Sauvegarde dans un fichier spécifique
    output_file = os.path.join(output_dir, f"{crypto.lower().replace(' ', '_')}_posts.csv")
    df_reddit.to_csv(output_file, index=False, encoding="utf-8")

    print(f"✅ Scraping terminé pour {crypto} ! {df_reddit.shape[0]} posts sauvegardés dans {output_file}\n")

print("🚀 Scraping Reddit COMPLET pour toutes les cryptos !")
