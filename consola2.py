numero_uno = int(input("Digite un numero de 1  a 9  "))
numero_dos = int(input("Digite un numero de 1  a 9  "))

validador = True

while (validador):
    
    if (numero_uno >= 1 and numero_uno <= 9 ):
        validador = False
            
    else:
        numero_uno = int(input("El primer numero no cumple los parametros ingreselo nuevamente  ")) 
  

validador = True  
     
while (validador):
    
    if (numero_dos >= 1 and numero_dos <= 9 ):
        validador = False
            
    else:
        numero_dos = int(input("El segundo numero no cumple los parametros ingreselo nuevamente ")) 

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multi = numero_uno * numero_dos



print("La suma del numero 1 menos el numero 2 es  ", suma) 
print("La resta del numero 1 menos el numero 2 es  ", resta) 
print("La multiplicacion del numero 1 menos el numero 2 es  ", multi) 