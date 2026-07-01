# Ejercicio N41 Aplanar Lista Anidada
anidada = [[3, 2], [4, 2, 5], [6]]

plana = []
for sublista in anidada:
    for elemento in sublista:
        plana.append(elemento)

print("Lista aplanada:", plana)
