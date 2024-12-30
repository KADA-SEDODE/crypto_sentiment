# indicators_calculator.py

import pandas as pd

# Fonction pour calculer le RSI (Relative Strength Index)
def calculate_rsi(data, window=14):
    """
    Calcule le RSI (Relative Strength Index) pour un DataFrame donné.

    Parameters:
        data (pd.DataFrame): Le DataFrame contenant les prix historiques (colonne 'Close').
        window (int): La période de calcul (par défaut 14).

    Returns:
        pd.DataFrame: Le DataFrame avec une nouvelle colonne 'RSI'.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return data

# Fonction pour calculer le MACD (Moving Average Convergence Divergence)
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    """
    Calcule le MACD pour un DataFrame donné.

    Parameters:
        data (pd.DataFrame): Le DataFrame contenant les prix historiques (colonne 'Close').
        short_window (int): Période pour la moyenne mobile courte (par défaut 12).
        long_window (int): Période pour la moyenne mobile longue (par défaut 26).
        signal_window (int): Période pour la ligne de signal (par défaut 9).

    Returns:
        pd.DataFrame: Le DataFrame avec les colonnes 'MACD' et 'Signal Line'.
    """
    data['EMA12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    return data

# Fonction pour calculer les Bandes de Bollinger
def calculate_bollinger_bands(data, window=20):
    """
    Calcule les Bandes de Bollinger pour un DataFrame donné.

    Parameters:
        data (pd.DataFrame): Le DataFrame contenant les prix historiques (colonne 'Close').
        window (int): Période pour la moyenne mobile simple (par défaut 20).

    Returns:
        pd.DataFrame: Le DataFrame avec les colonnes 'Upper Band', 'Lower Band', et 'SMA'.
    """
    data['SMA'] = data['Close'].rolling(window=window).mean()
    data['Upper Band'] = data['SMA'] + (data['Close'].rolling(window=window).std() * 2)
    data['Lower Band'] = data['SMA'] - (data['Close'].rolling(window=window).std() * 2)
    return data

# Fonction pour enrichir un DataFrame avec tous les indicateurs techniques
def enrich_with_indicators(data):
    """
    Ajoute le RSI, le MACD et les Bandes de Bollinger à un DataFrame donné.

    Parameters:
        data (pd.DataFrame): Le DataFrame contenant les prix historiques.

    Returns:
        pd.DataFrame: Le DataFrame enrichi avec les indicateurs techniques.
    """
    data = calculate_rsi(data)
    data = calculate_macd(data)
    data = calculate_bollinger_bands(data)
    return data
