"""
  Ejercicios Cadena de Caracteres
  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Mayo-25-2021          Versión inicial del programa
"""

#####################################################################
# Ejercicio No 1:
# Realizar un programa que comprueba si una cadena leída por teclado
# comienza por una subcadena introducida por teclado.
#####################################################################

# cadena        = input ("Digite una cadena :")
# inicioCadena  = input ("Digite inicio de cadena a validar :")

# if cadena.startswith(inicioCadena):
#    print("La cadena inicia con la subcadena", inicioCadena)
# else:
#    print("La cadena no inicia con la subcadena", inicioCadena)



###################################################################################################
#  Ejercicio No 2:
#  Pide una cadena y un solo carácter por teclado (valida que sea un carácter  y solo un caracter) y
#  muestra cuantas veces aparece el carácter en la cadena
#  isalpha():  Devuelve  “True”  is todos los caracteres en la cadena contienen letras del alfabeto
# 
###################################################################################################

# cadena        = input ("Digite una cadena : ")

# esCaracter = True
# while (esCaracter):    
#     caracter      = input ("Digite un caracter : ")

#     if caracter.isalpha():
#         if len(caracter) > 1:
#             print ("Debe digitar un solo caracter")        
#         else:
#             esCaracter =False
    
# numeroCaracteres = cadena.count(caracter)

# print(" El caracter {} aparece en la cadena {} : {} veces ".format(caracter,cadena,numeroCaracteres))


###################################################################################################
# Ejercicio No 3:
# Introducir  una cadena por teclado que representa una frase (palabras separadas por un espacio).
# Realiza un programa que cuente cuantas palabras tiene. 
# La cadena no debe contener números,ni caracteres especiales
###################################################################################################

# cadenaCorrecta = True
# while cadenaCorrecta:
#      cadena = input ("Digite una cadena : ")
     
#      esCaracter = True
#      for elemento in cadena:
#          if not(elemento.isalpha() or elemento.isspace()):
#              esCaracter = False

#      if esCaracter == True:
#          cadenaCorrecta = False
#      else:
#          print("La cadena debe contener solo caracteres alfabéticos y separar las palabras con espacio")
     


# cadenaSinEspacios = cadena.strip()
# numeroEspacios    = cadenaSinEspacios.count(" ")
# numeroPalabras    = numeroEspacios +1

# print ("El número de palabras que contiene la frase :{}  es {}".format(cadena,numeroPalabras))



###############################################################################################
# Ejercicio No 4:
# Pide una cadena(valide que solo tenga caracteres alfabéticos o espacios) y 
# dos caracteres por teclado (valida que sea un carácter y solo una caracter).
# Sustituya la aparición del primer carácter en la cadena por el segundo
# carácter.
################################################################################################

# cadenaCorrecta = True
# while (cadenaCorrecta == True): 
#       cadena        = input ("Digite una cadena : ")

#       esCaracter = True
#       for elemento in cadena:
#           if not(elemento.isalpha() or elemento.isspace()):
#               esCaracter = False

#       if esCaracter == True:
#          cadenaCorrecta = False
#       else:
#           print("La cadena solo debe contener caracteres alfabéticos o espacios")
     


# esCaracter = True
# while (esCaracter):    
#       caracterCambiar      = input ("Digite el caracter que desea cambiar : ")
#       caracterRemplazo     = input ("Digite el caracter de remplazo: ")

#       if caracterCambiar.isalpha() and caracterRemplazo.isalpha() :
#          if (len(caracterCambiar) == 1) and (len(caracterRemplazo) == 1):
#             esCaracter = False
#          else:
#              print("Digite únicamente un caracter alfabético ")
#       else:
#           print("Digite únicamente caracteres alfabéticos ")
          

# cadenaModificada = cadena.replace(caracterCambiar,caracterRemplazo)


# print("Cadena Inicial :",cadena)
# print("Cadena Inicial :",cadenaModificada)

