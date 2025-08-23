import math
"""
Ejercicio 6:
Escribir una función que reciba una muestra de números en una lista y devuelva su promedio.
"""

def average(numbers):
    return sum(numbers) / len(numbers)

nums = [10, 20, 30, 40]
print(average(nums))   # 25.0
