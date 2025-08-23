import math

"""
Ejercicio 9:
Escribir una función que calcule el máximo común divisor (MCD) de dos números
y otra que calcule el mínimo común múltiplo (MCM).
"""


def gcd_builtin(a, b):
    return math.gcd(a, b)

def lcm_builtin(a, b):
    return abs(a * b) // math.gcd(a, b)


def gcd_vanilla(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_vanilla(a, b):
    return abs(a * b) // gcd_vanilla(a, b)

# Uso
print(gcd_builtin(24, 36))  # 12
print(lcm_builtin(24, 36))  # 72
print(gcd_vanilla(24, 36))  # 12
print(lcm_vanilla(24, 36))  # 72