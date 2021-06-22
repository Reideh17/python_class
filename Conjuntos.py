"""
  Conjuntoa
  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-08-2021          Versión inicial del programa
"""

# Un conjunto son objetos mutables vía add() y discard().
# No obstante, un conjunto no puede incluir objetos mutables como listas, diccionarios, e incluso otros conjuntos.
# Sus valores no se repiten.




#######################
# Crear un conjunto
#######################

# conjunto = {1, True, "Sandía",(1,2)}
# print(conjunto)

# conjuntoNumeros = set()  # crea un conjunto
# print(type(conjuntoNumeros))

# numeros = {}     # crea un diccionario 
# print(type(numeros))

# numeros= {[1,2]} 
# print(numeros)     # Saca error




###########################################
# Crea un conjunto apartir de un iterable
###########################################

# conjuntoNumeros = set([1,2,3,4,5])
# print(conjuntoNumeros) 

# conjuntoNumeros = set(range(5))
# print(conjuntoNumeros)


###############################################
#  Conversiones
###############################################

# # Convertir un conjunto a lista 
# conjuntoNumeros = set(range(5))
# listaNumeros = list(conjuntoNumeros)
# print(listaNumeros)

# # Convertir una lista a conjunto

# conjuntoNumeros = set([1,2,3,4,5,5 ])  # si hay elementos duplicados, se unifican
# print(conjuntoNumeros) 

# conjuntoNumeros  = {20,30,40,50,20}  # si hay elementos duplicados, se unifican
# print(conjuntoNumeros)

# conjuntoCaracteres = set("vocaless")  # si hay elementos duplicados, se unifican
# print(conjuntoCaracteres)


###############################################
#  Acceso a los elementos de un conjunto - for
##############################################

# conjuntoFrutas = {"mango","mora","fresa","ciruela"}
# for fruta in conjuntoFrutas:
#     print(fruta,end=" ")


# conjuntoFrutas = {"mango","mora","fresa","ciruela"}
# if  "mango" in conjuntoFrutas:
#      print("La cadena está en el conjunto frutas")
# else:
#      print("La cadena No está en el conjunto frutas")



##############################################
# Operaciones con conjuntos
##############################################

################################################################### 
# adiciona un elemento al conjunto. Si ya existe no tiene efecto
###################################################################
# conjuntoFrutas = {"mango","mora","fresa","ciruela"}
# conjuntoFrutas.add("frambuesa")
# print(conjuntoFrutas)

# conjuntoNumeros = {1,2,3,4}
# conjuntoNumeros.add(5)
# print(conjuntoNumeros)

# Borrar los elementos de un conjunto

# conjuntoFrutas = {"mango","mora","fresa","ciruela"}
# conjuntoFrutas.clear()
# print(conjuntoFrutas)


# conjuntoFrutas[0]="pera"   # Marca error


################################################################### 
# Encontrar la diferencia entre dos conjuntos
###################################################################

conjuntoNumerosSeis = {1,2,3,4,5,6 }
conjuntoNumerosDiez = {1,2,3,4,5,6,7,8,9,10}

# diferencia = conjuntoNumerosSeis.difference(conjuntoNumerosDiez) # Los que están en conjuntoNumeroSeis que no estan en conjuntoNumerosDiez
# print(diferencia)


# diferenciaSimetrica = conjuntoNumerosSeis.symmetric_difference(conjuntoNumerosDiez) # La Union de los dos y se quitan los comunes
# print(diferenciaSimetrica)

# diferencia = conjuntoNumerosDiez.difference(conjuntoNumerosSeis) # Los que están en conjuntoNumeroDiez que no estáb en conjuntoNumeroSeis
# print(diferencia)

# diferenciaSimetrica = conjuntoNumerosDiez.symmetric_difference(conjuntoNumerosSeis)
# print(diferenciaSimetrica)

# diferencia  =  conjuntoNumerosSeis - conjuntoNumerosDiez # Los que están en conjuntoNumeroSeis que no estan en conjuntoNumerosDiez
# print(diferencia)


# diferencia  =  conjuntoNumerosDiez - conjuntoNumerosSeis # Los que están en conjuntoNumeroDiez que no estáb en conjuntoNumeroSeis
# print(diferencia)


# conjuntoNumerosSeis = {1,3,5,7,9 }
# conjuntoNumerosDiez = {1,2,3,4,5,6,7,8}


# diferencia = conjuntoNumerosSeis.difference(conjuntoNumerosDiez) # Los que están en conjuntoNumeroSeis que no estan en conjuntoNumerosDiez
# print(diferencia)

# diferencia = conjuntoNumerosDiez.difference(conjuntoNumerosSeis) # Los que están en conjuntoNumeroDiez que no estáb en conjuntoNumeroSeis
# print(diferencia)


