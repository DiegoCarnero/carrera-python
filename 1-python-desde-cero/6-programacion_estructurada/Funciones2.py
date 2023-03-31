# Funcion EsMultiplo: Recibe dos número e indica si el primero el múltiplo del
# segundo. Para ello calculo el resto de la división, si es 0 es múltiplo.
# Parámetros de entrada: dos números
# Dato devuelto: múltiplo: Valor lógico verdadero si el primero es múltiplo
# del segundo, Falso en caso contrario

def es_multiplo(num1, num2):
    return num1 % num2 == 0

x = 25
y = 5
print(x,"es multiplo de",y,end="")
print("?: ",es_multiplo(x, y))