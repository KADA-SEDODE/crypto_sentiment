import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import os
import black

def scrape_articles(base_url, max_days=180, query="BITCOIN", max_pages=300):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    articles_data = []
    page = 1  # Commencer à la première page
    date_limit = datetime.now() - timedelta(days=max_days)  # Limite temporelle

    while page <= max_pages:
        print(f"Scraping page {page}...")

        # Construire l'URL pour la pagination
        url = f"{base_url}/page/{page}/?s={query}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Erreur lors de l'accès à {url}. Statut : {response.status_code}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # Trouver tous les articles sur la page
        articles = soup.find_all("div", class_="search-result-loop")

        if not articles:  # Arrêter si aucune donnée n'est trouvée
            print("Aucun article trouvé sur cette page. Fin du scraping.")
            break

        for article in articles:
            try:
                # Titre
                title_element = article.find("h3", class_="search-result-loop__title")
                title = title_element.text.strip() if title_element else "Titre indisponible"

                # Date
                date_element = article.find("div", class_="search-result-loop__date")
                if date_element:
                    raw_date = date_element.text.strip()
                    # Convertir la date en format datetime (anglais avec am/pm)
                    article_date = datetime.strptime(raw_date, "%B %d, %Y at %I:%M %p")
                else:
                    article_date = None

                # Vérifier si l'article est dans la limite des 6 mois
                if article_date and article_date < date_limit:
                    continue  # Ignorer les articles trop anciens

                # Description ou résumé (si disponible)
                description_element = article.find("div", class_="search-result-loop__summary")
                description = description_element.text.strip() if description_element else "Description indisponible"

                # Ajouter les données de l'article
                articles_data.append({
                    "title": title,
                    "date": article_date.strftime("%Y-%m-%d %H:%M:%S") if article_date else "Inconnu",
                    "description": description
                })
            except Exception as e:
                print(f"Erreur lors de l'extraction d'un article : {e}")
                continue

        # Sauvegarde partielle après chaque page
        save_partial_data(articles_data, "data/raw/articles_partiels.csv")

        # Passer à la page suivante
        page += 1

    return articles_data

def save_partial_data(articles_data, file_path):
    """Sauvegarde les données partiellement collectées dans un fichier CSV."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df = pd.DataFrame(articles_data)
        df.to_csv(file_path, index=False, encoding="utf-8")
        print(f"Données partiellement sauvegardées dans {file_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données : {e}")

# "Polkadot", "Dogecoin ", "Tether ", "Cardano ","Polygon","BITCOIN", "ETHEREUM",
# cryptos = ["Binance Coin BNB","Ripple XRP", "Solana SOL"]  # Liste des nouveaux cryptos



# ✅ Liste mise à jour des **25 cryptos** à scraper

cryptos = ["Binance Coin","Bitcoin","Cardano","Dogecoin","Ethereum","Litecoin","Shiba Inu","Solana","Tether","TRON","XRP"]


base_url = "https://crypto.news"

# ❌ On met en commentaire l'exécution automatique
"""  
for crypto in cryptos:
    print(f"🚀 Scraping articles pour {crypto}...")
    file_path = f"data/raw/articles_{crypto.lower().replace(' ', '_')}.csv"
    articles = scrape_articles(base_url, max_days=180, query=crypto, max_pages=300)
    save_partial_data(articles, file_path)
    print(f"✅ Terminé pour {crypto}. Données sauvegardées dans {file_path}.\n")

print("🎯 **Scraping terminé pour toutes les 11 cryptos !**")
"""

# Exécuter le scraping SEULEMENT si ce script est exécuté directement
if __name__ == "__main__":
    base_url = "https://crypto.news"

    for crypto in cryptos:
        print(f"🚀 Scraping articles pour {crypto}...")
        file_path = f"data/raw/articles_{crypto.lower().replace(' ', '_')}.csv"
        articles = scrape_articles(base_url, max_days=180, query=crypto, max_pages=300)
        save_partial_data(articles, file_path)
        print(f"✅ Terminé pour {crypto}. Données sauvegardées dans {file_path}.\n")

    print("🎯 **Scraping terminé pour toutes les cryptos !**")
