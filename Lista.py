# # #creo una lista vacia
# numeros = []
# print(numeros)

# # # #Añadir elementos a lista 
# numeros.append(5)
# print(numeros)

# numeros.append("piña")
# print(numeros)

# numeros.append("sandia")
# print(numeros)

# numeros.append("calabazas")
# print(numeros)

# numeros.append("manzanas")
# print(numeros)

# numeros.append("peras")
# print(numeros)

# numeros.append("uvas")
# print(numeros)

# numeros.append("zanahorias")
# print(numeros)

# numeros.append("bananos")
# print(numeros)

# numeros.append("cerezas")
# print(numeros)

# numeros.append("fresas")
# print(numeros)

# numeros = [5,"piña","sandia","calabazas","manzanas","peras","uvas","zanahorias","bananos","cerezas","fresas"]
# print(numeros)

# # # #Cambiar el valor de un elemento 
# numeros[0] = 6
# print(numeros)

# numeros[2] = "piña"
# print(numeros)

# numeros[-3] = "agraz"
# print(numeros)

# # # #Ver un rango de la lista con incrementos
# numeros = [5,"piña","sandia","calabazas","manzanas","peras","uvas","zanahorias","bananos","cerezas","fresas"]
# porcionLista = numeros[1:10:2]
# porcionLista = numeros[4:]
# porcionLista = numeros[:3]
# print(porcionLista)

# # #Insertar un elemento a la lista
# numeros.insert(9,"melocotones") # El elemento que inserto queda en esa posición
# print(numeros)

# # # #Borrar un elemento a la lista por indice
# numeros.pop(0)
# print(numeros)

# # # #Borrar  el primer elemento que coincida en contenido
# numeros.remove("fresas")
# print(numeros)

# del numeros[0:len(numeros)+1]
# print(numeros)

# # # ######################################################
# # # #  OTRAS FUNCIONES CON LISTAS
# # # ######################################################

# # # #funcion count() cuenta la cantidad de veces que un elemento aparece en la lista.
# numeros = [5,"piña","fresas","calabazas","manzanas","fresas","uvas","zanahorias","bananos","cerezas","fresas"]
# numeroRepeticiones = numeros.count("fresas")
# print(numeroRepeticiones)

# # # #funcion extend() extiende una lista agregando un iterable al final.
# numeros.extend(["moras"])
# print(numeros)

# # # #funcion index() recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.
# indice =numeros.index("fresas")
# print(indice)

# indice =numeros.index("fresas",3) # Devuelve el índice de la primera aparición apartir de la posición 3
# print(indice)

# # # #funcion reverse(). Asigna sobre la misma variable.
# # # #invierte el orden de los elementos de una lista. 
# # numeros.reverse() 
# # print(numeros)

# # # #funcion sort(). Asigna sobre la misma variable
# # # #ordena los elementos de una lista. 

# # numeros = [5,"piña","fresas","calabazas","manzanas","fresas","uvas","zanahorias","bananos","cerezas","fresas"]
# # system('cls')
# # print(numeros)
# # numeros.pop(0)
# # print(numeros)
# # numeros.sort()
# # print(numeros)
# # numeros.sort(reverse=True)
# # print(numeros)



# # # for con listas
# # numeros = ["piña","fresas","calabazas","manzanas","fresas","uvas","zanahorias","bananos","cerezas","fresas"]

# # for fruta  in numeros:
# #   print(fruta, end =" ")

# # # for con indice

# # numeros = ["piña","fresas","calabazas","manzanas","fresas","uvas","zanahorias","bananos","cerezas","fresas"]

# # for indice in range(len(numeros)):
# #   print(numeros[indice],end=" ")


# # #while 

# # numeros = ["piña","fresas","calabazas","manzanas","fresas","uvas","zanahorias","bananos","cerezas","fresas"]
# indice = 0
# while indice < len(numeros):
#   print(numeros[indice])
#   indice = indice + 1



# # # Unión de listas con concatenación

# # frutas   = ["fresa", "mango", "agraz"]
# # verduras = ["tomate", "lechuga", "repollo "]

# # alimentos = frutas + verduras

# # print(alimentos)


# # # Unión con for

# # frutas   = ["fresa", "mango", "agraz"]
# # verduras = ["tomate", "lechuga", "repollo "]


# # for verdura in verduras:
# #   frutas.append(verdura)

# # print(frutas)

# # # Unión con  extend()

# # frutas   = ["fresa", "mango", "agraz"]
# # verduras = ["tomate", "lechuga", "repollo "]

# # frutas.extend(verduras)
# # print(frutas)
