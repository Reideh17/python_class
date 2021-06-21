lista = [1,2,3,4,5,6,7,8,9,0] 
numero_usuario = int(input("Digite un numero de 1  a 9  "))
validador = True

while (validador):
    
    if (numero_usuario >= 1 and numero_usuario <= 9 ):
        validador = False
            
    else:
        numero_usuario = int(input("El numero ingresado no cumplr por favor digite un numero de 1  a 9  ")) 
        

if ( numero_usuario in lista ):
    print("esta en la lista")
else :
    print(" no esta en la lista")







# print(total)