### Dictionaries ###

# Creación de una variable por medio del constructor
from msilib import MSIMODIFY_DELETE


my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Los elementos estan declarados en relación clave:valor
my_other_dict = {"Nombre":"Francisco","Apellido":"Palma","Edad":33, 1:"Python"}

# De esta manera se puede visualizar las claves y sus valores de forma vertical
my_dict = {
    "Nombre":"Francisco",
    "Apellido":"Palma",
    "Edad":33,
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.80
    }

print(my_other_dict)
print(my_dict)

# Acá observamos la cantidad de claves en un diccionario para no confundir en el conteo de los valores
print(len(my_other_dict))
print(len(my_dict))

# Se puede hacer impresión del valor dada una llave como parámetro
print(my_dict["Nombre"])

# Se puede cambiar el valor de la llave directamente con referenciarla como parámetro
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

# Sintaxis para agregar una nueva clave y su valor al diccionario
my_dict["Calle"] = "Calle Palma"
print(my_dict)

# Sintaxis para borrar la clave según el valor que se pasa como parámetro
del my_dict["Calle"]
print(my_dict)

# La comparación del parámetro en el diccionario funciona validando las claves, no los valores
print("Palma" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# La función formkeys crea un diccionario nuevo con las claves que se definan en los parámetros
my_new_dict = my_other_dict.fromkeys(("Nombre",1,"Piso"))
print(my_new_dict)

my_list = ["Nombre",1,"Piso"]

# Variantes de uso de fromkeys para creación de un diccionario a partir de una lista en variable y una lista definida en código
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre",1,"Piso"))
print((my_new_dict))

# Sintaxis para crear un nuevo diccionario basado en otro diccionario como parámetro
# La estructura de claves es tomada del parámetro para la creación del nuevo diccionario. Los valores quedan vacios (None)
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

# Prueba de sobrecarga de fromkeys. El segundo valor es para pasar un valor que se aplicará a todas las claves del nuevo diccionario
my_new_dict = dict.fromkeys(my_dict, ("BackEnd"))
print((my_new_dict))

# Esto genera un elemento de tipo de dato 'dict-values'
my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))