"""
  Excepciones
    
  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-08-2021          Versión inicial del programa
"""



#############################################################################
# Excepciones:
# Errores presentados en tiempo de ejecución
# La última línea de los mensajes de error indica que sucedio.
# Las excepciones vienen de distintos tipos, y el tipo se imprime
# como parte del mensaje: Ejemplo  ZeroDivisionError, NameError y TypeError
#############################################################################

#Esquema general Excepción
#try:
       # El código susceptible de error en ejecución.... 

#except:
       # Código para manejar la excepción
       # 

#else:
       # código que se ejecuta si no hay excepción

#finally:
      # código que se ejecuta siempre ( Si hay o no hay excepción)





#division = 10/0


#Traceback (most recent call last):
#  File "c:\Users\luzma\Excepciones.py", line 19, in <module>
#   division = 10/0
#   ZeroDivisionError: division by zero

# En este caso el nombre de la excepción corresponde a ZeroDivisionError ( Tipo de excepcion)




##############################################################################################################################
# La declaración try funciona de la siguiente manera:
# • Primero, se ejecuta el bloque try (el código entre las declaración try y except).
# • Si no ocurre ninguna excepción, el bloque except se salta y termina la ejecución de la declaración try.
# • Si ocurre una excepción durante la ejecución del bloque try, el resto del bloque se salta. Luego, si su tipo coincide con
#   la excepción nombrada luego de la palabra reservada except, se ejecuta el bloque except, y la ejecución continúa
#   luego de la declaración try.
# • Si ocurre una excepción que no coincide con la excepción nombrada en el except, esta se pasa a declaraciones try
#   de más afuera; si no se encuentra nada que la maneje, es una excepción no manejada, y la ejecución se frena
#   
################################################################################################################################

# try:
#     division = 10/0
#     print("Division por cero")
# except:
#     print("Division no permitida.")

# print("Sigue la ejecución")


# while True:
#        try:
#          numero = input(" Ingrese un número: ")
#          numeroEntero = int(numero)
#          break
#        except ValueError:
#          print("El valor digitado no es válido....Intenta de nuevo")




# #####################################################################################################################
# Una declaración try puede tener más de un except, para especificar manejadores para distintas excepciones. A lo sumo
# un manejador será ejecutado. Sólo se manejan excepciones que ocurren en el correspondiente try, no en otros
# manejadores del mismo try. Un except puede nombrar múltiples excepciones usando paréntesis
######################################################################################################################

# while True:
#        try:
#          numero = input(" Ingrese un número: ")
#          numeroEntero = int(numero)
#          division = numeroEntero/0         

#          break
#        except ValueError:
#             print("El valor digitado no es válido....Intenta de nuevo")

#        except ZeroDivisionError:
#             print("División por cero no es valida")



# while True:
#        try:
#          numero = input(" Ingrese un número: ")
#          numeroEntero = int(numero)
#          division = numeroEntero/0         
#          break
#        except ValueError:
#             print("El valor digitado no es válido....Intenta de nuevo")

#        except :
#             print("División por cero no es valida")


# while True:
#        try:
#          numero = input(" Ingrese un número: ")
#          numeroEntero = int(numero)
#          division = numeroEntero/0         
#          break
#        except (ValueError,ZeroDivisionError):
#             print("El valor digitado no es válido/División por cero no es válida")
#        except :
#             print("Cualquier otra excepcion")



############################################################################################################################
# Las declaraciones try ... except tienen un bloque else opcional, el cual, cuando está presente, debe seguir a los except.
# Es útil para aquel código que debe ejecutarse si el bloque try no genera una excepción.
# El bloque finally se ejecuta independientemente de que exista o no excepcion
############################################################################################################################

# x= 2
# y= 0
# try:
#      division = x / y
# except ZeroDivisionError:
#      print("Esta dividiendo por cero")
# else:
#      print("La division es correcta",division)
# finally:
#      print("Siempre se ejecuta con excepcion o sin excepción")


# while True:
#     try:
#         divisor   = input(" Ingrese divisor: ")
#         dividendo = input(" Ingrese dividendo: ")

#         divisor   = int(divisor)
#         dividendo = int(dividendo)
#         division  =  divisor/dividendo
#     except ZeroDivisionError:
#          print("Esta dividiendo por cero")
#     else:
#          print("La division es correcta",division)
#          break
#     finally:
#          print("Siempre se ejecuta con excepcion o sin excepción")



# while True:
#     try:
#         divisor   = input(" Ingrese divisor: ")
#         dividendo = input(" Ingrese dividendo: ")

#         divisor   = int(divisor)
#         dividendo = int(dividendo)
#         division  =  divisor/dividendo
#     except ZeroDivisionError:
#          print("Esta dividiendo por cero")
#     except:
#         print("valores deben ser numéricos")
#     else:
#          print("La division es correcta",division)
#          break
#     finally:
#          print("Siempre se ejecuta con excepcion o sin excepción")


# while True:
#     try:
#         divisor   = input(" Ingrese divisor: ")
#         dividendo = input(" Ingrese dividendo: ")

#         divisor   = int(divisor)
#         dividendo = int(dividendo)
#         division  =  divisor/dividendo
#     except ZeroDivisionError:
#          print("Esta dividiendo por cero")
#     except ValueError:
#         print("valores deben ser numéricos")
#     else:
#          print("La division es correcta",division)
#          break
#     finally:
#          print("Siempre se ejecuta con excepcion o sin excepción")


# try:
#     division = 10/0
#     print("Division por cero")
# except Exception as e:
#     print("Division no permitida.",e)

# print("Sigue la ejecución")


################################################
#  Generar excepciones manualmente
#  La declaración raise permite al programador 
#  forzar a que ocurra una excepción específica
################################################


# while True:
#       try:
#          divisor   = input(" Ingrese divisor: ")
#          dividendo = input(" Ingrese dividendo: ")
         
#          divisor   = int(divisor)
#          dividendo = int(dividendo)
#          if (dividendo == 0):
#             raise ZeroDivisionError("El dividendo debe ser mayor que cero")          
       
#          division = divisor/dividendo
       
#       except Exception as e:
#           print(e)
#       else:
#              print("La division es",division)
#              break
       

# print("Sigue la ejecución")



##########################################################
# Jerarquía  de las excepciones
# https://docs.python.org/es/3/library/exceptions.html
##########################################################


