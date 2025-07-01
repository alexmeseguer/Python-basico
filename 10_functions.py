# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name = "desconocido"):
    print(f"Hola, {name}")

# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiply(first_number: int, second_number):
    return first_number * second_number

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(integer: int):
    return integer % 2 == 0

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(text: str):
    return text.upper()

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*numbers: float):
    return sum(numbers)

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(name: str, surname: str):
    print(f"Hola, {name} {surname}")

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base: int, exp: int):
    return pow(base,exp)

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
def calculate_average(first_num: float, second_num: float, third_num: float):
    return (first_num + second_num + third_num) / 3

# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_characters(text: str):
    return len(text)

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*texts: str):
    for text in texts:
        print(convert_to_uppercase(text))

# Pruebas de las funciones
personalized_greeting()
personalized_greeting("Pau")
print(multiply(2,23))
print(is_even(21))
print(is_even(22))
print(convert_to_uppercase("en mayúsuculas"))
print(arbitrary_sum(1,2,1.5,0))
generate_full_greeting("Pepe", "Botella")
print(power(2,3))
print(calculate_average(2,3,4))
print(count_characters("texto"))
display_messages("textos", "en", "mayúsculas")