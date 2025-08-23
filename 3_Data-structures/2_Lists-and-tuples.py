"""Ejercicio 2 
Escribir un programa que almacene las asignaturas de un curso (por ejemplo: Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje "Yo estudio <asignatura>", donde <asignatura> es cada una de las asignaturas de la lista."""

school_subjects = ["Geography", "Math", "Physics", "Chemistry", "History", "Language"]

for subject in school_subjects:
    print(f"I study {subject}")