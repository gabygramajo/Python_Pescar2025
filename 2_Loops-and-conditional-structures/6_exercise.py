"""Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
"""

height = int(input("Enter the height of the triangle: "))

for i in range(1, height + 1):
    print("*" * i)