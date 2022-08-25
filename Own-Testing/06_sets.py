### Sets ###

# Declaración de un set por medio del constructor y directamente con las llaves
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Francisco", "Palma", 33}

print(type(my_other_set)) # Ahora el tipo de datos es un set

print(len(my_other_set))

my_other_set.add("Backend")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Backend") # Un set no admite repetidos

print(my_other_set)

print("Francisco" in my_other_set)
print("Francisc" in my_other_set)

my_other_set.remove("Francisco")
print(my_other_set)

my_other_set.clear()

print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Francisco", "Palma", 33}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)

print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))
