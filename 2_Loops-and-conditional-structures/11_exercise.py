"""Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última."""

print("### WELCOME TO THE CHAR COUNTER ###")
word = input('Enter a any word: ')

for char in word[::-1]:
    print(char, end='')