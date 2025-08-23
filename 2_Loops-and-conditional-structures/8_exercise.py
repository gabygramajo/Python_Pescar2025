"""Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

height = int(input("Enter the height of the triangle: ")) * 2

for row in range(1, height + 1, 2):
    for col in range(row, 0, -2):
        print(col, end=' ')
    print("")