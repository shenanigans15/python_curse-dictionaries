students = {"Ana": [8, 7, 9], "Luis": [6, 5, 7], "Sofia": [10, 9, 10]}

# Agregar nuevo estudiante
students["Adrian"] = [2, 5, 5]
# Sacar el promedio de un estudiante existente
name = "Luis"
if name in students:
    students_grades = students[name]
    total_grade = (students_grades[0] + students_grades[1] + students_grades[2]) / 3
    if total_grade >= 6.0:
        print(f"{name} aprobó con un promedio de: {total_grade:.2f}")
    else:
        print(f"{name} reprobó con un promedio de: {total_grade:.2f}")
else:
    print("El estudiante no esta registrado")
# El promedio del estudiante nuevo
name = "Adrian"
if name in students:
    students_grades = students[name]
    total_grade = (students_grades[0] + students_grades[1] + students_grades[2]) / 3
    if total_grade >= 6.0:
        print(f"{name} aprobó con un promedio de: {total_grade:.2f}")
    else:
        print(f"{name} reprobó con un promedio de: {total_grade:.2f}")
else:
    print("El estudiante no esta registrado")
