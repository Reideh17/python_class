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

nombrefruta  = 'naranja'

primeraletra = nombrefruta[0]
print(primeraletra)

segundaletra = nombrefruta[1]
print(segundaletra)
terceraletra = nombrefruta[2]
cuartaletra  = nombrefruta[3]
quintaletra  = nombrefruta[4]
sextaletra   = nombrefruta[5]
septimaletra = nombrefruta[6]

# ###############################################################
# # Acceso a los caracteres de un string de atrás hacia adelante
# ###############################################################

# nombreFruta    = 'naranja'
# ultimaLetra    = nombreFruta[-1]
# print(ultimaLetra)
# penultimaLetra = nombreFruta[-2]
# print(ultimaLetra,penultimaLetra)

# ############################################################################################
# # Índices de las cadenas de caracteres:
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

# nombreFruta = 'naranja'

# tresLetras     = nombreFruta[0:3]
# print(tresLetras)

# tresLetras     = nombreFruta[2:5]
# print(tresLetras)

# porcionFinal  = nombreFruta[4:]
# print(porcionFinal)

# porcionInicial= nombreFruta[:2]
# print(porcionInicial)

# ####################################################################################################
# #Si elprimer indice es  mayor al seguno  o los indices son iguales el resultado es una cadena vacia
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


# # Pero  si puedo hacer
# nombreFruta = "naranja"
# refresco    = nombreFruta[:] + "da"
# print(refresco)


# #################################################################
# # Identificar un  caracter o cadena de caracteres en una cadena
# #################################################################
# nombreFruta="naranja"

# if "ran" in nombreFruta:
#      print ("naranja incluye los caracteres ran")


# nombreFruta= "naranja"
# if not ( "ran" in nombreFruta):
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
