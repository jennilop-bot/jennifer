#Datos personales del usuario 
name = input("ingrese su nombre:")
lastname= input("ingrese su apellido;")
mail = input("ingrese su correo;")
age = input("ingrese su edad:")
sexo = input("ingrese su sexo;")
birthyear = input("Ingrese su fecha de nacimiento;")

age = int(age)
phone = input("Ingrese su numero de telefono:")
phone = str(phone)
#Año de nacimiento 
birthyear = 2026 - age 
print(f"Tu año de nacimiento es: {birthyear}"
      )
print (f"Nombre: {name}")
print(f"apellido {lastname}")
print(f"correo: {mail}")
print(f"Edad: {age}")
print(f"Sexo: {sexo}")
print(f"telefono: {phone}")