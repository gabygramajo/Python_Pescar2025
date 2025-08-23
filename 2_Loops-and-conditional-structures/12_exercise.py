"""Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase."""

print("### WELCOME TO THE LETTER COUNTER ###")

phrase = input("Enter a phrase: ").lower()
letter = input("Enter a letter to count: ").lower()

#opción 1
count = phrase.count(letter)
print(f"The letter '{letter}' appears {count} times in the phrase.")

#opción 2
count = 0
for char in phrase:
    if char == letter:
        count += 1

print(f"The letter '{letter}' appears {count} times in the phrase.")
