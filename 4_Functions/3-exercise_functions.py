import math
"""
Ejercicio 3:
Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""


def factorial_vanilla(n):
    result = 1
    
    for i in range(1, n + 1):
        result *= i
        
    return result

def factorial_recursive(n):
    if n == 1:
        return n
    
    return n * factorial_recursive(n - 1) 

def factorial_builtin(n):
    return math.factorial(n)

# Uso
num= 6

print(factorial_vanilla(num))
print(factorial_recursive(num))
print(factorial_builtin(num))