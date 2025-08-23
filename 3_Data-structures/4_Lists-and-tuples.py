"""Ejercicio 4 
Escribir un programa que pregunte al usuario los números ganadores de la lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.""" 

winning_numbers = []

while True:
    number = input("Enter the winning number (exit for out): ")
    
    if number.lower() == 'exit':
        break
    
    winning_numbers.append(int(number))

winning_numbers.sort()    
print("Winning numbers: ", winning_numbers)