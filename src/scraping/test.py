import pandas as pd
# data/raw/articles_bitcoin.csv
# data\raw\articles_ethereum.csv
# data\raw\articles_sol.csv
# data\raw\articles_xrp.csv
#

# Charger les données
file_path = "data/raw/articles_xrp.csv"
df = pd.read_csv(file_path)

# Aperçu des données
print(df.head())  # Afficher les 5 premières lignes
print(df.info())  # Obtenir des informations sur les colonnes
# Convertir la colonne 'date' en format datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Vérifier les premières dates
print("Dates les plus anciennes :", df['date'].min())
print("Dates les plus récentes :", df['date'].max())