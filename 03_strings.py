# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
print("Hola"+ "Python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
print("Frase con saltos\nde líneas\nen pantalla.")

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname, age = "Álex", "Meseguer", 34
print(f"Mi nombre es {name} {surname} y tengo {age} años")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
char1, char2, char3, char4, char5, char6 = "Python"
print(char1)
print(char2)
print(char3)
print(char4)
print(char5)
print(char6)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
print("Programación"[3:8])

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
print("Python"[::-1])


# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
print("aprendiendo python".upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
print("Programación en Python".count('ñ'))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
print("12345".isnumeric())