import math
"""
Ejercicio 5:
Escribir una función que calcule el área de un círculo y otra que calcule
el volumen de un cilindro usando la primera función.
"""


def circle_area(radius):
    return math.pi * radius ** 2

def cylinder_volume(radius, height):
    return circle_area(radius) * height

# Uso
print(circle_area(5))        # 78.5398
print(cylinder_volume(5, 10))  # 785.398
