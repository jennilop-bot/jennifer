# Ejercicio 23: Notas de Estudiantes
notas = {"Hilary": 75, "Jose": 92, "lore": 23}
promedio = sum(notas.values()) / len(notas)
mejor_estudiante = max(notas, key=notas.get)
print("Promedio de notas:", promedio)
print("Estudiante con mayor nota:", mejor_estudiante, "(", notas[mejor_estudiante], ")")
