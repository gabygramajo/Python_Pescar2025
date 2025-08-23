import math

"""
Ejercicio 8:
Escribir una función que reciba una lista de números y devuelva un diccionario
con su media, varianza y desviación típica.
"""

def stats_builtin(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    return {"mean": mean, "variance": variance, "std_dev": std_dev}


def stats_vanilla(numbers):
    total = 0
    for n in numbers:
        total += n
    mean = total / len(numbers)

    variance_sum = 0
    for n in numbers:
        variance_sum += (n - mean) ** 2
    variance = variance_sum / len(numbers)

    std_dev = variance ** 0.5
    return {"mean": mean, "variance": variance, "std_dev": std_dev}

# Uso
nums = [2, 4, 4, 4, 5, 5, 7, 9]
print(stats_builtin(nums))
print(stats_vanilla(nums))