import praw
import pandas as pd
import time

# # 🔹 Renseigne tes informations Reddit
# reddit = praw.Reddit(
#     client_id="E7oYGUF7r2R4fYVMI-FTZw",  # Ton Client ID 
#     client_secret="ZBXN8T8IFXAEJFnE65KXCpF-_-2yxQ",  # Ton Client Secret 
#     user_agent="crypto_scraper",
# )

# # 🔹 Liste des cryptos à surveiller
# cryptos = [
#     "Bitcoin", "Ethereum", "Binance Coin", "Solana", "XRP", "Cardano", "Dogecoin",
#     "Polygon", "Polkadot", "Tether", "Litecoin", "Chainlink", "Uniswap", "Avalanche",
#     "Cosmos", "Shiba Inu", "Stellar", "TRON", "Near Protocol", "Algorand", "Toncoin",
#     "Arbitrum", "Aptos", "Optimism", "VeChain"
# ]

# # 🔹 Stocker les résultats
# all_posts = []

# # 🔹 Parcourir chaque crypto et scraper Reddit
# for crypto in cryptos:
#     print(f"🔍 Scraping Reddit pour {crypto}...")

#     subreddit = reddit.subreddit("CryptoCurrency")  # Scraper le subreddit r/CryptoCurrency
    
#     for post in subreddit.search(crypto, sort="hot", time_filter="month", limit=50):
#         all_posts.append({
#             "crypto": crypto,
#             "title": post.title,
#             "score": post.score,
#             "comments": post.num_comments,
#             "created": pd.to_datetime(post.created_utc, unit="s"),
#             "url": post.url
#         })
    
#     time.sleep(2)  # Pause pour éviter d'être bloqué par Reddit

# # 🔹 Convertir en DataFrame et sauvegarder
# df_reddit = pd.DataFrame(all_posts)
# df_reddit.to_csv("data/raw/reddit_crypto_posts.csv", index=False, encoding="utf-8")

# print("✅ Scraping terminé ! Données sauvegardées dans data/raw/reddit_crypto_posts.csv")

#################################################################################################################"
# 
# "
# # 🔹 Configuration de l'API Reddit
# reddit = praw.Reddit(
#     client_id="E7oYGUF7r2R4fYVMI-FTZw",  # Ton Client ID
#     client_secret="ZBXN8T8IFXAEJFnE65KXCpF-_-2yxQ",  # Ton Client Secret
#     user_agent="crypto_scraper",
# )

# # 🔹 Liste des cryptos à surveiller
# cryptos = [
#     "Bitcoin", "Ethereum", "Binance Coin", "Solana", "XRP", "Cardano", "Dogecoin",
#     "Polygon", "Polkadot", "Tether", "Litecoin", "Chainlink", "Uniswap", "Avalanche",
#     "Cosmos", "Shiba Inu", "Stellar", "TRON", "Near Protocol", "Algorand", "Toncoin",
#     "Arbitrum", "Aptos", "Optimism", "VeChain"
# ]

# # 🔹 Date limite pour filtrer les résultats (Juillet 2024)
# date_limite = pd.to_datetime("2024-07-01")

# # 🔹 Stocker les résultats
# all_posts = []

# # 🔹 Parcourir chaque crypto et scraper Reddit
# for crypto in cryptos:
#     print(f"🔍 Scraping Reddit pour {crypto}...")

#     subreddit = reddit.subreddit("CryptoCurrency")  # Scraper le subreddit r/CryptoCurrency
    
#     # Récupérer tous les posts de l'année écoulée
#     for post in subreddit.search(crypto, sort="hot", time_filter="year", limit=500):  # 🔥 Augmentation de la limite
#         post_date = pd.to_datetime(post.created_utc, unit="s")  # Convertir en date
        
#         # ✅ Filtrer uniquement les posts après Juillet 2024
#         if post_date >= date_limite:
#             all_posts.append({
#                 "crypto": crypto,
#                 "title": post.title,
#                 "score": post.score,
#                 "comments": post.num_comments,
#                 "created": post_date,
#                 "url": post.url
#             })
    
#     time.sleep(2)  # Pause pour éviter d'être bloqué par Reddit

# # 🔹 Convertir en DataFrame et sauvegarder
# df_reddit = pd.DataFrame(all_posts)
# df_reddit.to_csv("data/raw/reddit_crypto_posts.csv", index=False, encoding="utf-8")

# print("✅ Scraping terminé ! Données sauvegardées dans data/raw/reddit_crypto_posts.csv")


###################################################################################################################

# import praw
# import pandas as pd
# import time

