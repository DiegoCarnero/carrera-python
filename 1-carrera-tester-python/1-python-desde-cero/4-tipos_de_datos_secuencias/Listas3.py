# Se quiere realizar un programa que lea por teclado las 5 notas
# obtenidas por un alumno (comprendidas entre 0 y 10). A continuación
# debe mostrar todas las notas, la nota media, la nota más alta que has
# sacado y la menor

notas = []

for i in range(1, 6):
    err = True
    while err:
        nota = int(input("Nota nº%d: " % i))
        if nota > 0 and nota <= 10:
            notas.append(nota)
            err = False
        else:
            print("Nota no valida", end=' ')

print("Notas: ", *notas)
print("Media:", sum(notas)/5)
print("Max:", max(notas))
print("Min:", min(notas))
