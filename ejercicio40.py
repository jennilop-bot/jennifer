# Ejercicio N40 Rotar Lista
lista = [3,2,1,6]
k = 3

k = k % len(lista)
rotada = lista[-k:] + lista[:-k]

print("Lista rotada", k, "posiciones:", rotada)
