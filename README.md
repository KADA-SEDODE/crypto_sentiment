# 🚀 Crypto Sentiment API

Une API permettant d'interagir avec le scraping de données financières, l'analyse de sentiment via **CryptoBERT** et la gestion des données cryptos.

## 📖 Table des matières
- [📌 Présentation](#-présentation)
- [⚙️ Installation](#%EF%B8%8F-installation)
- [🚀 Lancer l'API](#-lancer-lapi)
- [🛠️ Fonctionnalités](#%EF%B8%8F-fonctionnalités)
- [📂 Structure du Projet](#-structure-du-projet)
- [📡 Endpoints de l'API](#-endpoints-de-lapi)
- [📌 Notes Importantes](#-notes-importantes)

---

## 📌 Présentation

Ce projet a pour objectif :

📊 Scrapper des actualités cryptos depuis plusieurs sources.
🔍 Analyser le sentiment du marché à l'aide du modèle CryptoBERT.
📈 Calculer les rendements associés aux stratégies de trading.
Nous avons scrapé des données depuis Reddit et CryptoNews, mais seules les données de CryptoNews ont été utilisées pour l'analyse des sentiments et les modèles de prédiction dans cet API. 📰⚡

---

## ⚙️ Installation

### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/KADA-SEDODE/crypto_sentiment.git
cd crypto-sentiment-api


### 2️⃣ Créer un environnement virtuel

python -m venv .venv
source .venv/bin/activate  # Pour Linux/macOS
# ou
.venv\Scripts\activate  # Pour Windows
### 3️⃣ Installer les dépendances
pip install -r requirements.txt

🚀 Lancer l'API
uvicorn src.api.main:app --reload

## 📂 Structure du Projet

📦 PROJET_FINANCE_QUANTITATIVE
├── 📂 .venv # Environnement virtuel Python
├── 📂 data
│ ├── 📂 raw # 📊 Données brutes scrappées (articles, prix, sentiments, rendements)
│ ├── 📂 reddit_data # 📊 Données spécifiques à Reddit
├── 📂 data_processing
│ ├── 📂 data
│ │ ├── 📄 data_cleaning_cryptonews_only.ipynb # Notebook de nettoyage des articles crypto
│ │ ├── 📄 data_cleaning_cryptonews_reddit.ipynb # Notebook de nettoyage des articles Reddit
├── 📂 scripts # 📜 Scripts de traitement des données
│ ├── 📂 pycache/ # ⚙️ Cache Python
├── 📂 src # 📂 Code source principal
│ ├── 📂 api # 🚀 API FastAPI
│ │ ├── 📂 pycache/ # ⚙️ Cache Python
│ │ ├── 📄 init.py # Initialisation du module API
│ │ ├── 📄 data_api.py # API pour l'analyse des données et des sentiments
│ │ ├── 📄 main.py # Point d'entrée principal de l'API
│ │ ├── 📄 predict_api.py # 🤖 API pour analyser les sentiments avec CryptoBERT
│ │ ├── 📄 models.py # Modèles Pydantic pour les requêtes/réponses
│ │ ├── 📄 scraper_api.py # API pour le scraping des news cryptos
│ │ ├── 📄 utils.py # Fonctions utilitaires pour l'API
│ ├── 📂 scraping # 📡 Scripts de scraping
│ │ ├── 📂 pycache/ # ⚙️ Cache Python
│ │ ├── 📄 init.py # Initialisation du module scraping
│ │ ├── 📄 crypto_prices.py # Récupération des prix des cryptos via Yahoo Finance
│ │ ├── 📄 reddit_scraper.py # Scraping des articles Reddit
│ │ ├── 📄 scraping_5cryptos.py # Scraping des articles de cryptos depuis crypto.news
├── 📄 .gitignore # 🚫 Fichiers à ignorer par Git
├── 📄 README.md # 📖 Documentation du projet
├── 📄 requirements.txt # 📜 Liste des dépendances Python

📌 Notes Importantes
📁 Les fichiers de données utiles pour l'API sont déjà disponibles dans data/raw/ 
⚡ Le scraping doit être exécuté avant d’analyser les sentiments.
🔄 Si des erreurs surviennent, réinstallez les dépendances avec : pip install -r requirements.txt
⚡ De préférence, utilisez Google Chrome pour exécuter l'API.

## 📡 Endpoints de l'API

🔹 1️⃣ Scraping des articles
📌 Endpoint : POST /scrape/scrape
📌 Description : Scrape des articles sur une crypto depuis une source donnée.
 
 📌 Exemple de requête JSON
{
  "crypto": "Bitcoin",
  "source": "crypto.news",
  "limit": 10
}

🔹 2️⃣ Analyse du sentiment d’un texte
📌 Endpoint : POST /predict/predict
📌 Description : Analyse le sentiment d’un texte donné avec CryptoBERT.
📌 Exemple de requête JSON :

{
  "description": "Bitcoin atteint un nouveau record historique !"
}

🔹 3️⃣ Récupération des données de prix
📌 Endpoint : GET /data/get_crypto_data
📌 Description : Retourne les données de prix des cryptos stockées.

🔹 4️⃣ Analyse de sentiment sur les données stockées
📌 Endpoint : POST /data/analyze_sentiment
📌 Description : Analyse les sentiments des articles stockés.

🔹 5️⃣ Calcul des rendements du portefeuille
📌 Endpoint : GET /data/compute_portfolio_returns
📌 Description : Calcule les rendements du portefeuille de cryptos.

🔹 6️⃣ Récupération des statistiques du portefeuille
📌 Endpoint : GET /data/portfolio_statistics
📌 Description : Retourne les métriques de performance du portefeuille.

🔹 7️⃣ Affichage du graphique des rendements cumulés
📌 Endpoint : GET /data/plot_cumulative_returns
📌 Description : Retourne une image du graphique des rendements cumulés.
