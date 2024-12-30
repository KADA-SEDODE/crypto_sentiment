import pandas as pd

# Fonction pour calculer le RSI
def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return data

# Fonction pour calculer le MACD
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    data['EMA12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    return data

# Fonction pour calculer les Bandes de Bollinger
def calculate_bollinger_bands(data, window=20):
    data['SMA'] = data['Close'].rolling(window=window).mean()
    data['Upper Band'] = data['SMA'] + (data['Close'].rolling(window=window).std() * 2)
    data['Lower Band'] = data['SMA'] - (data['Close'].rolling(window=window).std() * 2)
    return data

# Appliquer les calculs sur ton DataFrame
def enrich_with_indicators(data):
    data = calculate_rsi(data)
    data = calculate_macd(data)
    data = calculate_bollinger_bands(data)
    return data



import yfinance as yf

# Télécharger les données historiques pour ExxonMobil
data_XOM = yf.download('XOM', start='2015-01-01', end='2024-11-30')
# Ajouter une colonne pour le ticker
data_XOM['Ticker'] = 'XOM'
# Réorganiser les colonnes pour avoir "Ticker" au début
data_XOM = data_XOM.reset_index()  # On remet la date comme une colonne normale
data_XOM = data_XOM[['Ticker', 'Date', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']]
# Aplatir les colonnes du data_XOMFrame
data_XOM.columns = [' '.join(col).strip() for col in data_XOM.columns.values]

data_XOM.rename(columns={
    'Adj Close XOM': 'Adj Close',
    'Close XOM': 'Close',
    'High XOM': 'High',
    'Low XOM': 'Low',
    'Open XOM': 'Open',
    'Volume XOM': 'Volume'
}, inplace=True)

# Afficher le data_XOMFrame final
data_XOM.head()
