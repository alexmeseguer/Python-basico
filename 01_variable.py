# Variables
my_variable = 10

# EN una línea
name, surname, alias, age = "Álex", "Meseguer", "ameseguer", 34
print("Mi nombre es", name, surname, "-", alias, "-", "y tengo",age, "años.")

# Forzar tipado de datos => Realmente no sirve de nada, es simplemente informativo
name: str = "Álex"
name = 10
print(type(name)) # tipo INT

# Ejercicio de variables en Python
# 1. Declara y asigna valores a las siguientes variables:
# • name: una cadena que contenga tu nombre.
# • age: un número entero que represente tu edad.
# • height: un número flotante que represente tu altura.
# • Imprime cada variable en una línea separada.

name = "Álex"
age = 34
height = 1.84
print("Nombre:", name)
print("Edad:", age)
print("Altura:", height, "m")

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
print("Tengo " + str(age) + " años.")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student = False
print("¿Eres estudiante?", is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
full_name = "Álex Meseguer"
name_length = len(full_name)
print("La longitud de mi nombre completo es:", name_length)

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, surname, city = "Álex", "Meseguer", "Murcia"
print("Nombre:", name, surname, ". Ciudad:", city)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
color = input("¿Cuál es tu color favorito? ")
print("Tu color favorito es:", color)

# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "Manzana"
print("Fruta inicial:", fruit)
fruit = "Plátano"
print("Fruta cambiada:", fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
float_price = 19.99
price = int(float_price)
print("Precio como entero:", price)

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address = "Calle false 123"
address_len = len(address)
print("La dirección:", address, "tiene", address_len, "caracteres.")


# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone: int = 123456789
phone = 987654321
print("Phone sigue siendo del tipo:", type(phone))