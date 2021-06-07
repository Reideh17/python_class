"""
  Estructuras de Repetición
  Autor :  Formador

  Creación/ Actualización  Observaciones
     Mayo-10-2021          Versión inicial del programa
"""

########################################
#  Esquema general de la estructura while
##########################################

# while (condicion):
#       cuerpo del ciclo (instrucciones a repetir)


#################################################################
# Ejercicio 1: Imprima la suma de los números enteros de 1 al 10
#################################################################

# controladorCiclo= 1
# suma = 0

# while (controladorCiclo <= 10):
#       suma = suma + controladorCiclo
#       controladorCiclo += 1

# print("la suma es :",suma)


##################################################################################
# Ejercicio 2:
# Escriba un programa que capture un número entero y que
# compruebe si el número es menor que 10. 
# Si no lo es, debe  volver a capturar el número repitiendo la operación 
# hasta que el usuario escriba un valor correcto. 
# Finalmente, debe escribir por  pantalla el valor leído cuando este sea correcto.
###################################################################################

#Alternativa 1
# controladorCiclo = True
# while (controladorCiclo):
       
#        numeroEntero = input("Digite número entero :")
#        if numeroEntero.isnumeric():
#           numeroEntero = int(numeroEntero)
#           if (numeroEntero < 10):
#              print("Número digitado es correcto: ",numeroEntero)
#              controladorCiclo = False    
#        else:      
#            None
          

#Alternativa 2
# controladorCiclo = True
# while (controladorCiclo):
       
#        numeroEntero = input("Digite número entero :")
#        if numeroEntero.isnumeric():
#           numeroEntero = int(numeroEntero)
#           if (numeroEntero < 10):
#              print("Número digitado es correcto: ",numeroEntero)
#              controladorCiclo = False    

#Alternativa 3
# controladorCiclo = True
# while (controladorCiclo):
     
#        numeroEntero = input("Digite número Entero :")
#        if (numeroEntero.isnumeric()) and (int(numeroEntero) < 10):
#           print("Número digitado es correcto: ",numeroEntero)
#           controladorCiclo = False    


######################################################################
# Ejercicio No 3:
# Modifique el algoritmo del problema anterior para que, en vez de
# comprobar que el número sea menor que 10, compruebe que se
# encuentre en el rango (0, 20) incluyendo el 0 y el 20.
######################################################################

#Alternativa 1
# controladorCiclo = True

# while (controladorCiclo):

#       numeroEntero = input("Digite número entero :")
#       if numeroEntero.isnumeric():
#          numeroEntero = int(numeroEntero)
#          if (numeroEntero >=0) and (numeroEntero <=20): 
#             print("Número digitado es correcto: ",numeroEntero)
#             controladorCiclo = False



#Alternativa 2
# controladorCiclo = True

# while (controladorCiclo):
#       numeroEntero = input("Digite número entero :")
#       if numeroEntero.isnumeric():
#          numeroEntero = int(numeroEntero)
#          if (numeroEntero in range(0, 21)): 
#             print("Número digitado es correcto: ",numeroEntero)
#             controladorCiclo = False

#Alternativa 3
# controladorCiclo = True
# while (controladorCiclo):
     
#         numeroEntero = input("Digite número Entero :")
#         numeroEntero = int(numeroEntero)
#         if (numeroEntero.isnumeric()) and (numeroEntero < 10):
#            print("Número digitado es correcto: ",numeroEntero)
#            controladorCiclo = False    

#Alternativa 4

# controladorCiclo = True
# while (controladorCiclo):
     
#         numeroEntero = input("Digite número Entero :")
#         numeroEntero = int(numeroEntero)

#         if (numeroEntero.isnumeric()) and (numeroEntero in range(0,21)):
#            print("Número digitado es correcto: ",numeroEntero)
#            controladorCiclo = False    


#######################################################################
# Ejercicio No 4:
# Liste los números primos hasta el rango que un usuario nos defina
# Un número primo es:
#   Es un número natural.
#   Es mayor que 1.
#   Son divisibles por sí mismo y por 1.
#######################################################################

# rangoFinal = int(input(" Hasta que número quiere imprimir los números primos : "))

# numeroActual = 2
# while (numeroActual >= 2) and (numeroActual <= rangoFinal):
      
#       divisor = 2
#       contadorDivisores = 0
#       # ciclo interno para identificar si tiene más de un divisor
#       while (divisor >= 2) and (divisor <= numeroActual):
#             if (numeroActual % divisor == 0):
#                contadorDivisores +=1
#             divisor +=1
            

#       #  Si no tiene más de un divisor el número es primo
#       if contadorDivisores <=1:
#          print("El número primo es ",numeroActual )
#       numeroActual +=1
