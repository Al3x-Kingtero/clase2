#CONCEPTOS BASICOS DE PROGRAMACION

#1. FUNCIONES SON CIUDADANOS DE PRIMER ORDEN
def suma(a,b):
        return a+b

def resta(a,b):
        return a-b

def multi(a,b):
        return a*b
def div(a,b):
    if b != 0:
         return a/b
    
val1 = int(input("ingrese valor 1"))
val2 = int(input("ingrese valor 2"))
op = int(input("ingrese la operacion: 1. suma 2. resta 3. multip. 4 div."))

if op == 1:
    operacion = suma
elif op == 2:
      operacion = resta
elif op == 3:
      operacion = multi
elif op == 4:
      operacion = div
else:
    print("operacion no valida")

print(f"El resultado es:{operacion(val1, val2)}")

# x = suma
# y = suma

# print(x(5,3))
# print(y(6,8))

# Ejemplo: una calculadora

#2. FUNCIONES PURAS
#3. FUNCIONES ANONIMAS (LAMBDA)
num = int(input("Ingrese un numero cualquiera:"))
es_par = lambda x: x % 2 == 0
print(f"{num}es par?: {es_par(num)}")
print(es_par(27))
print(f"{num} es par?: {es_par(num)}")

#4. FUNCIONES DE ORDEN SUPERIOR

# 4.a MAP
# Ejemplo sin map:normalizar un conjunto de datos:
ciudades = ["Cali", "medellin", "BOGOTA", "barranquilla"]

#ES UNA FUNCION PURA?
def normalizar_datos(lista_nombres):
      datos_norm = []
      for nombre in lista_nombres:
          datos_norm.append(nombre.capitalize())
        return datos_norm

ciudades_norm = normalizar_datos(ciudades)  
print(f"Datos sin normalizar:{ciudades}")
print(f"Datos normalizados:{ciudades_norm}")

#Ejemplo con una funcion de orden superior: map
#Usando map, sin funcion lambda:
def capitalizar(palabra):
      #retorna la palabra con la inicial en mayuscula
      return palabra.capitalize()

ciudades_norm2 = list(map( capitalizar, ciudades))

ciudades_norm2 = list(map( capitalizar, ciudades))

ciudades_norm = normalizar_datos(ciudades)
print(f"Datos sin normalizar:{ciudades}")
print(f"Datos normalizados:{ciudades_norm}")
print(f"Datos normalizados con map (sin lambda):{ciudades_norm2}")

#usando map,sin funcion lambda:
ciudades_norm3 = list(map (lambda n: n.capitalize() ,ciudades ))
print(f"datos normalizados con map (con lambda):{ciudades_norm3}")




#x = suma
#y = suma
#print (x(5,3))
#print (y(6,8))