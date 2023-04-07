"""
Ejercicio 15
Dadas dos variables numéricas A y B, que el usuario debe teclear, 
se pide realizar un algoritmo que intercambie los valores de ambas variables 
y muestre cuanto valen al final las dos variables.
"""
var1 = input("var1: ")
var2 = input("var2: ")
aux = var1
var1 = var2
var2 = aux
print(var1,var2)