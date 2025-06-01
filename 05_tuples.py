# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
first_tuple=(10, 20, 30, 40, 50)
print(first_tuple)
print(type(first_tuple))

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
second_tuple = (100, 200, 300, 400, 500)
print(second_tuple[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
third_tuple=(1,2,3)
#third_tuple[0] = 10

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
print((1, 2, 3, 3, 4, 5, 3).count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
print(("Java", "Python", "JavaScript", "Python").index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
print((1,2,3)+(4,5,6))

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
print((10, 20, 30, 40, 50)[2:4])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
original_tuple = ("rojo", "verde", "azul")
tuple_converted_to_list = list(original_tuple)
tuple_converted_to_list[1] = "amarillo"
resultant_tuple = tuple(tuple_converted_to_list)
print(original_tuple)
print(resultant_tuple)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
del first_tuple
#print(first_tuple)

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
ultimate_tuple = tuple((100,))
print(ultimate_tuple)
print(type(ultimate_tuple))
ultimate_tuple_v2 = (100)
print(ultimate_tuple_v2)
print(type(ultimate_tuple_v2))