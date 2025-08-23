"""
Ejercicio 7:
Escribir una función que reciba una lista de números y devuelva otra lista con sus cuadrados.
"""

# --- Versión con función integrada ---
def squares(numbers):
    return [n ** 2 for n in numbers]

# --- Versión Python vanilla ---
def squares_vanilla(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

# Uso
nums = [1, 2, 3, 4]
print(squares(nums))  # [1, 4, 9, 16]
print(squares_vanilla(nums))  # [1, 4, 9, 16]