# Ejercicio 4 calculadora Simple
num1 = 150
num2 = 222
operador = "+"

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    resultado = None
    print("Operador invalido")

if resultado is not None:
    print(num1, operador, num2, "=", resultado)
