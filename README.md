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

⚙️ Installation

1️⃣ Cloner le projet
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
uvicorn src.api.main:app --reload

