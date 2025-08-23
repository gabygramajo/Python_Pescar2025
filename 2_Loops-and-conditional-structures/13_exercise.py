"""Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""

while True:
    text = input("Say something (type 'exit' to quit): ")
    if text.lower() == "exit":
        print("Program terminated.")
        break
    print(f"You said: {text}")