import pandas as pd

print("Loading data...")
df = pd.read_parquet('personas_censo2024.parquet', columns=['comuna', 'cod_ciuo'])

print("Creating crosstab matrix...")
# Create a matrix with comunas as rows, cod_ciuo as columns, and count as values
matrix = pd.crosstab(index=df['comuna'], columns=df['cod_ciuo'])

print("Saving to CSV...")
matrix.to_csv('matriz_ciuo_por_comuna.csv')

print("Matrix successfully saved to matriz_ciuo_por_comuna.csv")
