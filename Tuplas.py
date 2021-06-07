"""
  Tuplas  en python
  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Mayo-28-2021          Versión inicial del programa
"""

# #################
# Crear una tupla
###################


# tuplaMeses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  # tupla
# listaMeses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio"]  # lista

# tuplaDias  = 'Lunes', 'Martes', 'Miercoles', 'jueves','viernes'  # tupla sin paréntesis
# print(tuplaDias)

# lunes,martes,miercoles,jueves,viernes =  tuplaDias
# print(lunes)
# print(martes)
# print(miercoles)
# print(jueves)
# print(viernes)

# lunes,martes,miercoles,jueves,viernes =  'Lunes', 'Martes', 'Miercoles', 'jueves','viernes'
# print(lunes)
# print(martes)
# print(miercoles)
# print(jueves)
# print(viernes)

# Crear una tupla con un sol0 elemento, colocar una coma la final

# tuplaAgosto = ("agosto",)
# print(type(tuplaAgosto))

# tuplaAgosto = ('agosto')
# print(type(tuplaAgosto))


####################################################
# Accediendo al valor de los elementos de una tupla
####################################################

# tuplaMeses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  # tupla
# enero = tuplaMeses[0]
# julio =tuplaMeses[-1]
# print(enero)
# print(julio)

#############################################################################################################
# Las tuplas son inmutables: No se pueden adicionar elementos o eliminar elementos de la tupla una vez creada
#############################################################################################################

# No puedo hacer esto
# tuplaMeses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  # tupla
# tuplaMeses[0] = "Diciembre"

#Pero si puedo hacer esto
# tuplaMesesJulio = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  # tupla 1
# tuplaMesesDiciembre = ("Agosto","Septiembre","Octubre","Noviembre","Diciembre")  # tupla 2
# tuplaTodosMeses = tuplaMesesJulio + tuplaMesesDiciembre
# print(tuplaTodosMeses)

# tuplaTres  = (1,2,3)
# tuplaSeis  = (4,5,6)
# tuplaTotal =  tuplaTres + tuplaSeis
# print(tuplaTotal)



# #######################################################################
# # Porciones o rebanadas o slice de una tupla 
# #######################################################################

# tuplaMesesJulio = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  

# tresElementos = tuplaMesesJulio[0:3]
# print(tresElementos)

# tresElementos = tuplaMesesJulio[2:5]
# print(tresElementos)

# porcionFinal  = tuplaMesesJulio[4:]
# print(porcionFinal)

# porcionInicial = tuplaMesesJulio[:2]
# print(porcionInicial)

# porcion = tuplaMesesJulio[-2]
# print(porcion)

# porcion = tuplaMesesJulio[:]
# print(porcion)

# porcion = tuplaMesesJulio[0:7:2]
# print(porcion)


# ####################################
# # Borrar completamente una tupla 
# ####################################
# tuplaMesesJulio = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  
# print(tuplaMesesJulio)
# del tuplaMesesJulio
# #print(tuplaMesesJulio) # Marca error


# ####################################
# # For con tuplas 
# ####################################

# tuplaMesesJulio = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  
# for mes in tuplaMesesJulio:
#   print(mes,end="  ")


# tuplaMesesJulio = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  
# for numero in range(len(tuplaMesesJulio)):
#   print(tuplaMesesJulio[numero],end="  ")



# ####################################
# # while con tuplas 
# ####################################

# tuplaMesesJulio = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")  
# controladorCiclo  = 0
# while controladorCiclo < len(tuplaMesesJulio):
#   print(tuplaMesesJulio[controladorCiclo],end=" ")
#   controladorCiclo +=1



# ####################################
#  concaternar y Multiplicar tuplas  
# ####################################

# tupla1 = ("a", "b" , "c")
# tupla2 = (1, 2, 3)

# tupla3 = tupla1 + tupla2
# print(tupla3)



# tuplaFestivos = ("lunes festivo", "domingo festivo", "viernes festivos")
# variosFestivos = tuplaFestivos * 2
# print(variosFestivos)

# #################################################################
#  comparación de las tuplas  
#  Python comienza comparando el primer elemento de cada secuencia. 
#  Si son iguales, pasa al siguiente elemento, y así sucesivamente, 
#  hasta encontrar elementos que difieren
# ##################################################################

# if  (0, 1, 2) < (0, 3, 4):
#     print(" la primera tupla es menor que la segunda")
# else:
#     print(" la primera tupla es mayor que la segunda")


# ####################################
#  Métodos de las tuplas  
# ####################################

# # count() : Devuelve el número de veces que un valor se repite en la tupla
# tuplaFestivos = ("festivo", "festivo", "festivo")
# print (tuplaFestivos.count("festivo"))


# # index() : Busca en la tupla por un valor específico y retorna la posición donde fue encontrado
# tuplaFestivos = ("lunes festivo", "domingo festivo", "viernes festivo")

# print(tuplaFestivos.index("viernes festivo"))
  



# Tamaño una tupla 
# a = tuple(range(1000))
# b = list(range(1000))

# a.__sizeof__() # 8024
# b.__sizeof__() # 8040

# print(a.__sizeof__())
# print(b.__sizeof__())













