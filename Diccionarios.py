"""
  Diccionarios

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-2-2021          Versión inicial del programa
"""


#0. Idea intuitiva
#  Libros de Harry Potter
#
#
#   Harry Potter y la Piedra filosofal 
#   Harry Potter y la Cámara secreta 
#   Harry Potter y el Prisionero de azkaban 
#   Harry Potter y el Cáliz de fuego 
#   Harry Potter y la Orden del fénix 
#
#        ...........
#
#   LLAVE   VALOR
#   1997 : Harry Potter y la Piedra filosofal 
#   1998 : Harry Potter y la Cámara secreta 
#   1999 : Harry Potter y el Prisionero de azkaban 
#   2000 : Harry Potter y el Cáliz de fuego 
#   2003 : Harry Potter y la Orden del fénix 
#
#   Los diccionarios son ordenados, son mutables y no admiten duplicados




#1.  Crear un diccionario Vacio

# diccionario = {} 
# print(diccionario)

# diccionario = dict()
# print(diccionario)

#2. Crear un diccionario con datos

# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }

# print(librosPublicadosPotter)



#3. Crear un diccionario elemento por elemento

# librosPublicadosPotter = {}
# librosPublicadosPotter[1997]= "Harry Potter y la Piedra filosofal"
# librosPublicadosPotter[1998]= "Harry Potter y la Cámara secreta"
# librosPublicadosPotter[1999]= "Harry Potter y el Prisionero de azkaban"
# print(librosPublicadosPotter)

# #4. Obtener las llaves del diccionario

# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }



# print(librosPublicadosPotter.keys())
# print(type(librosPublicadosPotter.keys()))

#5. Obtener los valores del diccionario
# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }


#print(librosPublicadosPotter.values())
#print(type(librosPublicadosPotter.values()))

#5. Obtener el valor de un diccionario por su llave
# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }

# #Obtener el libro publicado
# print(librosPublicadosPotter[1998])
# print(librosPublicadosPotter[2003])

# print(librosPublicadosPotter.get(1997))
# print(librosPublicadosPotter.get(2003))
# print(type(librosPublicadosPotter.get(2003)))


# fecha = 2020
# if fecha  in librosPublicadosPotter:
#     print(librosPublicadosPotter[fecha])
# else:
#     print("No existe un libro para el año:",fecha)



### ******
#5.1 obtener cada item del diccionario 

# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }
# 
# items = librosPublicadosPotter.items()
# print(items)
# print(type(items))

# Pasar los items del diccionario a una lista de tuplas
# listaTuplas = list(items)
# print(listaTuplas)
# print(type(listaTuplas))

# Obtener el valor de una tupla en una lista
# print(listaTuplas[0])
# print(listaTuplas[0][1])

################################

# items = librosPublicadosPotter.items()
# print(items)
# print(type(items))

# # Pasar los items del diccionario  a una tupla
# tuplas= tuple(items)
# print(tuplas)
# print(type(tuplas))

# # Obtener el valor de una tupla de tuplas
# print(tuplas[0])
# print(tuplas[0][1])




#6. Cambiar el valor de un elemento del diccionario por su llave

# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }


# # librosPublicadosPotter[2003] = "Harry nuevo lanzamiento"
# # print(librosPublicadosPotter[2003])



# #6.1  Cambiar el valor de un elemento utilizando el método update

# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }


# librosPublicadosPotter.update({2003 : "Harry al rescate"})
# print(librosPublicadosPotter[2003])



# #7. Adicionar un elemento al diccionario
# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }

# librosPublicadosPotter[2004] = " Parte2: Harry Potter y la Orden del fénix "

# print(librosPublicadosPotter)


# #7. Remover un elemento del diccionario por llave

# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }

# librosPublicadosPotter.pop(2003)
# print(librosPublicadosPotter)

# # #7.2 Remover el último elemento insertado en el diccionario
# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }

# librosPublicadosPotter.popitem()
# print(librosPublicadosPotter)

# # #7.3 Remover un elemento con del
# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }


# del librosPublicadosPotter[1999]
# print(librosPublicadosPotter)

# librosPublicadosPotter.clear()
# print(librosPublicadosPotter)

# # #7.3 Remover todo el diccionario
# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }


# del librosPublicadosPotter
# print(librosPublicadosPotter) # error de no definida


# #8. ciclos con diccionarios

# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }

#Imprimir la llaves del diccionario
# for fechaLibro in librosPublicadosPotter:
#     print(fechaLibro,end=" ")

