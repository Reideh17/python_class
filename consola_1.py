numero_magico = 12345679 
numero_usuario = int(input("Digite un numero de 1  a 9  "))
validador = True
total = 0


while (validador):
    
    if (numero_usuario >= 1 and numero_usuario <= 9 ):
        validador = False
            
    else:
        numero_usuario = int(input("Digite un numero de 1  a 9  ")) 
        

total = int((numero_usuario * 9 )) + int(numero_usuario * numero_magico)


print(total)