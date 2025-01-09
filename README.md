📂 crypto_sentiment_analysis/
│── 📂 data/                     # Stockage des fichiers CSV ou bases de données
│   ├── raw/                     # Données brutes collectées (avant transformation)
│   ├── processed/                # Données nettoyées et transformées
│   ├── sentiment_scores.csv       # Scores des sentiments après NLP
│   ├── crypto_prices.csv          # Prix des cryptos (historique)
│
│── 📂 notebooks/                 # Contient les analyses exploratoires en Jupyter
│   ├── eda.ipynb                  # Notebook d’analyse exploratoire des données
│   ├── backtesting.ipynb          # Notebook de backtesting des stratégies
│
│── 📂 src/                        # Dossier principal pour le code source
│   ├── 📂 scraping/                # Scripts pour récupérer les données
│   │   ├── yahoo_scraper.py         # Scraper Yahoo Finance
│   │   ├── reddit_scraper.py        # Scraper Reddit
│   │   ├── twitter_scraper.py       # Scraper Twitter
│   │
│   ├── 📂 sentiment_analysis/      # Scripts pour analyser le sentiment
│   │   ├── finbert_analysis.py      # Analyse des textes avec FinBERT
│   │
│   ├── 📂 data_processing/         # Scripts pour traiter et nettoyer les données
│   │   ├── feature_engineering.py   # Création des indicateurs techniques
│   │   ├── data_cleaning.py         # Nettoyage des données
│   │
│   ├── 📂 portfolio_strategy/      # Stratégies d'investissement basées sur le sentiment
│   │   ├── portfolio_builder.py     # Construction du portefeuille HML
│   │   ├── backtest.py              # Script pour backtester la stratégie
│
│   ├── 📂 api/                     # Déploiement de l'API avec FastAPI
│   │   ├── main.py                  # Fichier principal de l’API
│
│── 📂 models/                      # Stockage des modèles entraînés
│   ├── trained_model.pkl            # Modèle ML entraîné
│
│── 📂 tests/                       # Tests unitaires pour s’assurer du bon fonctionnement
│   ├── test_scraping.py             # Tests pour le scraping
│   ├── test_sentiment.py            # Tests pour FinBERT
│
│── 📂 docs/                        # Documentation du projet
│   ├── README.md                    # Explication du projet
│   ├── requirements.txt              # Liste des packages nécessaires
│   ├── config.yaml                   # Fichier de configuration
│
│── .gitignore                      # Ignorer certains fichiers inutiles (ex : fichiers de logs)
│── setup.py                         # Pour transformer le projet en package Python
│── run.py                           # Script principal pour exécuter tout le pipeline
