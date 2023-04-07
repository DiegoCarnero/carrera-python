# Vamos a crear un programa en python donde vamos a declarar un
# diccionario para guardar los precios de las distintas frutas. El
# programa pedirá el nombre de la fruta y la cantidad que se ha
# vendido y nos mostrará el precio final de la fruta a partir de los
# datos guardados en el diccionario. Si la fruta no existe nos dará un
# error. Tras cada consulta el programa nos preguntará si queremos
# hacer otra consulta.

frutas = {"platano": 1, "manzana": 2}

ejec = True

while ejec:
    fruta = input("Nombre fruta: ")

    if fruta in frutas:
        ventas = int(input("Cantidad vendida: "))
        print("Total: ", frutas[fruta] * ventas)
        b = input("Otra?: ")
        ejec = b    # cadena vacia es False
    else:
        raise NameError
