"""Ejercicio 5 
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""

numbers = list(range(1, 11))

# Version 1
for number in range(len(numbers), -1, -1):
    if number == min(numbers):
        print(number)
        break    
    print(number, end=', ')

# Version 2
print(", ".join(map(str, numbers[::-1])))