# for fechaLibro in librosPublicadosPotter.keys():
#     print(fechaLibro,end=" ")


#Imprimir los valores por cada llave del diccionario

# for fechaLibro in librosPublicadosPotter:
#     print("\n",librosPublicadosPotter[fechaLibro])


# for nombreLibro in librosPublicadosPotter.values():
#     print(nombreLibro)


#Imprimir las llaves y los  valores 

# for fechaLibro,nombreLibro in librosPublicadosPotter.items():
#      print("La fecha del libro es {} y el nombre  del libro es {}".format(fechaLibro,nombreLibro))



# #9. copiar un diccionario

# librosPublicadosPotter = { 1997 : "Harry Potter y la Piedra filosofal", 1998 : "Harry Potter y la Cámara secreta", \
#                            1999 : "Harry Potter y el Prisionero de azkaban", 2000 : "Harry Potter y el Cáliz de fuego", \
#                            2003: "Harry Potter y la Orden del fénix" \
#                          }

# copiaDiccionario = librosPublicadosPotter.copy()

# print(copiaDiccionario)


# #10. Diccionarios anidados

# miFamilia = { "papa" : { "nombre" : "pepito" , "edad": 25},  "mama" : { "nombre" : "pepita" , "edad": 24}, "hija" : { "nombre" : "pepin" , "edad": 2} }

# print(miFamilia["papa"])
# print(miFamilia["papa"]["nombre"])
# print(miFamilia["papa"]["edad"])

# print(miFamilia["hija"])
# print(miFamilia["hija"]["nombre"])
# print(miFamilia["hija"]["edad"])

####################################################

# papa = { "nombre" : "pepito" , "edad": 25 }
# mama = { "nombre" : "pepita" , "edad": 24 }
# hija = { "nombre" : "pepin" , "edad": 2   } 


# miFamilia ={ "papa" :papa, "mama": mama, "hija": hija}
# print(miFamilia["hija"])
# print(miFamilia["hija"]["nombre"])
# print(miFamilia["hija"]["edad"])


#10.1 Listas como valores de un diccionario

# listaPapa = ["pepito", "Mayo" ,  25]
# listaMama = ["pepita", "Junio",  24]
# listaHija = ["pepin" , "Enero",  2 ]

# elementoDiccionarioPapa = {"papa" : listaPapa}  # Sería equivalente a diccionarioPapa = {"papa" : ["pepito" , "Mayo"  ,  25]}
# elementoDiccionarioMama = {"mama" : listaMama } # Sería equivalente a diccionarioMama = {"mama" : ["pepita" , "Junio" ,  24]}
# elementoDiccionarioHija = {"hija" : listaHija}  # Sería equivalente a diccionarioHija = {"hija  : ["pepin"  , "Enero" ,   2]}

# print(len(elementoDiccionarioPapa))
# print(len(elementoDiccionarioMama))
# print(len(elementoDiccionarioHija))

#diccionarioFamilia = {"papa" : listaPapa,"mama" : listaMama, "hija" : listaHija}
# Sería equivalente a 
# diccionarioFamilia = { "papa" : ["pepito" , "Mayo"  ,  25],  "mama" : ["pepita" , "Junio" ,  24] , "hija" : ["pepin"  , "Enero" ,   2] }
# print(len(diccionarioFamilia))


# print(diccionarioFamilia["papa"][0]) # Nombre Papa
# print(diccionarioFamilia["papa"][2]) # Edad Papa
# print(diccionarioFamilia["hija"][0]) # Nombre Hija
# print(diccionarioFamilia["mama"])


#diccionarioFamilia = {elementoDiccionarioPapa,elementoDiccionarioMama,elementoDiccionarioHija}  # Error

# #11. funcion fromkeys. Crea un diccionario apartir de la llave, valor


# funcion fromkeys()

# municipios = ("sopo","guatavita","suesca")
# departamento = ("cundinamarca")

# municipiosCundinamarca =dict.fromkeys(municipios,departamento)  #todos tienes el mismo valor departamente
# print(municipiosCundinamarca)

#####################################

# municipios = ("sopo","guatavita","suesca")
# municipiosCundinamarca =dict.fromkeys(municipios) # Crea valores None si no se define valor 
# print(municipiosCundinamarca)



# #11. funcion setdefault(). Retorna el valor del item si la llave existe. Sino crea elemento


# print(municipiosCundinamarca.setdefault("fusagasuga")) # inserta fusagasuga con None


# municipiosCundinamarca.setdefault("choachi", "templado") # inserta choachi con templado
# print(municipiosCundinamarca)
