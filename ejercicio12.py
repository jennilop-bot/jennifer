# Ejercicio 12: Mayor y Menor
numeros = [244, 453, 23, 90, 54, 19, 111]
mayor = numeros[0]
menor = numeros[0]
for n in numeros:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
print("Número mayor:", mayor)
print("Número menor:", menor)
