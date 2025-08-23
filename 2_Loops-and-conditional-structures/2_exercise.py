"""Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

age = int(input('Hi! How old are you? '))
for year in range(1, age + 1):
    if year == 1:
        print(f"{year} year")
        continue
    print(f"{year} years")
