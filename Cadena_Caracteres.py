"""
  Cadena de Caracteres
  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Mayo-25-2021          Versión inicial del programa
"""

# #######################################
# #  Acceso a los caracteres de un string
# #######################################

# nombreFruta  = 'naranja'

# primeraLetra = nombreFruta[0]
# print(primeraLetra)

# segundaLetra = nombreFruta[1]
# print(segundaLetra)
# terceraLetra = nombreFruta[2]
# cuartaLetra  = nombreFruta[3]
# quintaLetra  = nombreFruta[4]
# sextaLetra   = nombreFruta[5]
# septimaLetra = nombreFruta[6]

# ###############################################################
# # Acceso a los caracteres de un string de atrás hacia adelante
# ###############################################################

# nombreFruta    = 'naranja'
# ultimaLetra    = nombreFruta[-1]
# print(ultimaLetra)
# penultimaLetra = nombreFruta[-2]
# print(ultimaLetra,penultimaLetra)

# ############################################################################################
# # Índices de las cadenas de caracteres:
# # Se puede usar cualquier expresión, incluyendo variables y operadores, como un índice, 
# # pero el valor del índice tiene que ser un número entero 
# # ########################################################################################## 

# # nombreFruta = 'naranja'
# # primeraLetra = nombreFruta[1.5]


# nombreFruta         = 'naranja'

# longitudNombreFruta = len(nombreFruta)
# print(longitudNombreFruta)

# primeraLetra = nombreFruta[longitudNombreFruta -7]
# print(primeraLetra)

# segundaLetra = nombreFruta[longitudNombreFruta -6]
# terceraLetra = nombreFruta[longitudNombreFruta -5]
# cuartaLetra  = nombreFruta[longitudNombreFruta -4]
# quintaLetra  = nombreFruta[longitudNombreFruta -3]
# sextaLetra   = nombreFruta[longitudNombreFruta -2]
# septimaLetra = nombreFruta[longitudNombreFruta -1]




# #######################################################################
# # Porciones o rebanadas o slice de un string 
# #######################################################################

#nombreFruta = 'naranja'

# tresLetras     = nombreFruta[0:3]
# print(tresLetras)

# tresLetras     = nombreFruta[2:5]
# print(tresLetras)

# porcionFinal  = nombreFruta[4:]
# print(porcionFinal)

# porcionInicial= nombreFruta[:2]
# print(porcionInicial)

# porcion = nombreFruta[-1:-3]  # No funciona
# print(porcion)

# porcion = nombreFruta[-3:-1]  # No funciona
# print(porcion)

# ####################################################################################################
# #Si elprimer indice es  mayor al seguno  o los indices son iguales el resultado es una cadena vacia
# # nombreFruta = 'naranja'
# ####################################################################################################

# primerIndiceMayor = nombreFruta[1:1]
# primerIndiceMayor = nombreFruta[2:1]

# ##############################################
# # Sin indices el resultado es toda la cadena
# ##############################################
# nombreFruta = 'naranja'
# queResulta  = nombreFruta[:]
# print(queResulta)

# ###############################
# # Las cadenas son inmutables
# ###############################
# nombreFruta    = 'naranja'
# nombreFruta[0] = 'P'         # Genera error


# # Pero  si puedo hacer
# nombreFruta = "naranja"
# refresco    = nombreFruta[:] + "da"
# print(refresco)


# #################################################################
# # Identificar un  caracter o cadena de caracteres en una cadena
# #################################################################
# nombreFruta="naranja"

# if "ran" in nombreFruta:
#      print ("naranja incluye los caracteres ran")


# nombreFruta= "naranja"
# if not ( "ran" in nombreFruta):
#    print ("No imprima nada")
# else:
#    print ("naranja incluye los caracteres ran")

# nombreFruta= "naranja"
# if  "ran" not in nombreFruta:
#    print ("No imprima nada")
# else:
#    print ("naranja incluye los caracteres ran")


# ##################################
# # comparación de caracteres:
# ##################################

# nombreFrutaRoja  = "fresa"
# nombreFrutaVerde = "limon"
# nombreFrutaAcida = "limon"

# if (nombreFrutaRoja == nombreFrutaVerde):
#     print(" Las frutas son iguales")
# else:
#     print(" Las frutas son diferentes")


# if (nombreFrutaAcida == nombreFrutaVerde):
#     print(" Las frutas son iguales")
# else:
#     print(" Las frutas son diferentes")

# ############################################
# # procedimientos: variable.procedimiento()
# ############################################
# nombreFruta          = 'banana'
# nombreFrutaMayuscula = nombreFruta.upper()                         
# print(nombreFrutaMayuscula)


# #########################################################
# # Probar si un caracter es número o letra o alfanúmerico
# #########################################################

# cadena = "1"
# if cadena.isnumeric():
#    print("es número") 

# cadena = "abc"
# if cadena.isalpha():
#    print("es cadena") 


# cadena = "123abc"
# if cadena.isalnum():
#    print("es cadena alfanumérica") 

