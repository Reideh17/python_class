"""
  Ejercicios Listas

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-2-2021          Versión inicial del programa
"""

#############################################################################
# Ejercicio 1:
# Dada la Lista de Baraja, muestre en pantalla las siguientes cartas
# empleando indices según correspondan:
#  1. Siete de tréboles
#  2. Rey de corazones
#  3. As de diamantes
#  4. Joker de espadas
#############################################################################

# listaBaraja = [ ["As", "Dos", "Tres", "Cuatro", "Cinco", "Seis",  "Siete", "Ocho", "Nueve", "Diez", "Joker", "Reina", "Rey"], \
#                 ["Corazones ", "Diamantes ", "Tréboles ", "Espadas "] \
#               ]

# print(len(listaBaraja))
# print(listaBaraja)

# listaCaras = ["As", "Dos", "Tres", "Cuatro", "Cinco", "Seis",  "Siete", "Ocho", "Nueve", "Diez", "Joker", "Reina", "Rey"] 
# listaPalos = ["Corazones ", "Diamantes ", "Tréboles ", "Espadas "]
# listaBaraja = [listaCaras,listaPalos ]
# print(len(listaBaraja))

# print(listaBaraja[0][6],"de",listaBaraja[1][2])
# print(listaBaraja[0][12],"de",listaBaraja[1][0])
# print(listaBaraja[0][0],"de",listaBaraja[1][1])
# print(listaBaraja[0][10],"de",listaBaraja[1][3])


# #############################################################################
# # Ejercicio 2:
# # Dada la Lista de Baraja, muestre en pantalla las siguientes cartas
# # empleando indices según correspondan:
# #  1. Joker Diamantes
# #  2. Rey de corazones
# #  3. Reina  de tréboles
# #  4. Reina de Espadas
# #  5. Joker J Diamantes D
# #  6. Reina a  treboles s
# #############################################################################


# listaPalos = ["Corazones", "Diamantes", "Tréboles", "Espadas"]
# listaBaraja = [listaPalos,"Joker ", "Reina ", "Rey "  ]

# print(listaBaraja[1],"de", listaBaraja[0][1])
# print(listaBaraja[3],"de", listaBaraja[0][0])
# print(listaBaraja[2],"de", listaBaraja[0][2])
# print(listaBaraja[2],"de", listaBaraja[0][3])
# print(listaBaraja[1],listaBaraja[1][0],listaBaraja[0][1],listaBaraja[0][1][0])
# print(listaBaraja[2],listaBaraja[2][4],listaBaraja[0][2],listaBaraja[0][2][7])



# #############################################################################
# # Ejercicio 3:
# # Dada la Lista de Baraja, muestre en pantalla las siguientes cartas
# # empleando indices según correspondan, utilizando variables:
# #  1. Siete de tréboles
# #############################################################################
# listaBaraja = [ ["As ", "Dos ", "Tres ", "Cuatro ", "Cinco ", "Seis ",  "Siete ", "Ocho ", "Nueve ", "Diez ", "Joker ", "Reina ", "Rey "], \
#                 ["Corazones ", "Diamantes ", "Tréboles ", "Espadas "] \
#               ]

# print(listaBaraja)

# listaCaras = ["As", "Dos", "Tres", "Cuatro", "Cinco", "Seis",  "Siete", "Ocho", "Nueve", "Diez", "Joker", "Reina", "Rey"] 
# listaPalos = ["Corazones ", "Diamantes ", "Tréboles ", "Espadas "]
# listaBaraja = [listaCaras,listaPalos ]


# cara0 = 0
# cara1 = 6 
# palo0 = 1
# palo1 = 2
# print(listaBaraja[cara0][cara1]," de",listaBaraja[palo0][palo1])



# #######################################################################
# # Ejercicio No 4
# # Proponer una representación con listas para las cartas de una baraja. 
# # Obtener una carta aleatoria
# #######################################################################
# import random

# def seleccionarCarta(numeroPalo:int, numeroCara:int) ->list:
#     caras = ["As ", "Dos ", "Tres ", "Cuatro ", "Cinco ", "Seis ",  "Siete ", "Ocho ", "Nueve ", "Diez ", "Joker ", "Reina ", "Rey "]
#     palos = ["Corazones ", "Diamantes ", "Treboles ", "Espadas "]

#     carta =  [caras[numeroCara],palos [numeroPalo]]
  
#     return carta


# aleatorioCara = random.randint(0, 12)
# aleatorioPalo = random.randint(0, 3)
# carta = seleccionarCarta (aleatorioPalo,aleatorioCara)
# print(carta)




###################################################################################################
# Ejercicio No 6:
# Introducir  una cadena por teclado que representa una frase (palabras separadas por espacios).
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
     


# listaCadena    = cadena.split()
# numeroPalabras = len(listaCadena)

# print ("El número de palabras que contiene la frase :{}  es {}".format(cadena,numeroPalabras))




#####################################################################
# Ejercicio 7:
# Sacar cuatro cartas al azar. Si se obtiene para las cuatro cartas 
# la misma cara sin importar el palo, el jugador gana
#####################################################################


# import random

# def seleccionarCarta(numeroPalo:int, numeroCara:int) ->tuple:
#     caras = ["As ", "Dos ", "Tres ", "Cuatro ", "Cinco ", "Seis ",  "Siete ", "Ocho ", "Nueve ", "Diez ", "Joker ", "Reina ", "Rey "]
#     palos = ["Corazones ", "Diamantes ", "Treboles ", "Espadas "]

#     carta =  [caras[numeroCara],palos [numeroPalo]]
  
#     return carta


# # Se saca para que nos genere 4 veces la misma carta
# # aleatorioCara = random.randint(0, 12)
# # aleatorioPalo = random.randint(0, 3)
  

# listaCartas = []
       
# for lanzada in range(1,5):

#     aleatorioCara = random.randint(0, 12)
#     aleatorioPalo = random.randint(0, 3)

#     cartaAleatoria = seleccionarCarta (aleatorioPalo,aleatorioCara)
#     listaCartas.append(cartaAleatoria)

# print(listaCartas)


# if (listaCartas[0][0] == listaCartas[1][0] ==  listaCartas [2][0] ==  listaCartas[3][0] ):
#     print("Ganador")
# else:
#     print("Inténtalo nuevamente")



# #########################################################
# # Numeros primos
# #########################################################
# # Es un número natural.
# # Es mayor que 1.
# # Son divisibles por sí mismo y por 1.

#############
# Versión 1
#############

# rangoFinal  = 5
# listaPrimos = []
# for numeroActual in range(2,rangoFinal+1):

#     contadorDivisores = 0
#     # ciclo interno para identificar si tiene más de un divisor
#     for divisor in range(2,numeroActual+1):
#         if (numeroActual % divisor == 0):
#            contadorDivisores +=1


#      #  Si no tiene más de un divisor
#     if contadorDivisores <=1 :
#         listaPrimos.append(numeroActual)

# print("Lista de Primos :",listaPrimos )


###############
# #Versión 2
###############

# rangoFinal  = 5
# listaRango = list(range(2,rangoFinal+1))


# listaPrimos = []
# for numeroActual in listaRango:

#     contadorDivisores = 0
#     # ciclo interno para identificar si tiene más de un divisor

#     listaDivisor = list(range(2,numeroActual+1))
#     for divisor in listaDivisor:
#         if (numeroActual % divisor == 0):
#            contadorDivisores +=1


#      #  Si no tiene más de un divisor
#     if contadorDivisores <=1 :
#         listaPrimos.append(numeroActual)

# print("Lista de Primos :",listaPrimos )



