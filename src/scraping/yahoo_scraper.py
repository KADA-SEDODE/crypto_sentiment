import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timedelta

import json

import requests
import json

import requests
import json

# URL de l'API Yahoo Finance pour récupérer les news (on cible mieux avec "Bitcoin")
URL = "https://query1.finance.yahoo.com/v1/finance/search?q=Bitcoin&newsCount=10"

# Ajouter un User-Agent pour éviter le blocage
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Effectuer la requête HTTP
response = requests.get(URL, headers=headers)

# Vérifier que la requête a réussi
if response.status_code == 200:
    try:
        data = response.json()  # Convertir en dictionnaire Python

        # Extraire la liste des articles
        articles = data.get("news", [])

        # Filtrer les articles contenant "Bitcoin" ou "BTC" dans leur titre
        bitcoin_articles = [article for article in articles if "Bitcoin" in article.get("title", "") or "BTC" in article.get("title", "")]

        if not bitcoin_articles:
            print("Aucune news sur Bitcoin trouvée.")
        else:
            print(f"📌 {len(bitcoin_articles)} articles sur Bitcoin trouvés :\n")
            for article in bitcoin_articles:
                title = article.get("title", "Titre non trouvé")
                link = article.get("link", "Lien non trouvé")
                provider = article.get("publisher", "Source inconnue")
                # Extraire la date au format UNIX (timestamp)
                date_timestamp = article.get("providerPublishTime", None) # 
                
                # Vérifier si la date existe, sinon mettre "Date inconnue"
                
                if date_timestamp:
                    date_formatee = datetime.utcfromtimestamp(date_timestamp).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    date_formatee  = "Date inconnue"
                
                print(f"📌 {title}")
                print(f"🔗 {link}")
                print(f"📰 Source: {provider}")
                print(f"🗓️ Date: {date_formatee}")
                print("-" * 80)

    except json.JSONDecodeError:
        print("Erreur : Impossible de décoder le JSON (données mal formées)")
else:
    print(f"Erreur HTTP {response.status_code}")
from datetime import datetime

# Convertir le timestamp en date lisible
