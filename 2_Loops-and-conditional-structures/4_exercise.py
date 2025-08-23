"""Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""
num = int(input('Enter a positive integer greater than 1: '))

for n in range(num, -1, -1):
    if n == 0:
        print(n)
        break
    print(n, end=',')