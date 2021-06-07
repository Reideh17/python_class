"""
  Ejercicios de repaso: Estructuras de decisión.
  
  Autor :  Formador
  Creación/ Actualización  Observaciones
     Mayo-26-2021          Versión inicial del programa
"""


# Nota generales:
# condición: se crea utilizando operadores relacionales o de comparación y lógicos
# Operadores relacionales:
#    “==” se usa para determinar si dos valores son exactamente iguales. Ejemplo: 2 == 2    Resultado: true
#    “!=” se usa para determinar Si dos valores son diferentes. Ejemplo: 2 != 5  Resultado:  true
#    “>”  se usa para determinar si el valor de la izquierda es mayor que el de la derecha. Ejemplo: 4 > 2  Resultado:true
#    “<“  se usa para determinar si el valor de la izquierda es menor que el de la derecha. Ejemplo: 1 < 2  Resultado:true
#    ">=” se usa para determinar si el valor de la izquierda es mayor o igual que el de la derecha. Ejemplo: 4 >= 2  Resultado:true
#    "<=" se usa para determinar si el valor de la izquierda es menor o igual que el de la derecha. Ejemplo: 4 <= 6  Resultado:true
# Operadores lógicos:
#   "and"  :  Si y sólo si todos los elementos son True dará por resultado True. Sino False
#   "or"   :  Si algún elemento es True dará por resultado True. Sino False
#   "Not"  :  El operador “not” es unario, de negación por ende solo dará True si su elemento es False y viceversa.






# Ejercicio No 1
# Dados los tres lados de un triangulo, determine si el triangulo es equilatero, isoceles o obtuso
# Triangulo equilatero: Tiene todos los lados iguales
# Triangulo isoceles:  Tiene dos lados iguales y uno desigual
# Triangulo escaleno:  Tiene todos los lados desiguales


# Alternativa 1
ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
                            input("Digite el valor del lado dos del triángulo   : "), \
                            input("Digite el valor del lado tres del triángulo  : ")


if ((ladoUno == ladoDos) and (ladoDos == ladoTres)):
   print (" El triangulo es equilatero")
else:
     if  (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
         print (" El triangulo es isóceles ")
     else:
         print ("El triangulo es escaleno")
        
        
# Alternativa 2

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")


# if ((ladoUno == ladoDos) and (ladoDos == ladoTres)):
#     print (" El triangulo es equilatero")
# elif (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
#      print (" El triangulo es isóceles ")
# else:
#      print ("El triangulo es escaleno")

# Alternativa 3

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")


# if ((ladoUno != ladoDos) and (ladoDos != ladoTres) and (ladoUno != ladoTres)):
#     print (" El triangulo es escaleno")
# else:
#     if  (ladoUno == ladoDos == ladoTres):
#         print (" El triangulo es equilatero ")
#     else:
#         print ("El triangulo es isóceles ")

# Alternativa 4

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")


# if ((ladoUno != ladoDos) and (ladoDos != ladoTres) and (ladoUno != ladoTres)):
#     print (" El triangulo es escaleno")
# elif (ladoUno == ladoDos == ladoTres):
#      print (" El triangulo es equilatero ")
# else:
#      print ("El triangulo es isóceles ")