# Diseñar el algoritmo correspondiente a un programa, que:
#
# * Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# * Carga la tabla con valores numéricos enteros.
# * Suma todos los elementos de cada fila y todos los elementos de
#   cada columna visualizando los resultados en pantalla

tabla = []

for ndx_fila in range(1, 6):
    fila = []
    for ndx_col in range(1, 6):
        fila.append(int(input("%dx%d: " % (ndx_fila, ndx_col))))
    tabla.append(fila)

cont = 1
for f in tabla:
    print("suma fila %d = %d" % (cont, sum(f)))
    cont += 1
