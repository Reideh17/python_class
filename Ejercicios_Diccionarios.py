"""
  Ejercicios Diccionarios

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-2-2021          Versión inicial del programa
"""


#############################################################################
#  Ejercicio 0:
#  Dado el diccionario de alimentos, muestre en pantalla:
#  0. El número de elementos que tiene el diccionario
#  1. Los tipos de alimentos que hay: frutas,verduras y cereales
#  2. Los tipos de frutas : manzanas, uvas 
#  3. Los tipos de papa : negras, blancas
#  4. Cuantas uvas verdes hay? : 3 
# 
#############################################################################


alimentos = { 'frutas'    : {' manzanas': [' verdes', ' 7', ' rojas', ' 5'],'uvas': [' negras', ' 5', ' verdes', ' 3']},
              'verduras'  : {'papa': ['negras', ' 50', ' blancas', ' 20'],'cebolla': [' blancas', ' 30']},
              'cereales'  : {' arroz': [' fino',' 600', ' largo', ' 800']}
            } 

#################################################
# 0. Número de elementos que tiene el diccionario
#################################################
# print(len(alimentos))
# print(type(alimentos))

###################################################################
# #  1. Los tipos de alimentos que hay: frutas,verduras y cereales
###################################################################

# print(type(alimentos.keys()))
# print("Los tipos de alimentos son : ",alimentos.keys())

# lista = list(alimentos.keys())
# print("Los tipos de alimentos son : ",lista)

# for tipoAlimento in lista:
#    print(tipoAlimento,end=" ")



#############################################
#  2. Los tipos de frutas : manzanas, uvas 
#############################################

# #Obtener los valores del diccionario
# print(alimentos.values())

# #Obtener una lista del diccionario
# lista = list(alimentos.values())
# print(lista)
# print(len(lista))



# #Obtener las llaves del primer elemento de la lista

# listaLLaves = lista[0].keys()

# for frutas in listaLLaves:
#     print(frutas,end=" ")


###########################################
#  3. Los tipos de papa : negras, blancas
###########################################
# Obtener lista de los values
# lista = list(alimentos.values())
# print(lista)
# print(len(lista))

# valores = lista[1].values()
# print(valores)
# print(type(valores))

# listaValores = list(valores)
# print(listaValores)
# print(listaValores[0][0], listaValores[0][2])


# listaPapas = list(listaValores)
# print(listaPapas)





##########################################################################################
# Ejercicio 1:
#Escriba una función en python que pida un número entero positivo y que cree un
#diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores
#sean los cuadrados de las claves
##########################################################################################

# def seleccionarNumero(numeroEntero:int) ->dict:
#     diccionarioSalida={ }
#     for iterador in range(1,numeroEntero+1):
#         diccionarioSalida[iterador] = iterador*iterador
#     return diccionarioSalida

# numeroEntero = int(input("Ingrese un numero Entero: "))
# print(seleccionarNumero(numeroEntero))


# #######################################################################################
# Ejercicio 2
# Escribe una función que reciba como parámetro una cadena y devuelva un diccionario con
# la cantidad de apariciones de cada carácter en la cadena.
#########################################################################################

# def contadorCaracteres(cadena:str) ->dict:
#     diccionarioCaracteres={ }

#     for caracter in cadena:
#         diccionarioCaracteres.setdefault(caracter)

#     for  letra in diccionarioCaracteres.keys():
#          numeroCaracteres = cadena.count(letra)
#          diccionarioCaracteres.update({letra : numeroCaracteres})
         

#     return diccionarioCaracteres


# cadena = input("Ingrese una cadena: ")
# print(contadorCaracteres(cadena))



# #####################################################################################################
# Ejercicio 3
# Crear un programa en python donde se va a declarar un diccionario para guardar el nombre precio 
# unitario, cantidad, valor total de distintas frutas. El programa pedirá el nombre de la fruta, 
# el precio unitario  y la cantidad que se ha vendido e irá creando una cesta de frutas que visualizará
# por pantalla
# Tras cada consulta el programa nos preguntará si queremos ingresara otra fruta a la cesta.
#########################################################################################################
#############
# Versión 1
#############

# cestaFrutas = {}


# controladorCiclo= True
# while controladorCiclo:
#         nombreFruta   = input("Ingrese el nombre de la Fruta: ")
#         precioFruta   = input("Ingrese el precio de la Fruta: ")
#         cantidadFruta = input("Ingrese la cantidad de Fruta vendida: ")

#         if nombreFruta.isalpha() and precioFruta.isnumeric() and cantidadFruta.isnumeric():
#            precioFruta   = float(precioFruta)
#            cantidadFruta = int(cantidadFruta)
           
         
#            tupla = ("precio","cantidad")

