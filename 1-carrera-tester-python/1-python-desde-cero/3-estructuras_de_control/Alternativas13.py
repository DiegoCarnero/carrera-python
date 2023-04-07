# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("dia:"))
mes = int(input("mes:"))
anho = int(input("año:"))

if mes in (1,3,5,7,8,10,12):
    max_dias = 31
elif mes == 2:
    # bisiesto?
    max_dias = 29 if (anho % 4 == 0 or anho % 400 == 0) and anho % 100 == 0 else 28
else:
    max_dias = 30

correcto = True
if dia > max_dias or dia < 1:
    correcto = False

print("Fecha correcta?:",correcto)