# Ejercicio N39 Intersección de Listas
lista1 = [6,7,8,9,10]
lista2 = [5,4,3,2,1]

interseccion = []
for elemento in lista1:
    if elemento in lista2 and elemento not in interseccion:
        interseccion.append(elemento)

print("Intersección:", interseccion)
