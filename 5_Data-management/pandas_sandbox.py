from pathlib import Path 
import pandas as pd

ruta_sales = Path(__file__).parent / "sales.csv"
ruta_datos = Path(__file__).parent / "datos.csv"

#Leer un CSV
df = pd.read_csv(ruta_sales)

# Leer las 1ras 5 filas
print(df.head())

#Leer por columna 
print(df["Product"])