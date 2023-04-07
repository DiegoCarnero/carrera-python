# Realiza un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.

s1 = input("Cadena: ")
s2 = input("Subcadena: ")

print(s1,"contiene",s2,"?:",s1.__contains__(s2))