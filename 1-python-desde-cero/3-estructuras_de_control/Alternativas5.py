# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

nom = input("Nombre de usuario: ")
psswrd = input("Contraseña: ")

if nom == "pepe" and psswrd == "asdasd":
    print("Has entrado al sistema")
else:
    print("Nada")