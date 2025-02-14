from Modulo1 import *


print("hola mundo")
nombre =input("Alex")
edad =int (input("ingrese su edad"))
peso =float (input("ingrese su edad"))

nombre_archivo=input("ingrese nombre de archivo")
lista_datos=cargarDatos(nombre_archivo)

for linea in lista_datos:
    print("\n" + linea)

