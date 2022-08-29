### Strings ###

from re import A


my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) # Concatenación de variables y cadena de texto definida en ejecución.

my_new_line_string = "Este es un String\ncon salto de línea" # Uso de operador de salto de línea dentro de cadena de texto.
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # Uso de operador de tabulación dentro de cadena de texto.
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado" # Uso de operador para que no reconozca los comandos anteriores.
print(my_scape_string)

# Formateo

name, surname, age = "Francisco", "Palma", 33

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # El uso de format requiere {} en la posición de los valores a formatear.
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # El uso de % para formateo requiere de los parámetros tipado en el texto.
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Esta línea lleva el formateo de texto con variables a la antigua. No es recomendado.
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Variante de formateo usando el prefijo f antes de la cadena de texto y las variables entre llaves.

# Desempaquetado de caracteres
language = "python"
#a, b = language # ValueError: too many values to unpack (expected 2)
a, b, c, d, e , f = language
print(a)
print(e)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3] # Toma el valor en la posicion 1 (segunda desde cero) hasta un valor antes del segundo parámetro 3.
print(language_slice)

language_slice = language[1:] # Toma el valor de y junto a todos los caracteres hasta llegar al final del String.
print(language_slice)

language_slice = language[-2] # Toma el valor de o contado del final hacia el inicio.
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1] # Función que revierte el orden de todos los caracteres.
print(reversed_language) 

# Funciones

print(language.capitalize()) # Función que pone la primera letra en mayúsculas.
print(language.upper()) # Función que pone todas las letra en mayúsculas.
print(language.count("t")) # Función que retorna la cantidad de ocurrencias del parámetro en la cadena que estamos manipulando.
print(language.isnumeric()) # Función que valida si el valor de la variable es numérico.
print("1".isnumeric())
print(language.lower()) # Función que pone todas las letra en minúsculas.
print(language.lower().isupper()) # Concatenación de funciones sobre variable de tipo String.
print(language.startswith("Py")) # Función que valida un parámetro contra el valor de la variable.
print("Py" == "py") # No es lo mismo por el case.