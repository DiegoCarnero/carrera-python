# Realiza un programa que comprueba si una cadena leída por teclado comienza
# por una subcadena introducida por teclado

s1 = input("Cadena: ")
s2 = input("Comienzo: ")

print(s1, "comienza por", s2, "?:", s1.startswith(s2))
