"""
  Manejo de Archivos

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-08-2021          Versión inicial del programa
"""



####################################################################################################
# Leer un archivo de texto en python # 
# "r" - Read -  Valor por defecto. Abre el archivo para lectura. Saca error si el archivo no existe
#####################################################################################################

# try:
#   archivo = open("archivo_prueba.txt")  # Abre el archivo
    #print(archivo.read())      # Lee todo el contenido del archivo.
    #print(archivo.read(5))     # Lee cinco caracteres del archivo.
    # print(archivo.readline())  # Lee la primera línea del archivo.
    # print(archivo.readline())  # Lee la segunda línea del archivo.

    # for linea in archivo:       # Recorrer linea a linea el archivo por un for
    #     print(linea,end="") 
    # archivo.close()             # Cerrar el archivo
    # archivo.readline()          # Genera excepción al no encontrarse el archivo abierto

# except:
#     print("\n Error procesando el archivo")


#################################################
# Guardar en una lista las líneas de un archivo
#################################################

# listaLineas = []
# with open("archivo_prueba.txt") as archivo:
# 	lineas = archivo.readlines()
# 	for linea in lineas:
# 		listaLineas.append(linea.strip('\n'))
# print (listaLineas)


#############################################################
# Guardar en listas las palabras de cada linea de un archivo
#############################################################

# listaPalabras = []
# with open("archivo_prueba.txt") as archivo:
# 	for lineas in archivo:
# 		listaPalabras.append(lineas.split())

# print (listaPalabras)


#############################################################
# Guardar en un sola lista las lineas  de un archivo
#############################################################

# listaPalabras = []
# with open("archivo_prueba.txt") as archivo:
# 	for lineas in archivo:
# 		listaPalabras.append(lineas.strip("\n"))

# print (listaPalabras)

#############################################################
# Guardar en un sola lista las palabras de un archivo
#############################################################

# listaPalabras = []
# with open("archivo_prueba.txt") as archivo:
# 	for lineas in archivo:
# 		 listaPalabras.extend(lineas.strip("\n"))

# print (listaPalabras)



#############################################################################
# Escribir en un archivo existente                                          # 
# "a" - Append - Creará una arhivo si el archivo especificado no existe     #
# "x" - Create - Creará un archivo retornará un error si el archivo existe  #
# "w" - Write -  Creará un archivo si el archivo especificado no existe     #
#############################################################################

#try:
    # archivo = open("archivo_prueba.txt","a")             # Abre el archivo en modo append. Añade al final del archivo
    # archivo.write("Esta es una cuarta línea de prueba")  # Escribir en el archivo.
    # archivo.close()                                      # Cerrar el archivo

    # archivo = open("archivo_prueba.txt","r")             # Abre el archivo en modo lectura.
    # print(archivo.read() )

    # ------------------------------------------
    
#     archivo = open("archivo_prueba.txt","w") 
#     archivo.write("Vamos a sobreescribir todo el archivo")  #  Sobreescribir el archivo.
#     archivo.close()                                         # Cerrar el archivo
#     archivo = open("archivo_prueba.txt","r")                # Abre el archivo en modo lectura.
#     print(archivo.read() )


# except:
#     print("Error procesando el archivo")


#########################################################################
# Crear un archivo 
# "x" - Create - Creará un archivo retornará un error si el archivo existe
# "a" - Append - Creará una arhivo si el archivo especificado no existe
# "w" - Write -  Creará un archivo si el archivo especificado no existe
#########################################################################

##########
# Caso 1
##########
# try:
#     archivo = open("archivo_prueba_cinco.txt","x")  # Genera excepción porque el archivo ya existe
# except:
#     print("Error procesando el archivo")


##########
# Caso 2
##########
# try:
#     archivo    = open("archivo_prueba.txt","w") # El archivo existe pero no genera excepción
#     archivoDos = open("archivo_prueba_seis.txt","w") #El archivo no existe y lo crea
# except:
#     print("Error procesando el archivo")


##########
# Caso 3
##########
# try:
#     archivo     = open("archivo_prueba.txt","a") # El archivo existe pero no genera excepción
#     archivoTres = open("archivo_prueba_ocho.txt","a") # El archivo no existe y lo crea
# except:
#     print("Error procesando el archivo")




#########################################################################
# Borrar un archivo 
# Se debe importar el modulo OS  y llamar el metodo remove 
#########################################################################

##########
# CASO 1
##########
# from os import remove
# try:
#    remove("archivo_prueba.txt")
# except:
#    print("Error procesando el archivo")

##########
# CASO 2
##########

# import os 
# if os.path.exists("archivo_prueba.txt"):  # Valida primero si el archivo existe
#    os.remove("archivo_prueba.txt")
# else:
#   print("El archivo no existe")





