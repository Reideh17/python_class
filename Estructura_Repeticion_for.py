"""
  Estructuras de Repetición : For
  Autor :  Formador

  Creación/ Actualización  Observaciones
     Junio-3-2021          Versión inicial del programa
"""


##########################################
#  Esquema general de la estructura for
##########################################
#
# for  <element> in <iterable>:
#     cuerpo del bucle


##################################################
# Ejercicio 1: Imprimir los números del 1 al 10
##################################################


# # Con for
# for paleta in range(1,11):
#     print(paleta,end=" ")


# # Con while

# paleta = 1
# while (paleta <11):
#     print(paleta,end=" ")
#     paleta +=1


#####################################################
# Ejercicio 2: Imprima los números impares de 1 a 10
#####################################################

# for numerosImpares in range(1, 11, 2):
#     print(numerosImpares,end=" ")



#####################################################
# Ejercicio 3: Imprima los números impares de 11 al 1
#####################################################

# for numerosImpares in range(11, 0, -2):
#    print(numerosImpares,end=" ")


###############################################################################
# Ejercicio 4: Imprima los números  según un rango dado por el usuario
###############################################################################
# rangoInicial = 30
# rangoFinal   = 40 

# for numerosImpares in range(rangoInicial, rangoFinal+1):
#     print(numerosImpares,end=" ")




########################################################################
# Ejercicio 5: Muestre la tabla de Multiplicar de 1 ( 10 primeras filas) 
#########################################################################


# for lineaTabla  in range(1,11):
#     producto = 1 * lineaTabla
#     print("1 x {} = {}".format(lineaTabla,producto)) 



#########################################################################################################
# Ejercicio 6:  -  Muestre la tabla de Multiplicar que especifique el usuario (10 primeras filas)
#########################################################################################################

# tabla = int(input("Cual tabla de multiplicar desea: "))
# for lineaTabla in range(1,11):
#     producto = lineaTabla * tabla
#     print("{} x {} = {}".format(tabla,lineaTabla,producto)) 


############################################################
# Ejercicio 7  - Muestre las tablas de Multiplicar según rango 
#############################################################

# tablainicial = int(input("tabla inicial : "))
# tablafinal   = int(input("tabla final : "))

# while (tablafinal < tablainicial ):
#   print("La tabla final no puede contener un numero mayor a la incial1")
#   tablafinal   = int(input("tabla final : "))

# for tabla  in range (tablainicial,tablafinal+1):
#     for lineatabla in range(1,11):
#           producto = lineatabla * tabla
#           print("{} x {} = {}".format(tabla,lineatabla,producto)) 
      
#     print("\n")

#######################################################################
# Ejercicio No 9 :
# Liste los números primos hasta el rango que un usuario nos defina
# Un número primo es:
#   Es un número natural.
#   Es mayor que 1.
#   Son divisibles por sí mismo y por 1.
#######################################################################

rangoFinal = int(input(" Hasta que número quiere imprimir los números primos : "))

 #ciclo externo para identificar hasta que número de primos quiero imprimir
for numeroActual in range(2,rangoFinal+1):

      contadorDivisores = 0

      # ciclo interno para identificar el número de dvisores 
      for divisor in range(2,numeroActual+1):
         if (numeroActual % divisor == 0):
            contadorDivisores +=1
    
      # Si solo encontro que es divisible por si mismo
      if contadorDivisores <=1 :
         print(numeroActual)





