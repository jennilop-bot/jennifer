# Ejercicio 5: Triángulo Válido
lado1 = 5
lado2 = 6
lado3 = 10

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Los lados", lado1, ",", lado2, "y", lado3, "forman un triángulo válido")
else:
    print("Los lados", lado1, ",", lado2, "y", lado3, "no forman un triángulo válido")
