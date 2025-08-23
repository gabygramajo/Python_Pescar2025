"""Ejercicio 2 
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""

user = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "address": input("Enter your address: "),
    "phone": input("Enter your phone number: ")
}

print(f"{user['name']} is {user['age']} years old, lives at {user['address']}, "
      f"and their phone number is {user['phone']}.")