# # # 🔹 Renseigne tes informations Reddit
# # reddit = praw.Reddit(
# #     client_id="E7oYGUF7r2R4fYVMI-FTZw",
# #     client_secret="ZBXN8T8IFXAEJFnE65KXCpF-_-2yxQ",
# #     user_agent="crypto_scraper",
# # )

# reddit = praw.Reddit(
#     client_id="E7oYGUF7r2R4fYVMI-FTZw",
#     client_secret="ZBXN8T8IFXAEJFnE65KXCpF-_-2yxQ",
#     user_agent="crypto_scraper",
#     username="Aromatic_Departure38",  # Ajoute ton nom d'utilisateur Reddit
#     password="Sabinekodjori1963marv"  # Ajoute ton mot de passe Reddit
# )

# # 🔹 Liste des cryptos à surveiller
# cryptos = [
#     "Bitcoin", "Ethereum", "Binance Coin", "Solana", "XRP", "Cardano", "Dogecoin",
#     "Polygon", "Polkadot", "Tether", "Litecoin", "Chainlink", "Uniswap", "Avalanche",
#     "Cosmos", "Shiba Inu", "Stellar", "TRON", "Near Protocol", "Algorand", "Toncoin",
#     "Arbitrum", "Aptos", "Optimism", "VeChain"
# ]

# # 🔹 Liste des subreddits à scraper
# subreddits = ["CryptoCurrency", "CryptoMarkets", "CryptoMoonShots", "cryptotech", "cryptocurrencytrading"]

# # 🔹 Stocker les résultats
# all_posts = []

# # 🔹 Parcourir chaque crypto et scraper Reddit
# for crypto in cryptos:
#     print(f"🔍 Scraping Reddit pour {crypto}...")
    
#     for subreddit_name in subreddits:
#         print(f"🔹 Scraping dans {subreddit_name}...")
#         subreddit = reddit.subreddit(subreddit_name)
        
#         for post in subreddit.search(crypto, sort="hot", time_filter="year", limit=500):
#             all_posts.append({
#                 "crypto": crypto,
#                 "subreddit": subreddit_name,
#                 "title": post.title,
#                 "score": post.score,
#                 "comments": post.num_comments,
#                 "created": pd.to_datetime(post.created_utc, unit="s"),
#                 "url": post.url
#             })
        
#         time.sleep(5)  # Pause pour éviter d'être bloqué par Reddit

# # 🔹 Convertir en DataFrame et sauvegarder
# df_reddit = pd.DataFrame(all_posts)
# df_reddit.to_csv("data/raw/reddit_crypto_posts2.csv", index=False, encoding="utf-8")

# print(f"✅ Scraping terminé ! {df_reddit.shape[0]} posts sauvegardés.")

################################################################################

# import praw
# import pandas as pd
# import time

# reddit = praw.Reddit(
#     client_id="E7oYGUF7r2R4fYVMI-FTZw",
#     client_secret="ZBXN8T8IFXAEJFnE65KXCpF-_-2yxQ",
#     user_agent="crypto_scraper",
#     username="Aromatic_Departure38",  # Ajoute ton nom d'utilisateur Reddit
#     password="Sabinekodjori1963marv"  # Ajoute ton mot de passe Reddit
# )


# # 🔹 Liste des cryptos à surveiller
# cryptos = ["Ethereum"] # "Bitcoin", "Ethereum", "Binance Coin", "Solana", 

# # 🔹 Liste des subreddits accessibles
# subreddits = ["CryptoCurrency", "CryptoMarkets"]

# # 🔹 Stocker les résultats
# all_posts = []

# # 🔹 Scraper chaque crypto
# for crypto in cryptos:
#     print(f"🔍 Scraping Reddit pour {crypto}...")

#     for subreddit_name in subreddits:
#         print(f"🔹 Scraping dans {subreddit_name}...")
        
#         try:
#             subreddit = reddit.subreddit(subreddit_name)
#             for post in subreddit.search(crypto, sort="hot", time_filter="year", limit=500):
#                 all_posts.append({
#                     "crypto": crypto,
#                     "subreddit": subreddit_name,
#                     "title": post.title,
#                     "score": post.score,
#                     "comments": post.num_comments,
#                     "created": pd.to_datetime(post.created_utc, unit="s"),
#                     "url": post.url
#                 })
            
#             time.sleep(3)  # Pause pour éviter d'être bloqué

#         except Exception as e:
#             print(f"⚠️ Erreur avec {subreddit_name}: {e}")

# # 🔹 Convertir en DataFrame et sauvegarder
# df_reddit = pd.DataFrame(all_posts)
# df_reddit.to_csv("data/redit_data/Ethereum_posts.csv", index=False, encoding="utf-8")

# print(f"✅ Scraping terminé ! {df_reddit.shape[0]} posts sauvegardés.")


