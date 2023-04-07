# Suponiendo que hemos introducido una cadena por teclado que representa una frase
# (palabras separadas por espacios), realiza un programa que cuente cuantas
# palabras tiene

s = input("Frase: ")
s = s.strip()

num_palabras = 0
if len(s) != 0:
    num_palabras = len(s.split(" "))

print("La frase tiene",num_palabras,"palabras")