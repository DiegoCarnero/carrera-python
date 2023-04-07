# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for i in range(1,6):
    for j in range(1,10):
        print("{:2g} x {} = {:2g}".format(i,j,i*j))
    print()