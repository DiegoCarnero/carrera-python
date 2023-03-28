# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
# y la media de todos los números introducidos.

suma = 0
cont = 0

while True:
    num = int(input("Num: "))
    if num == 0:
        break
    else:
        suma += num
        cont += 1
    

print("Suma: {}".format(suma))
if suma != 0:
    print("Media: {:.2f}".format(suma / cont))
