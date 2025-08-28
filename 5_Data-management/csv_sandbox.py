from pathlib import Path 
import csv

ruta_sales = Path(__file__).parent / "sales.csv"
ruta_datos = Path(__file__).parent / "datos.csv"

# Leer
with open(ruta_sales, newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

# Leer como Diccionario
with open(ruta_datos, newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila["Nombre"], "-", fila["Pais"])

with open(ruta_sales, newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(f"{fila["Product"]}: $ {fila["Price"]}, Category: {fila["Category"]}")