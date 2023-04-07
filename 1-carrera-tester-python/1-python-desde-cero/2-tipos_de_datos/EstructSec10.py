"""
Ejercicio 10
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

 · 55% del promedio de sus tres calificaciones parciales.
 · 30% de la calificación del examen final.
 · 15% de la calificación de un trabajo final.
"""
par1 = float(input("parcial 1: "))
par2 = float(input("parcial 2: "))
par3 = float(input("parcial 3: "))
examen = float(input("examen: "))
trabajo = float(input("trabajo: "))

media = (par1 + par2 + par3) / 3
final = 0.55 * media + 0.3 * examen + 0.15 * trabajo
print("Nota final: {:.3f}".format(final))