# Ejercicio N37 Máximo Común Divisor
a, b = 25, 15

x, y = a, b
while y != 0:
    x, y = y, x % y

print("MCD de", a, "y", b, ":", x)
