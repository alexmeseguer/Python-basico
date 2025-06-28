def printWording(num):
    print(f'-----------------------\nResultado ejercicio {num}:\n-----------------------')

# 1. Usa un bucle while para imprimir los números del 1 al 10.
printWording(1)
count = 1
while(count < 11):
    print(count)
    count+=1
# 2. Usa un bucle for para recorrer la lista [10, 20, 30, 40, 50] e imprime cada número.
printWording(2)
for ten in [10, 20, 30, 40, 50]:
    print(ten)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
printWording(3)
num, result = 1, 0
while num <= 100:
    result+=num
    num+=1
print("Suma de los números del 1 al 100 =>",result)

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
printWording(4)
for caracter in 'Python':
    print(caracter)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
printWording(5)
num = 1
while num <= 50:
    if(num % 7 == 0 ):
        print(num, 'es divisible entre 7')
        break
    else:
        print(num, 'no es divisible entre 7')
    num +=1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
printWording(6)
for key in {"name": "Brais", "age": 37, "country": "Galicia"}:
    print(key)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
printWording(7)
num = 1
while num<=20:
    if(num % 2 == 0):
        print(num)
    num += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
printWording(8)
for num in range(10,0,-1):
    print(num)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista [30, 10, 30, 20, 30, 40].
printWording(9)
repeats = 0
for i in [30, 10, 30, 20, 30, 40]:
    if(i == 30):
        repeats += 1
print('Número de repeticiones del 30:', repeats,)
 
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
for name in ['Pep', 'Pau', 'Brais', 'Hugo']:
    print(name)
    if(name =='Brais'):
        break