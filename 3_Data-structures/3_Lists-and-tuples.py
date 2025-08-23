"""Ejercicio 3 
Escribir un programa que almacene las asignaturas de un curso (por ejemplo: Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.""" 

school_subjects = ["Geography", "Math", "Physics", "Chemistry", "History", "Language"]
grades = []

for subject in school_subjects:
    grade = float(input(f"Enter your grade in {subject}: "))
    grades.append(grade)

for i in range(len(school_subjects)):
    print(f"In {school_subjects[i]} you got {grades[i]}")
