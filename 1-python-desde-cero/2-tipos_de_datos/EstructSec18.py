# Ejercicio 18
# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre = input("Nombre: ")
apellido = input("Apellido: ")

print("{}.{}.".format(nombre[0].upper(),apellido[0].upper()))