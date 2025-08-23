# Ejercicios Prácticos - Bucles
"""Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

word = input('Enter a single word: ')
for n in range(1, 11):
    print(f"{n} {word}")
