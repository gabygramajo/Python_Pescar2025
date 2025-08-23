"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

investment = float(input("Enter the amount to invest: "))
annual_rate = float(input("Enter the annual interest rate (in %): ")) / 100
years = int(input("Enter the number of years: "))

for year in range(1, years + 1):
    investment *= (1 + annual_rate)
    print(f"Year {year}: ${investment:.2f}")