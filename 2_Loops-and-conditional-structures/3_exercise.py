"""Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

num = int(input('Enter an integer greater than 1: '))
for n in range(1, num + 1):
    if n % 2 == 0:
        if n == num:
            print(n)
            continue
        
        print(n, end=', ')