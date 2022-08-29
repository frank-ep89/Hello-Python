### Tuplas ###

my_tuple = tuple() # Definición de la tupla con el constructor.
my_other_tuple = () # Definición de la tupla mediante el elemento que la define ().

# Bloque de instrucción para definir las tuplas y sus elementos.
my_tuple = (33, 1.80, "Francisco", "Palma", "Francisco")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) # IndexError: tuple index out of range
# print(my_tuple[-6]) # IndexError: tuple index out of range


print(my_tuple.count("Francisco")) # Función que retorna la cantidad de ocurrencias del elemento en la tupla.

# Funciones que devuelven el índice de la tupla donde se encuentra la primera instancia del elemento.
print(my_tuple.index("Palma"))
print(my_tuple.index("Francisco"))

# my_tuple[1] = 1.81 # TypeError: 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6]) # Esta instrucción toma los indices 3 para empezar la subtupla y finaliza en el último valor antes de 6.

# Tupla mutable con conversión a lista

# Retipado de my_tuple de tupla a lista.
# Se imprime el nuevo tipo de lista de my_tuple
my_tuple = list(my_tuple)
print(type(my_tuple))

# Bloque de inserción de valores a la lista.
my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Morado")

# Bloque de retipado de my_tuple de lista a tupla.
# Se imprimen los elementos de la tupla y su nuevo tipo para confirmar el cambio de tipo de lista a tupla.
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] # TypeError: 'tuple' object doesn't support item deletion

del my_tuple # Esta instrucción borra la tupla de la memoria.
# print(my_tuple) # NameError: name 'my_tuple' is not defined