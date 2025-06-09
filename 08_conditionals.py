def requestNumber(inputText =  " -> Introduce un número:"):
    number = input(inputText)
    try:
        floatNumber = float(number)
        return floatNumber
    except ValueError:
        print("El valor introducido no es numérico")
        return None

# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
floatNumber = requestNumber()
if floatNumber:
    if floatNumber > 0:
        print("Número positivo")
    elif floatNumber == 0:
        print("El número es cero")
    elif floatNumber < 0:
        print("Número negativo")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad (18 años o más) o menor de edad.
age = int(input(" -> Qué edad tienes\n"))
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
inputString = input(" -> Introduzca texto:\n")
if inputString:
    print("El texto introducido es:\n" + inputString)
else:
    print("Texto NO introducido")


# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
firstNumber = requestNumber()
secondNumber = requestNumber(" -> Introduzca otro número:")

if firstNumber and secondNumber:
    if firstNumber > secondNumber:
        print(f"{firstNumber} es mayor que {secondNumber}")
    elif firstNumber < secondNumber:
        print(f"{firstNumber} es menor que {secondNumber}")
    else:
        print(f"{firstNumber} es igual que {secondNumber}")
else:
    print("Ambos valores deben ser numéricos")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
divisibleNumber = requestNumber(" -> Añade un número entero para saber si es divisible entre 3 y 5:\n")

if divisibleNumber % 3 == 0 and divisibleNumber % 5 == 0:
    print(f"{divisibleNumber} es divisible entre 3 y 5")
elif divisibleNumber % 3 == 0:
    print(f"{divisibleNumber} solo es divisible entre 3")
elif divisibleNumber % 5 == 0:
    print(f"{divisibleNumber} solo es divisible entre 5")
else:
    print("No es divisible entre 3 ni 5")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
evenNumber = requestNumber(" -> Añade un número entero para saber si es par o impar:\n")
if evenNumber % 2 == 0:
    print(f"{evenNumber} es un número par")
elif evenNumber % 2 > 0:
    print(f"{evenNumber} es un número impar")
else:
    print(f"No te puedo decir si {evenNumber} es un número par o impar")


# 7. Escribe un programa que determine si una persona puede votar en función de su edad (mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.

if age >= 18:
    print("Por cierto, con tu edad SÍ puedes votar.")
elif age >= 16:
    print("Por cierto, con tu edad puedes votar con un permiso especial.")
else:
    print("Por cierto, con tu edad NO puedes votar.")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
definedPass = "pass"
inputPass = input(" --> Introduzca una contraseña:\n")
if definedPass == inputPass:
    print("La contraseña es correcta.")
else:
    print("Contraseña incorrecta.")

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
numberInRange = requestNumber()
if(numberInRange >= 10 and numberInRange <= 20):
    print(f"{numberInRange} está entre 10 y 20, ambos inclusive")
else:
    print(f"{numberInRange} está fuera del rango de 10 y 20, ambos inclusive")


# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color (rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
colorInput = input(" --> Elige un color: rojo, verde o amarillo:\n")
colorInputLower = colorInput.lower()
if colorInputLower == 'r' or colorInputLower == "rojo":
    print("Debe detenerse")
elif colorInputLower == 'v' or colorInputLower == 'verde':
    print("Avanza")
elif colorInputLower == 'a' or colorInputLower == 'amarillo':
    print("Precaución")
else:
    print("No corresponde al color del semáforo")





