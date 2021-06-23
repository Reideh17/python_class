n, k= input().split()
n = int(n)
k = int(k)

laminas = input().split()

if n not in range(1, 10001):    
    n = 1

if k not in range(1, 10001):    
    k = 1

mi_diccionario = {}
laminas_rep = 0
laminas_en_memoria = 0

for posicion, value  in enumerate(laminas):
  if value in mi_diccionario:
    laminas_rep += 1
    if posicion - mi_diccionario[value] <= k:
      laminas_en_memoria += 1
  mi_diccionario[value] = posicion

print(laminas_rep,laminas_en_memoria)




#print(k , n)