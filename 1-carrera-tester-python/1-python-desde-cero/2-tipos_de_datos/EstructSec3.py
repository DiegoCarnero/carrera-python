# Ejercicio 3
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
cateto1=float(input("Cateto1:"))
cateto2=float(input("Cateto2:"))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print("hipotenusa = %.2f" % hipotenusa)