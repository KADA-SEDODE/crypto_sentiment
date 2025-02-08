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

📊 Scraper des actualités cryptos depuis plusieurs sources.
🔍 Analyser le sentiment du marché à l'aide du modèle CryptoBERT.
📈 Calculer les rendements associés aux stratégies de trading.
Nous avons scrapé des données depuis Reddit et CryptoNews, mais seules les données de CryptoNews ont été utilisées pour l'analyse des sentiments et les modèles de prédiction. 📰⚡

---

## ⚙️ Installation

### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/KADA-SEDODE/crypto_sentiment.git
cd crypto-sentiment-api


2️⃣ Créer un environnement virtuel

python -m venv .venv
source .venv/bin/activate  # Pour Linux/macOS
# ou
.venv\Scripts\activate  # Pour Windows
3️⃣ Installer les dépendances
pip install -r requirements.txt

🚀 Lancer l'API
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload

## 📂 Structure du Projet

📦 **PROJET_FINANCE_QUANTITATIVE**
├── 📂 .venv                      # Environnement virtuel Python
├── 📂 data
│   ├── 📂 raw                    # Données brutes scrappées
│   ├── 📂 reddit_data            # Données spécifiques à Reddit
├── 📂 data_processing
│   ├── 📂 data
│   │   ├── 📄 data_cleaning copy.ipynb  # Notebook de nettoyage et preprocessing
│   │   ├── 📄 df_final.csv          # Données finales après preprocessing
│   ├── 📂 scripts                 # Scripts de traitement des données
│       ├── 📂 __pycache__/          # Cache Python
├── 📂 src                         # Code source principal
│   ├── 📂 api                     # API FastAPI
│   │   ├── 📂 __pycache__/         # Cache Python
│   │   ├── 📄 __init__.py          # Initialisation du module API
│   │   ├── 📄 data_api.py          # API pour l'analyse des données et des sentiments
│   │   ├── 📄 main.py              # Point d'entrée principal de l'API
│   │   ├── 📄predict_api.py           # 🤖 API pour analyser les sentiments avec CryptoBERT
│   │   ├── 📄 models.py            # Modèles Pydantic pour les requêtes/réponses
│   │   ├── 📄 scraper_api.py       # API pour le scraping des news cryptos
│   │   ├── 📄 utils.py             # Fonctions utilitaires
│   ├── 📂 scraping                 # Scripts de scraping
│   │   ├── 📂 __pycache__/         # Cache Python
│   │   ├── 📄 __init__.py          # Initialisation du module scraping
│   │   ├── 📄 crypto_prices.py     # Récupération des prix des cryptos
│   │   ├── 📄 reddit_articles.py   # Extraction des articles Reddit
│   │   ├── 📄 reddit_scraper.py    # Scraping depuis Reddit
│   │   ├── 📄 scraping_5cryptos.py # Scraping de 5 cryptos depuis crypto.news
│   │   ├── 📄 utils.py             # Fonctions utilitaires scraping
├── 📄 .gitignore                   # Fichiers à ignorer par Git
├── 📄 README.md                    # Documentation du projet 📖
├── 📄 requirements.txt              # Liste des dépendances Python 📜


📌 Notes Importantes
📁 Les fichiers de données utiles pour l'API sont déjà disponibles dans data/raw/ ✅
➡️ Pas besoin d'exécuter data_cleaning_v2.ipynb, qui peut être très long ! ⚠️
⚡ Le scraping doit être exécuté avant d’analyser les sentiments.
🔄 Si des erreurs surviennent, réinstalle les dépendances avec : pip install -r requirements.txt