# import praw
# import pandas as pd
# import time
# import os

# # 🔹 Connexion à Reddit
# reddit = praw.Reddit(
#     client_id="E7oYGUF7r2R4fYVMI-FTZw",
#     client_secret="ZBXN8T8IFXAEJFnE65KXCpF-_-2yxQ",
#     user_agent="crypto_scraper",
#     username="Aromatic_Departure38",  # Ton nom d'utilisateur Reddit
#     password="Sabinekodjori1963marv"  # Ton mot de passe Reddit
# )

# # 🔹 Liste des cryptos à surveiller
# cryptos = [
#     "Bitcoin", "Ethereum", "Binance Coin", "Solana", "XRP", "Cardano", "Dogecoin",
#     "Polygon", "Polkadot", "Tether", "Litecoin", "Chainlink", "Uniswap", "Avalanche",
#     "Cosmos", "Shiba Inu", "Stellar", "TRON", "Near Protocol", "Algorand", "Toncoin",
#     "Arbitrum", "Aptos", "Optimism", "VeChain"
# ]

# # 🔹 Liste des subreddits pertinents
# # subreddits = ["CryptoCurrency", "CryptoMarkets"]
# # 🔹 Liste des subreddits pertinents
# subreddits = [
#     "CryptoCurrency", "CryptoMarkets",  # Subreddits généraux
#     "SHIBArmy", "dogecoin", "litecoin", "cardano", "ripple",
#     "dot", "vechain", "AlgorandOfficial", "cosmosnetwork", "avax", "Tronix"
# ]


# # 🔹 Dossier de sauvegarde
# output_dir = "data/reddit_data"
# os.makedirs(output_dir, exist_ok=True)

# # 🔹 Scraper chaque crypto et sauvegarder un fichier par crypto
# for crypto in cryptos:
#     print(f"🔍 Scraping Reddit pour {crypto}...")

#     all_posts = []  # Stocker les posts de cette crypto

#     for subreddit_name in subreddits:
#         print(f"🔹 Scraping dans {subreddit_name}...")

#         try:
#             subreddit = reddit.subreddit(subreddit_name)

#             for post in subreddit.search(crypto, sort="hot", time_filter="year", limit=1000):
#                 all_posts.append({
#                     "crypto": crypto,
#                     "subreddit": subreddit_name,
#                     "title": post.title,
#                     "score": post.score,
#                     "comments": post.num_comments,
#                     "created": pd.to_datetime(post.created_utc, unit="s"),
#                     "url": post.url
#                 })
            
#             time.sleep(3)  # Pause pour éviter un blocage API Reddit

#         except Exception as e:
#             print(f"⚠️ Erreur avec {subreddit_name} pour {crypto}: {e}")

#     # 🔹 Convertir en DataFrame
#     df_reddit = pd.DataFrame(all_posts)

#     # 🔹 Sauvegarde dans un fichier spécifique
#     output_file = os.path.join(output_dir, f"{crypto.lower().replace(' ', '_')}_posts.csv")
#     df_reddit.to_csv(output_file, index=False, encoding="utf-8")

#     print(f"✅ Scraping terminé pour {crypto} ! {df_reddit.shape[0]} posts sauvegardés dans {output_file}\n")

# print("🚀 Scraping Reddit COMPLET pour toutes les cryptos !")


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
    "Polygon": ["CryptoCurrency", "CryptoMarkets"],
    "Polkadot": ["dot", "CryptoCurrency"],
    "Tether": ["CryptoCurrency", "CryptoMarkets"],
    "Litecoin": ["litecoin", "CryptoCurrency"],
    "Chainlink": ["CryptoCurrency", "CryptoMarkets"],
    "Uniswap": ["CryptoCurrency", "CryptoMarkets"],
    "Avalanche": ["avax", "CryptoCurrency"],
    "Cosmos": ["cosmosnetwork", "CryptoCurrency"],
    "Shiba Inu": ["SHIBArmy", "CryptoCurrency"],
    "Stellar": ["CryptoCurrency", "CryptoMarkets"],
    "TRON": ["Tronix", "CryptoCurrency"],
    "Near Protocol": ["CryptoCurrency", "CryptoMarkets"],
    "Algorand": ["AlgorandOfficial", "CryptoCurrency"],
    "Toncoin": ["CryptoCurrency", "CryptoMarkets"],
    "Arbitrum": ["CryptoCurrency", "CryptoMarkets"],
    "Aptos": ["CryptoCurrency", "CryptoMarkets"],
    "Optimism": ["CryptoCurrency", "CryptoMarkets"],
    "VeChain": ["vechain", "CryptoCurrency"]
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
