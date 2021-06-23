import operator

va_error = ""

def promedio_precios(tienda_de_carlos):
  promedio=0
  for i in tienda_de_carlos:  
    promedio+=tienda_de_carlos[i][1]
  promedio = float ( promedio / len(tienda_de_carlos) )
  return(round(promedio,1))

def precio_mayor(tienda_de_carlos):  
  #des_producto = tienda_de_carlos.nlargest(1, tienda_de_carlos[1])
  varwhile = 1
  valor = 0
  producto_while =  ""
  contador = 0

  while(varwhile <= len(tienda_de_carlos)):
    if (tienda_de_carlos[varwhile][1] > valor ):
      valor = tienda_de_carlos[varwhile][1]
      contador = varwhile
    varwhile = varwhile + 1

  producto_while = tienda_de_carlos[contador][0]
  return producto_while

def total_inventario(tienda_de_carlos):  
  total_invet  = float(0)
  for i in tienda_de_carlos:          
    total_invet = total_invet + (tienda_de_carlos[i][1] * tienda_de_carlos[i][2])
  return total_invet
  
def precio_menor(tienda_de_carlos):  
  #des_producto = tienda_de_carlos.nlargest(1, tienda_de_carlos[1])
  varwhile = 1
  valor = tienda_de_carlos[1][1]
  producto_while =  ""
  contador = 0

  while(varwhile <= len(tienda_de_carlos)):
    if (   tienda_de_carlos[varwhile][1] < valor  ):
      valor = tienda_de_carlos[varwhile][1]
      contador = varwhile
    varwhile = varwhile + 1

  producto_while = tienda_de_carlos[contador][0]
  return producto_while

def borrar_producto(tienda_de_carlos,producto):
  if producto[0] in tienda_de_carlos:
    tienda_de_carlos.pop(producto[0]) # ['Melon',70,13]
    va_error = 'ok'
   # print(tienda_de_carlos)
  else:
    va_error = 'ERROR'
  return va_error


def actualizar_producto(tienda_de_carlos,producto):
  if producto[0] in tienda_de_carlos:
    clave=producto[0] # [11,'Melon',70,13]
    #del producto[0]
    producto.pop(0) # ['Melon',70,13]
    tienda_de_carlos[clave]= producto
    va_error = 'ok'
   # print(tienda_de_carlos)
  else:
    va_error = 'ERROR'
  return va_error

def agregar_producto(tienda_de_carlos,producto):
  if producto[0] in tienda_de_carlos:
    va_error = 'ERROR'
  else:
    clave=producto[0]
    #del producto[0]
    producto.pop(0) # ['Melon',70,13]
    tienda_de_carlos[clave]= producto
    va_error = 'ok'
  #  print(tienda_de_carlos)
  return va_error


def leer_datos():
  operacion= input() # AGREGAR ACTUALIZAR BORRAR
  producto=input().split() # [11,'Melon',70,13] =producto
  producto[0]= int(producto[0])
  producto[2]= float(producto[2])
  producto[3]= int(producto[3])
  return operacion, producto

def principal():
  tienda_de_carlos={1 : ['Manzanas',8000.0,65],
                  2 : ['Limones',2300.0,15],
                  3 : ['Granadilla',2500.0,38],
                  4 : ['Arandanos',9300.0,55],
                  5 : ['Tomates',2100.0,42],
                  6 : ['Fresas',4100.0,3],
                  7 : ['Helado',4500.0,41],
                  8 : ['Galletas',500.0,8],
                  9 : ['Chocolates',3500.0,806],
                 10 : ['Jamon',15000.0,10]}
  
  #print(len(tienda_de_carlos))
  operacion, producto=leer_datos()
  validador = ''
  if (operacion == 'AGREGAR' or operacion == 'agregar'):
     validador = agregar_producto(tienda_de_carlos,producto)
  elif (operacion == 'ACTUALIZAR' or operacion == 'actualizar' ):
     validador = actualizar_producto(tienda_de_carlos,producto)
  elif (operacion == 'BORRAR' or operacion == 'borrar'):
     validador = borrar_producto(tienda_de_carlos,producto)
  
  if (validador == 'ok'):
    precio_item_mayor = precio_mayor(tienda_de_carlos)
    precio_item_menor = precio_menor(tienda_de_carlos)
    promedito_inventario = promedio_precios(tienda_de_carlos)
    total_inventario_t =  total_inventario(tienda_de_carlos)
  #precio_mayor(tienda_de_carlos),precio_menor(tienda_de_carlos),promedio_precios(tienda_de_carlos)
    print(precio_item_mayor,precio_item_menor,promedito_inventario,total_inventario_t)
  else:
      print('ERROR')


principal()
