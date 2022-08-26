### Variables ###

# La definición de variables no requieren de una palabra reservada.
# La convención de nombramiento de variables es con snake_case.
# El tipo de la variable es dinámico al momento de asignarle un valor.
from audioop import add


my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

# Declaración de variable y cambio de tipo con función de sistema a Str.
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:",my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
# Hay que tener mucho cuidado al usar esta sintaxis.
name, surname, alias, age = "Francisco", "Palma", "EdpaDev", 33
print("Me llamo:",name, surname,". Mi edad es:", age,". Y mi alias es:", alias)

# Input
#name = input('¿Cuál es tu nombre? ')
#age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 33
age = "Francisco"
print(name)
print(age)

# ¿Forzamos el tipo?
address : str = "Mi dirección"
address = True
address = 3
address = 1.7
print(address)
print(type(address))