#            frutasPrecioCantidad = dict.fromkeys(tupla) # Crea valores None si no se define valor 
#            frutasPrecioCantidad["precio"]   = precioFruta
#            frutasPrecioCantidad["cantidad"] = cantidadFruta
#            frutasPrecioCantidad["total"]    = cantidadFruta * precioFruta

#            cestaFrutas.setdefault(nombreFruta,frutasPrecioCantidad)
#            print(cestaFrutas)

#            respuesta   = input("¿Desea ingresar otra fruta? (s)b: ")

#            if (respuesta.isalpha() and respuesta =="s"):
#               None
#            else:
#             controladorCiclo = False
           
         
#         else:
#             print ("Digite Valores correcores")
#             controladorCiclo = True


##################################################
# Versión 2  - Diccionario con precios diferentes
#################################################

# cestaFrutas = {1 : ["mango",1000.0, 10], 2 : ["mora",9200.0, 20], 3 : ["pera",900.0,8]}


# controladorCiclo= True
# while controladorCiclo:
#         nombreFruta   = input("Ingrese el nombre de la Fruta: ")
#         precioFruta   = input("Ingrese el precio de la Fruta: ")
#         cantidadFruta = input("Ingrese la cantidad de Fruta vendida: ")

#         if nombreFruta.isalpha() and precioFruta.isnumeric() and cantidadFruta.isnumeric():
#            precioFruta   = float(precioFruta)
#            cantidadFruta = int(cantidadFruta)
#            listaFruta    = [nombreFruta,precioFruta,cantidadFruta]         
#            cestaFrutas.setdefault(len(cestaFrutas)+1,listaFruta)
#            print(cestaFrutas)

#            respuesta   = input("¿Desea ingresar otra fruta? (s)b: ")

#            if (respuesta.isalpha() and respuesta =="s"):
#               None
#            else:
#             controladorCiclo = False
           
         
#         else:
#             print ("Digite Valores correcores")
#             controladorCiclo = True



# listaCestaFrutas = list(cestaFrutas.values())
# listaCestaFrutas.sort(key=lambda x :x[1])

# print(f"El producto(s) con menor  precio  es {listaCestaFrutas[0][0]} ")
# print(f"El producto(s) con mayor precio  es {listaCestaFrutas[-1][0]} ")

# sumaPrecio      = 0
# sumaInventario  = 0
# for producto in listaCestaFrutas:
#     sumaPrecio     += producto[1]
#     sumaInventario += producto[1] * producto[2]

# print(f"El promedio de  precios  es {sumaPrecio/len(listaCestaFrutas)} ")
# print(f"El valor del inventario  es {sumaInventario} ")



##################################################
# Versión 3  - Diccionario con precios iguales 
##################################################


#cestaFrutas = {1 : ["mango",1000.0, 10], 2 : ["mora",1200.0, 20], 3 : ["pera",2000.0,8], 4 : ["agraz",2000,9], 5: ["naranja",1000.0,8]}


# controladorCiclo= True
# while controladorCiclo:
#         nombreFruta   = input("Ingrese el nombre de la Fruta: ")
#         precioFruta   = input("Ingrese el precio de la Fruta: ")
#         cantidadFruta = input("Ingrese la cantidad de Fruta vendida: ")

#         if nombreFruta.isalpha() and precioFruta.isnumeric() and cantidadFruta.isnumeric():
#            precioFruta   = float(precioFruta)
#            cantidadFruta = int(cantidadFruta)
#            listaFruta    = [nombreFruta,precioFruta,cantidadFruta]         
#            cestaFrutas.setdefault(len(cestaFrutas)+1,listaFruta)
#            print(cestaFrutas)

#            respuesta   = input("¿Desea ingresar otra fruta? (s)b: ")

#            if (respuesta.isalpha() and respuesta =="s"):
#               None
#            else:
#             controladorCiclo = False
           
         
#         else:
#             print ("Digite Valores correcores")
#             controladorCiclo = True



# listaCestaFrutas = list(cestaFrutas.values())
# listaCestaFrutas.sort(key=lambda x :x[1])

# listaMenorPrecio = []
# listaMayorPrecio = []

# numeroMenor = listaCestaFrutas[0][1]
# numeroMayor = listaCestaFrutas[-1][1]
# for menor in listaCestaFrutas:
#     print(menor)
#     if menor[1] == numeroMenor:
#         listaMenorPrecio.append(menor[0]) 
#     elif menor[1] == numeroMayor:
#         listaMayorPrecio.append(menor[0])

# print(f"El producto(s) con mayor  precio  es {listaMayorPrecio} ")
# print(f"El producto(s) con menor  precio  es {listaMenorPrecio} ")

# sumaPrecio      = 0
# sumaInventario  = 0
# for producto in listaCestaFrutas:
#     sumaPrecio     += producto[1]
#     sumaInventario += producto[1] * producto[2]

# print(f"El promedio de  precios  es {sumaPrecio/len(listaCestaFrutas)} ")
# print(f"El valor del inventario  es {sumaInventario} ")
