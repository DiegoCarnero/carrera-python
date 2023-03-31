# Introducir una cadena de caraceres e indicar si es un palíndromo

s = input("Cadena: ")
s = s.lower()

if s == s[::-1]:
    print("Palíndromo")
else:
    print("No palíndromo")
