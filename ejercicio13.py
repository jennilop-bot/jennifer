# Ejercicio numero 13 Eliminar Duplicados
lista = [2, 2, 3, 3, 4, 4, 3, 8, 8]
sin_duplicados = []
for elemento in lista:
    if elemento not in sin_duplicados:
        sin_duplicados.append(elemento)
print("Lista sin duplicados:", sin_duplicados)
