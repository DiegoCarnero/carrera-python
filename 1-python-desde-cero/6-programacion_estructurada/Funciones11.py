# Funcion EsBisiesto: Recibe un año y devuelve si es o no EsBisiesto
# Parámetros de entrada: año
# Dato devuelto: Valor lógico indicando si es bisiesto (Verdadero) o no (Falso)

def es_bisiesto(anho):
    return (anho % 4 == 0 or anho % 400 == 0) and anho % 100 == 0

# Función DiasDelMes: Recibe un mes y un año y devuelve el número de díasque tiene
# ese mes en ese año. Necesita la función EsBisiesto
# Parámetros de entrada: mes y año
# Dato devuelto: Días del mes en ese año

def dias_del_mes(mes, anho):
    if mes in (1,3,5,7,8,10,12):
        max_dias = 31
    elif mes == 2:
        # bisiesto?
        max_dias = 29 if es_bisiesto(anho) else 28
    else:
        max_dias = 30

    return max_dias

# Función Calcular_Dia_Juliano: Recibe un día, mes y año y devuelve el día juliano
# correspondiente a esa fecha. El día juliano correspondiente a una fecha es un 
# año indicado. Depende de la función DiasDelMes
# Parámetros de entrada: día, mes y año
# Dato devuelto: Día juliano

def calcular_dia_juliano(dia, mes, anho):
    dia_juliano = 0
    for m in range (1, mes):
        dia_juliano = dia_juliano + dias_del_mes(m,anho)
        dia_juliano = dia_juliano + dia
    return dia_juliano

# Función LeerFecha: Lee por teclado el día, mes y el año y lo devuelve
# como parámetro de entrada / salida
# Datos devueltos: día, mes y año

def leer_fecha():
    dia = int(input("dia: "))
    mes = int(input("mes: "))
    anho = int(input("año: "))
    return dia, mes, anho

# Queremos crear un programa principal que al introducir una fecha nos diga el 
# día juliano que corresponde.

dia, mes, anho = leer_fecha()
print("Juliano:",calcular_dia_juliano(dia, mes, anho))