
"""Ejercicio 3 
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. Banana 500, Manzana 300, Pera 400 y Naranja 600."""

prices = {"Banana": 500, "Apple": 300, "Pear": 400, "Orange": 600}
fruit = input("Enter a fruit: ").capitalize()

if fruit in prices:
    kilos = float(input(f"How many kilos of {fruit}? "))
    total = prices[fruit] * kilos
    print(f"The price for {kilos} kg of {fruit} is ${total}")
    
else:
    print("Sorry, we don't have that fruit.")