"""Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

password = '1234'

while True:
    login_password = input('Enter your Password: ')
    if password == login_password:
        print("\nlogin successful!")
        break
    print('\nIncorrect Password, try again.')