### Condicionales ###

from operator import truediv


my_condition = False

# El formato del if es definir la condición seguida de :
if my_condition: # Es lo mismo que escribir if my_condition == True
    print("Se ejecuta la condición del if")

# my_condition = 5 * 2
my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else

#if my_condition > 10:
if my_condition > 10 and my_condition < 20:
    # print("Se ejecuta la condición del tercer if")
    # print("Es mayor que 10")
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    # print("Es menor o igual que 10")
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Condicional con inspección de valor

my_string = ""
#my_string = "Mi cadena de texto"

#if my_string:
#    print("Mi cadena de texto no es vacía")

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")