# Pide una cadena y un carácter por teclado (valida que sea un carácter)
# y muestra cuantas veces aparece el carácter en la cadena.

s = input("Cadena: ")
c = input("Caracter: ")
if len(c) == 1:
    print(s.count(c))
