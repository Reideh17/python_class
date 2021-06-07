boolCiclo = True
intSuma = 1
strDato = ""

while (boolCiclo):    
    strDato = input("Coloca tu clave   : ")
    
    if (strDato == 'hedier'):
        print ("Hola",strDato)
        boolCiclo = False
    else:
        print ("Error de contraseña numero de intento ",intSuma)
        intSuma += 1
    
    if (intSuma > 3):
        print ("Muchos intentos cuenta bloqueada ")
        boolCiclo = False
        