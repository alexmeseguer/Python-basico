# 1. Crea un set con los números del 1 al 5 e imprímelo.
first_set = set({1,2,3,4,5})
print(first_set)
print(type(first_set))
second_set = {1,2,3,4,5}
print(second_set)
print(type(second_set))

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
first_set.add(6)
print(first_set)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
#NADA, no se puede añadir, ya existe
first_set.add(5)
print(first_set)

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in second_set)

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
second_set.remove(4)
print(second_set)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
second_set.clear()
print(len(second_set))

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
fruits_set = {"manzana", "naranja", "plátano"} 
fruits_set = list(fruits_set)
print(fruits_set[0])

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
start_set = {1,2,3}
end_set = {4,5,6}
result_set = start_set.union(end_set)
print(result_set)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
diff_sets= {1, 2, 3, 4}.symmetric_difference({3, 4, 5, 6} )
print(diff_sets)

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
del diff_sets
#print(diff_sets)