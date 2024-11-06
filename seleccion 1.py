def selection_sort_students(students):
    n = len(students)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
           
            avg_i = sum(students[i][1]) / len(students[i][1])
            avg_j = sum(students[j][1]) / len(students[j][1])
            if avg_j > avg_i:
                max_idx = j
 
        students[i], students[max_idx] = students[max_idx], students[i]
        print(f"Iteración {i + 1}: {students}")
    
    return students
estudiantes = [
    ("Carlos", [90, 85, 88]),
    ("Ana", [88, 92, 84]),
    ("Luis", [80, 75, 90]),
    ("Marta", [95, 99, 92]),
    ("Pedro", [70, 65, 75])
]
print("Lista original de estudiantes:", estudiantes)
estudiantes_ordenados = selection_sort_students(estudiantes)
print("Lista ordenada por promedio de calificaciones:", estudiantes_ordenados)
