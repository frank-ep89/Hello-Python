### Operadores Aritméricos ###

# Operaciones con enteros.
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 //4)

print("Hola " + "Python " + "¿Qué tal?")
print("Hola" + str(5))

# Python no logra aplicar operaciones - / a tipos de dato str o combinados.
#print("Hola" - "Python") # TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print("Hola" + 5) # TypeError: can only concatenate str (not "int") to str

# Operación de texto multiplicado por un valor entero
print("Hola " * 5) # Hola Hola Hola Hola Hola 

print("Hola " * (2 ** 3))

#print("Hola " * 2.5) # TypeError: can't multiply sequence by non-int of type 'float'
#print("Hola " * 2.5 * 2) # TypeError: can't multiply sequence by non-int of type 'float'

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python") # Compara
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print("AAAA" >= "aaaa") # Ordenación alfabética por ASCII
print("aaaa" >= "AAAA") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python") # Comparaciones lógicas según la lógica booleana.
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 ==4))
print(not(3 > 4))