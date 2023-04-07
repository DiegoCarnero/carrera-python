# Escribe un programa que lea una cadena y devuelva un diccionario con
# la cantidad de apariciones de cada carácter en la cadena.

dicc = {}

c = input("Cadena: ")

for i in range(0, len(c)):
    char = c[i]
    dicc[char] = c.count(char)

d = dict(sorted(dicc.items))

for k, v in d.items():
    print(k, v)
