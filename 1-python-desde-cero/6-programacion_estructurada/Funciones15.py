# Función LongitudCole: Recibe una lista (cola).
# Devuelve un contador con los elementos de la cola.

def longitud_cola(cola):
    return len(cola)

# Función EstaVaciaCola: Recibe una lista (cola).
# Devuelve un valor lógico indicando si la cola está vacía.

def esta_vacia_cola(cola):
    return len(cola) == 0

# Procedimiento AddCola: Recibe una lista (cola) y un elemento (cadena)
# Parámetrode entrada: La cola y el elemento.
# Valor devuelto: La cola

def add_cola(cola, cadena):
    cola.append(cadena)

# Función SacarCola: Recibe una lista (cola) y devuelve
# el elemento que se ha introducido en primer lugar, si no está vacía.
# Parámetro de entrada: La cola y el elemento.
# Dato devuelto: El elemento

def sacar_cola(cola):
    if esta_vacia_cola(cola):
        print("Cola vacia")
    else: 
        return cola.pop(0)

# Función EscribirCola: Recibe una lista (cola)
# Muestra los elementos de la cola.
# Parámetros de entrada: La cola

def escribir_cola(cola):
    print(*cola)

# Realiza un programa principal que nos permita usar funciones para manipular pilas

cola = []
opcion = 0
while opcion != -1:
    print("1-AddCola")
    print("2-Sacar")
    print("3-Longitud")
    print("4-Escribir")
    print("5-Salir")
    opcion = int(input())

    if opcion == 1:
        e = input("Nuevo elemento: ")
        add_cola(cola,e)
    elif opcion == 2:
        print(sacar_cola(cola))
    elif opcion == 3:
        print(longitud_cola(cola))
    elif opcion == 4:
        escribir_cola(cola)
    elif opcion == 5:
        opcion = -1
    else:
        print("No valido")

    print()
