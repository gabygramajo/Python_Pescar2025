"""Ejercicio 5 
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso."""

credits = {"Math": 6, "Physics": 4, "Chemistry": 5, "Geography": 3, "History": 3, "Language": 4}

total_credits = 0
for subject, credit in credits.items():
    print(f"{subject} has {credit} credits")
    total_credits += credit

print(f"Total credits: {total_credits}")