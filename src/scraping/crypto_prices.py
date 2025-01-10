import yfinance as yf
import pandas as pd
import time

# 📌 Liste des 15 cryptos sélectionnées
CRYPTOS = {
    "Bitcoin": "BTC-USD",
    "Ethereum": "ETH-USD",
    "Binance Coin": "BNB-USD",
    "Solana": "SOL-USD",
    "XRP": "XRP-USD",
    "Cardano": "ADA-USD",
    "Dogecoin": "DOGE-USD",
    "Polygon": "MATIC-USD",
    "Polkadot": "DOT-USD",
    "Avalanche": "AVAX-USD",
    "Shiba Inu": "SHIB-USD",
    "Chainlink": "LINK-USD",
    "Litecoin": "LTC-USD",
    "Cosmos": "ATOM-USD",
    "Uniswap": "UNI-USD"
}

# 📅 Période : 12 derniers mois (Mai 2023 - Aujourd'hui)
PERIOD = "2y"
INTERVAL = "1d"

# Dictionnaire pour stocker les données
crypto_data = {}

# Fonction pour récupérer les prix historiques (Open, High, Low, Close, Volume )
def get_historical_prices(symbol):
    try:
        data = yf.download(symbol, period=PERIOD, interval=INTERVAL)
        data.reset_index(inplace=True)
        return data[["Date", "Open", "High", "Low", "Close", "Volume"]].rename(
            columns={
                "Open": f"{symbol}_Open",
                "High": f"{symbol}_High",
                "Low": f"{symbol}_Low",
                "Close": f"{symbol}_Close",
                "Volume": f"{symbol}_Volume"
            }
        )
    except Exception as e:
        print(f"❌ Erreur pour {symbol} : {str(e)}")
        return None

# Collecte des prix pour toutes les cryptos
for name, symbol in CRYPTOS.items():
    print(f"📊 Récupération des prix de {name} ({symbol})...")
    df = get_historical_prices(symbol)
    if df is not None:
        crypto_data[symbol] = df

# Fusionner toutes les cryptos sur la même colonne "Date"
df_final = None
for symbol, df in crypto_data.items():
    if df_final is None:
        df_final = df  # Premier DataFrame
    else:
        df_final = pd.merge(df_final, df, on="Date", how="outer")  # Fusionner sur "Date"

# Sauvegarde des données en CSV bien formaté
df_final.to_csv("data/raw/crypto_prices_historical_12months_fixed.csv", index=False, sep=",", encoding="utf-8")

print("✅ Données enregistrées dans data/raw/crypto_prices_historical_12months_fixed.csv avec un format aligné.")
