from pathlib import Path
import pandas as pd

archivo_excel = Path(__file__).parent / "students.xlsx"

# Leer por hoja indicando el nombre o su indice
df = pd.read_excel(archivo_excel, sheet_name="Hoja 1")
#df = pd.read_excel(archivo_excel, sheet_name=0)

# Mostrar nombres de columnas
print(df.columns)

# Filtrar
estudiantes_aprobados = df[df["Grade"] > 70]
print(estudiantes_aprobados)