# Ejercicio 3: Año Bisiesto
año = 2022
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(año, "este un año bisiesto")
else:
    print(año, "este no es un año bisiesto")
