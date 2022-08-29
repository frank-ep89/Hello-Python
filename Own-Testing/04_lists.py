### Listas ###

my_list = list() # Definición de la lista con el constructor.
my_other_list = [] # Definición de la lista mediante el elemento que la define [].

print(len(my_list)) # Se puede usar la función len para contar cuántos elementos tiene la lista.

my_list = [33, 24, 62, 52, 30, 30, 17] # Instrucción para definir la lista y sus elementos.

print(my_list)
print(len(my_list)) # Función que retorna el conteo total de los elementos en la lista dada como parámetro.

my_other_list = [33, 1.80, "Francisco", "Palma"] # La lista permite diferentes tipos de datos.

print(type(my_list)) # Mismo tipo de dato que my_other_list sin importar la forma en que se instancia.
print(type(my_other_list)) # Tipo de dato es lista.

# Acceso a elementos y búsqueda

print(my_other_list[0]) # Sintaxis para acceso al primer elemento de la lista.
print(my_other_list[-1]) # Sintaxis para acceso al primer elemento de la lista (de derecha a izquierda).
print(my_other_list[1]) # Sintaxis para acceso al segundo elemento de la lista.
print(my_other_list[-3]) # Sintaxis para acceso al tercer elemento de la lista (de derecha a izquierda).
print(my_other_list[-4]) # Sintaxis para acceso al cuarto elemento de la lista (de derecha a izquierda).
print(my_list.count(30)) # Función count requiere de un argumento para buscar la cantidad de instancias del parámetro en la lista.
#print(my_other_list[4]) # IndexError: list index out of range
#print(my_other_list[-5]) # IndexError: list index out of range

# Estructura para declarar variables con los valores contenidos en la lista.
# La forma de desempaquetar tiene que tener la misma cantidad de variables contra el total de elementos de la lista.
age, height, name, surname = my_other_list 
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # Estructura para definir valores según las posiciones de la lista.
print(age)

print(my_list + my_other_list) # Python acepta concatenación de listas con el + 
# print(my_list - my_other_list) # TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print(my_list * my_other_list) # TypeError: can't multiply sequence by non-int of type 'list'


# Creación, inserción, actualización y eliminación\

my_other_list.append("MoureDev") # Esta operación agrega el elemento dado como parámetro al final de la lista.
print(my_other_list)

my_other_list.insert(1, "Morado") # Esta operación agrega el elemento dado en la posición brindada.
print(my_other_list)

my_other_list.remove("Morado") # Esta operación borra el elemento dado de la lista.
print(my_other_list)

my_list.remove(30) # La operación borra la primera instancia del elemento en la lista.
print(my_list)

my_list.pop() # Esta operación elimina el último elemento de la lista.
print(my_list)

print(my_list.pop()) # Esta operación imprime el valor del elemento de la lista que fue removido.
print(my_list)

my_pop_element = my_list.pop(2) # Función que asigna el valor del elemento que el pop remueve de la lista a una variable.
print(my_pop_element)
print(my_list)

del my_list[2] # Esta operación elimina el elemento en el índice 2.
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy() # Esta función copia los elementos de my_list a my_new_list.

my_list.clear() # Esta función borra todos los elementos de la lista.
print(my_list)
print(my_new_list)

my_new_list.reverse() # Esta función revierte el orden de los elementos de la lista.
print(my_new_list)

my_new_list.sort() # Esta función ordena los elementos de la lista de forma ascendente.
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Espacio para ver el tipado dinámico de Python/Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))