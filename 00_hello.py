#Hola mundo
print('Hola Python')
#Consultar el tipo de dato
print(type("cadena"))

""" Comentario
en varias lineas
"""

''' y otro 
igual'''

# Ejercicio 1:
print("¡Hola Mundo!")

# Ej 2:
# El código del ejercicio anterior pinta por la consola de comandos el texto indicado.

# Ej 3:
print("Mi nombre es Àlex y tengo " + str(34) + " años.")

# Ej 4:
print(type("cadena"))
print(type(1))
print(type(1.0))

# Ej 5:
'''Los tipos de datos son las distintas maneras de categorizar las variables, pueden ser:
 números enteros, flotantes o complejos
 cadenas de texto
 listas
 tuplas 
 etc...'''
# Ej 6:
print("Hola","Mundo")
print("Hola"+"Mundo")

# Ej 7:
name = "Álex"
age = 34
print("Mi nombre es " + name + " y tengo " + str(age) + " años.")
print(f"Mi nombre es {name} y tengo {age} años.")
print("Mi nombre es {} y tengo {} años.".format(name, age))
print("Mi nombre es %s y tengo %d años." % (name, age))
# Ej 8:
print("¿Cómo te llamas?")
inputName = input()
print(f"Hola {inputName}")

# Ej 9:
# Creación de variables
firstNumber = 100
secondNumber = 200
# Imprimir la suma de las variables
print(f"La suma de {firstNumber} y {secondNumber} es {firstNumber + secondNumber}")
# Imprimir el tipo de dato del resultado
print("El tipo de datos es",type(firstNumber + secondNumber))