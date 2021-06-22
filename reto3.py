
def leer_datos():
  N=int(input()) 
  servicios=[]
  for i in range(N): 
    x=list(map(int, input().split())) 
    servicios.append(x)
  return servicios
  
def cartera():
  servicios = leer_datos()
  seleccion=[]
  for i in range(len(servicios)): 
    if servicios[i][0]>=3 and servicios[i][1]<70 and servicios[i][2]<=4 and servicios[i][3]<=0 and servicios[i][4]>=101:
      seleccion.append(servicios[i][4])  
  if len(seleccion)==0:
    print('NO DISPONIBLE')
  else:
    for i in range(len(seleccion)): 
      print(seleccion[i])  
   
cartera()