# diferenciaSimetrica = conjuntoNumerosSeis.symmetric_difference(conjuntoNumerosDiez) # La Union de los dos y se quitan los comunes
# print(diferenciaSimetrica)



# diferenciaSimetrica = conjuntoNumerosDiez.symmetric_difference(conjuntoNumerosSeis) # La Union de los dos y se quitan los comunes
# print(diferenciaSimetrica)






######################################################################### 
# Determinar si dos conjuntos son iguales
# Dos conjuntos son iguales si y solo si contienen los mismos elementos 
#########################################################################

# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# conjuntoNumerosDiez = {1,2,3,4,5,6,7,8,9,10}

# if conjuntoNumerosDiez == conjuntoNumerosSeis:
#     print("Los conjuntos son iguales")
# else:
#     print("Los conjuntos son diferentes")

# conjuntoNumerosSeis = {1,2,3,4,5,6}
# conjuntoNumerosDiez = {6,5,4,3,2,1}

# if conjuntoNumerosDiez == conjuntoNumerosSeis:
#     print("Los conjuntos son iguales")
# else:
#     print("Los conjuntos son diferentes")




######################################################################### 
#  Discard() - remueve un elemento desde un conjunto 
#########################################################################

# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# conjuntoNumerosSeis.discard(6)
# print(conjuntoNumerosSeis)

# conjuntoFrutas = {"mango","mora","fresa","ciruela"}
# conjuntoFrutas.discard("mora")
# print(conjuntoFrutas)

# conjuntoFrutas = {"mango","mora","fresa","ciruela"}
# conjuntoFrutas.discard("agraz")     # Si no existe el elemento el conjunto no cambia
# print(conjuntoFrutas)



########################################################################### 
#  Intersection() - El método devuelve la intersección entre los conjunto
###########################################################################

# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# conjuntoNumerosDiez = {1,2,3,4,5,6,7,8,9,10}

# interseccion = conjuntoNumerosSeis.intersection(conjuntoNumerosDiez)
# print(interseccion)

# interseccion = conjuntoNumerosDiez.intersection(conjuntoNumerosSeis)
# print(interseccion)

# interseccion = conjuntoNumerosSeis & conjuntoNumerosDiez
# print(interseccion)


########################################################################################
# isdisjoint() - devuelve el valor True si NO hay elementos comunes entre los conjuntos 
########################################################################################

# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# conjuntoNumerosDiez = {1,2,3,4,5,6,7,8,9,10}

# if conjuntoNumerosSeis.isdisjoint(conjuntoNumerosDiez):
#    print("No hay valores en común") 
# else:
#    print("Hay valores en común") 


# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# conjuntoNumerosDiez = {7,8,9,10}
# if conjuntoNumerosSeis.isdisjoint(conjuntoNumerosDiez):
#    print("No hay valores en común") 
# else:
#    print("Hay valores en común") 


########################################################################################
# issubset() - devuelve el valor True si un conjunto es subconjunto del otro
##########################################################################################

# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# conjuntoNumerosDiez = {1,2,3,4,5,6,7,8,9,10}

# if conjuntoNumerosSeis.issubset(conjuntoNumerosDiez):
#     print("Es subconjunto")                         # El conjuntoNumerosSeis es subconjunto del conjuntoNumerosDiez    
# else:
#     print("No es subconjunto")


# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# conjuntoNumerosDiez = {1,2,3,4,5,6,7,8,9,10}

# if conjuntoNumerosDiez.issubset(conjuntoNumerosSeis):
#     print("Es subconjunto")                         # El conjuntoNumerosDiez no es subconjunto del conjuntoNumerosSeis
# else:
#     print("No es subconjunto")


###################################################
# pop() - Remueve un valor aleatorio del conjunto
###################################################
# conjuntoNumerosSeis = {1,2,3,4,5,6 }

# numero = conjuntoNumerosSeis.pop()
# print(numero)
# print(conjuntoNumerosSeis)


###################################################
# remove() - Remueve un elemento
###################################################
# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# conjuntoNuevo = conjuntoNumerosSeis.remove(1)
# print(conjuntoNuevo)

# conjuntoFrutas = {"mango","mora","fresa","ciruela"}
# conjuntoFrutas.remove("mango")
# print(conjuntoFrutas)


##############################################################################################
# Union() - Devuelve un conjunto con todos los elementos que están en alguno de los conjuntos
##############################################################################################
# conjuntoFrutas = {"mango","mora","fresa","ciruela"}
# conjuntoNumerosSeis = {1,2,3,4,5,6 }
# unionConjuntos = conjuntoNumerosSeis.union(conjuntoFrutas)
# print(unionConjuntos)