####################################
# Dividir una cadena por un caracter
####################################
# correo = "correo@usa.edu.co"
# nombre, dominio = correo.split("@")
# print(nombre)
# print(dominio)



# ####################################################
# # Identificar los métodos según el tipo de dato
# ####################################################
# nombreFrutaRoja = "fresa"
# print(dir(nombreFrutaRoja))


# #########################
# # Otras operaciones 
# #########################

# cadena = 'python ' * 4
# print(cadena)

# cadena = 'python'
# cadena = cadena + ' versión 3.9.5'
# cadena += ' versión 3.9.5'
# print(cadena)


# #######################################
# # Formato de una cadena de caracteres
# #######################################

# nombreFruta = "sandia"
# calorias = 20
# print(" La {} es una fruta tropical y tiene {} calorias".format(nombreFruta,calorias))


# nombreFruta = "sandia"
# calorias = 20.88
# print(" La {} es una fruta tropical y tiene {:.1f} calorias".format(nombreFruta,calorias))


# nombreFruta = "sandia"
# calorias = 20.88
# print(" La {0} es una fruta tropical y tiene {1:.1f} calorias".format(nombreFruta,calorias))
# print(" La {nombreFruta} es una fruta tropical y tiene {calorias:.1f} calorias".format(nombreFruta="sandia",calorias=20.88))


# print(" La {nombreFruta} es una fruta tropical y tiene {calorias:+} calorias".format(nombreFruta="sandia",calorias=20.88))

# nombreFruta = "sandia"
# calorias = 20.88
# print(f' La {nombreFruta} es una fruta tropical y tiene {calorias} calorias ')


#############################################
# Ciclo repetitivo con cadena de caracteres
#############################################

# nombreFruta = "sandia"

# for caracterFruta in nombreFruta:
#   print(caracterFruta,end=" ")



#############################################
# Otros Metodos con cadena de caracteres
############################################

######################################################################
#capitalize() - Convierte la primera letra de la cadena en mayusculas
######################################################################
# nombreFruta = "sandia"

# mayuscula = nombreFruta.capitalize()
# print(mayuscula)


####################################################################
# title() - Convierte la primera letra de cada palabra en  mayúscula
###################################################################
# nombreFruta = " sandia , pera, mora"
# mayuscula = nombreFruta.title()
# print(mayuscula)


####################################################################
# swapcase() - Convierte mayúsculas en minúsculas y viceversa
###################################################################

# nombreFruta = " Sandia , Pera, Mora"
# mayuscula = nombreFruta.swapcase()
# print(mayuscula)



#####################################################################
# casefold - Retorna un string con todos los caracteres en minúscula
#####################################################################

# nombreFruta = " Sandia , Pera, Mora"
# minuscula = nombreFruta.casefold()
# print(minuscula)

#####################################################################
# find - Encuentra la ocurrencia de un valor especificado
#        Retorna -1 si el valor no fue encontrado
#        Retorna la posición si fue encontrado
#####################################################################

# nombreFruta = " Sandia , Pera, Mora"
# posicion = nombreFruta.find("Pera")
# print(posicion)


# nombreFruta = " Sandia , Pera, Mora"
# posicion = nombreFruta.find("Pera",11,17) # Busca en el rango de posiciones.
# print(posicion)



########################################################################
# index  - Encuentra la ocurrencia de un valor especificado
#          Retorna la posición si fue encontrado. Sino lanza excepción
########################################################################

# nombreFruta = " Sandia , Pera, Mora"
# posicion = nombreFruta.index("Pera")
# print(posicion)


# nombreFruta = " Sandia , Pera, Mora"
# posicion = nombreFruta.index("Pera",10,15) # Busca en el rango de posiciones.
# print(posicion)


# nombreFruta = " Sandia , Pera, Mora"
# posicion = nombreFruta.index("Pera",20) # Busca apartir de la posicion. Marca error
# print(posicion)




################################################
# replace() - Remplaza unos caracteres por otros
################################################
# nombreFruta = " Sandia , Pera, Mora"
# cambio = nombreFruta.replace("Pera", "mango") #remplaza Pera por mango
# print(cambio)


# nombreFruta = " Sandia , Pera, Mora"
# cambio = nombreFruta.replace("pera", "mango") #Si no encuentra devuelve la misma cadena.
# print(cambio)

# nombreFruta = " Sandia , Pera, Mora , Pera, Pera"
# cambio  = nombreFruta.replace("Pera", "mango", 2) # Remplaza las dos primeras ocurrencias
# print(cambio)


######################################################################
# strip() - Remueve los espacios al principio y al final de la cadena
######################################################################

# nombreFruta = "  Sandia , Pera, Mora , Pera, Pera  "
# sinEspacios = nombreFruta.strip()
# print(sinEspacios)

######################################################################
# strip() - Remueve los caracteres especificados
######################################################################

# nombreFruta = ",,,,,rrttggmmmm.....banana....rrr"
# sinCaracteres = nombreFruta.strip(",.grtm") # remueve los caracteres indicados.
# print(sinCaracteres)