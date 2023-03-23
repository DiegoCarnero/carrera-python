# Ejercicio 17
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.
horas = 12
minutos = 30
segundos = 20
tiempo_viaje = 5000

hora_salida_secs = horas * 3600 + minutos * 60 + segundos
hora_final_secs = hora_salida_secs + tiempo_viaje

horas_final = hora_final_secs // 3600 # como castear a int
minutos_final = divmod(hora_final_secs,3600)[1] // 60
segundos_final = divmod(divmod(hora_final_secs,3600)[1], 60)[1]
print("Llega a las {}:{}:{}".format(horas_final,minutos_final,segundos_final))