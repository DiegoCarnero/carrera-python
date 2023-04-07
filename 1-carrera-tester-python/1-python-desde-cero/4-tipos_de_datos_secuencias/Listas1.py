# Realizar un programa que inicialice una lista con 10 valores
# aleatorios (del 1 al 10) y posteriormente muestro en pantalla cada
# elemento de la lista junto con su cuadrado

import random

lista = []
for i in range(1, 11):
    lista.append(random.randrange(1, 10))

print(*lista)
