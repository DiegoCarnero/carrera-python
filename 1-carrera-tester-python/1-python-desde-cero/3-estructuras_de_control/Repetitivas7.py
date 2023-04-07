# Realizar una algoritmo que muestre la tabla de multiplicar de un número 
# introducido por teclado.

num = int(input("Num: "))

for i in range(1,10):
    print("{:2g} x {} = {:2g}".format(i,num,i*num))