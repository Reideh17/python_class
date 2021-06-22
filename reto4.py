n, k= input().split()
n = int(n)
k = int(k)
if n not in range(1, 1001):
  print('fuera de rango')
  if k<1 and k>1000:
    print('fuera de rango')
else:
  valores = input().split() 
  valores_int = []
  for i in valores:
    valores_int.append(int(i))
  print(valores)
  print(valores_int)