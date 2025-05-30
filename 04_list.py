# 1. Crea una lista con los números del 1 al 5 e imprímela.
units_list = [1, 2, 3, 4, 5]
print(units_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
tens_list = [10, 20, 30, 40, 50]
print(tens_list[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
units_list.append(6)
print(units_list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
tens_list.insert(1,15)
print(tens_list)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
list_5 = [10, 20, 30, 30, 40, 50]
print(list_5)
list_5.remove(30)
print(list_5)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
units_list.pop()
five =units_list.pop()
print(five)
print(units_list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
hundreds = [100, 200, 300, 400, 500]
hundreds.reverse()
print(hundreds)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
unordered_list = [3, 1, 4, 2, 5]
unordered_list.sort()
print(unordered_list)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
first_list = [1, 2, 3] 
second_list = [4, 5, 6] 
both_lists = first_list + second_list
print(both_lists)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
main_list = [10, 20, 30, 40, 50]
print(main_list[1:3])