from pathlib import Path 
import json

ruta_persona = Path(__file__).parent / "persona.json"

#Diccionario
persona = {"nombre":"Ana", "edad":25, "pais":"Costa Rica"}

#Guardar Diccionario como Json
# with open( ruta_persona, "w", encoding="utf-8") as f:
#     json.dump(persona, f, indent=4)

#Leer JSON
with open(ruta_persona, "r", encoding="utf-8") as f:
    data = json.load(f)
    
print(data["nombre"])