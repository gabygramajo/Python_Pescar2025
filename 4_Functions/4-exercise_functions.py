"""
Ejercicio 4:
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar.
Si no se indica, aplicar un 21%.
"""

def calculate_invoice(amount, vat=21):
    return amount + (amount * vat / 100)

# Uso
print(calculate_invoice(100))       # 121.0
print(calculate_invoice(100, 10))   # 110.0