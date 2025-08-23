"""Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

print("##### WELCOME TO THE PRIME NUMBER DETECTOR ###")

while True:
    number = abs(int(input('Enter an integer other than 1 (0=exit): ')))
    
    if number == 0:
        print("Exit....")
        break
        
    divisors = 1
    for divider in range(2, number + 1):
        if number % divider == 0:
            divisors += 1
    
    if divisors == 2:
        print(f"\n¡¡¡Prime number detected!!!\nThe {number} is indeed a prime number.")
    else:
        print(f"\nThe entered number is not prime number.")

    print("\nDo you want to try again?")