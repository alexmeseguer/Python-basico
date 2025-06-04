# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
first_dict = {"name": "Álex", "age": 35, "country": "ES"}
print(first_dict)
print(type(first_dict))
# 2. Accede al valor de la clave name en el diccionario.
print(first_dict["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
first_dict["job"]="Desarrollador de software"
print(first_dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
first_dict["age"]=38
print(first_dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del first_dict["country"]
print(first_dict)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
square_dict = dict({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
print(square_dict)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
brais_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in brais_dict)

# 8. Imprime solo las claves del diccionario.
print(first_dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
keys_list = list(first_dict.keys())
print(keys_list)
print(type(keys_list))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
ultimate_dict = first_dict.fromkeys(["name", "age", "job"],'Desconocido')
print(ultimate_dict)