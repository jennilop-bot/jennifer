# Ejercicio N14 Lista Invertida
original = [5, 4, 3, 2, 1]
invertida = []
for i in range(len(original) - 1, -1, -1):
    invertida.append(original[i])
print("Lista invertida:", invertida)
