"""Ejercicio 6 
Escribir un programa que almacene las asignaturas de un curso (por ejemplo: Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

school_subjects = ["Math", "Physics", "Chemistry", "History", "Language"]
failed_subjects = []

for subject in school_subjects:
    grade = float(input(f"Enter your grade in {subject}: "))
    if grade < 6:
        failed_subjects.append(subject)

print("You need to repeat:", failed_subjects)