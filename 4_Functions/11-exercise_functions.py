"""
Ejercicio 11:
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia.
Escribir otra función que reciba el diccionario generado y devuelva
una tupla con la palabra más repetida y su frecuencia.
"""

def word_frequency_builtin(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def most_frequent_builtin(freq_dict):
    return max(freq_dict.items(), key=lambda x: x[1])

def word_frequency_vanilla(text):
    words = []
    current = ""
    for char in text.lower():
        if char.isalpha():
            current += char
        elif current:
            words.append(current)
            current = ""
    if current:
        words.append(current)

    freq = {}
    for w in words:
        if w not in freq:
            freq[w] = 1
        else:
            freq[w] += 1
    return freq

def most_frequent_vanilla(freq_dict):
    max_word = None
    max_count = 0
    for word, count in freq_dict.items():
        if count > max_count:
            max_word = word
            max_count = count
    return (max_word, max_count)


text = "Python is great and Python is fun. Learn Python"
freq_builtin = word_frequency_builtin(text)
print(freq_builtin)
print(most_frequent_builtin(freq_builtin))

freq_vanilla = word_frequency_vanilla(text)
print(freq_vanilla)
print(most_frequent_vanilla(freq_vanilla))
