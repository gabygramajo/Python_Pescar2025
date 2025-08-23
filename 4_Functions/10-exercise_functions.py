"""
Ejercicio 10:
Escribir una función que convierta un número decimal en binario
y otra que convierta un número binario en decimal.
"""

def decimal_to_binary_builtin(n):
    return bin(n)[2:]

def binary_to_decimal_builtin(b):
    return int(b, 2)

def decimal_to_binary_vanilla(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def binary_to_decimal_vanilla(b):
    decimal = 0
    power = 0
    for digit in reversed(b):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

# Uso
print(decimal_to_binary_builtin(10))   # 1010
print(binary_to_decimal_builtin("1010"))  # 10
print(decimal_to_binary_vanilla(10))   # 1010
print(binary_to_decimal_vanilla("1010"))  # 10