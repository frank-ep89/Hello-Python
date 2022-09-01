### Loops ###

# While

from xml.dom.minidom import Element


my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 # Sin una validación de my_condition el bucle sería infinito
else: # Es opcional. Se puede usar else anidado a un while
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        break # Esta función rompe el bucle en la iteración que se ejecuta bajo la condicional del if.
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (33, 1.80, "Francisco", "Palma", "Francisco")

for element in my_tuple:
    print(element)

my_set = {"Francisco", "Palma", 33}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Francisco","Apellido":"Palma","Edad":33, 1:"Python"}

for element in my_dict: # Este for solo imprime los keys.
    print(element)
    if element == "Edad":
        break
# elif element == 1: # La función elif no se puede utilizar con el for.
#    print("element vale 1")
else: # Uso del else con un for.
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict.values(): # Para imprimir los values es necesario definir la estructura con .values()
    print(element)
    if element == "Palma":
        break

for element in my_dict.items(): # Para imprimir el diccionario  es necesario definir la estructura con .items()
    print(element)

    for element in my_dict:
        print(element)
        if element == "Edad":
            continue # Continua la ejecución del for en la siguiente iteración sin ejecutar las líneas que le siguen.
        print("Se ejecuta")
    else:
        print("El bucle for para diccionario ha finalizado")