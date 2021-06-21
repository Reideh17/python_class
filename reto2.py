datos = input()

distancia_mtr =  0 
vel_max_p = 0 
vel_max_p_int = 0
vel_max_p_end = 0
segundos = 0
segundos_int = 0
segundos_end = len(datos)

vel_media = float (0)

mtr = 0
hextra = True
boni = True

var_while = 0

while ( var_while < len(datos)):
    #print(datos[var_while])
    if (datos[var_while] == " " and hextra and boni):
        mtr = var_while
        vel_max_p_int = int(var_while + 1 )
        hextra =False
    else: 
        if (datos[var_while] == " " and (hextra == False) and boni):
            boni = False
            vel_max_p_end = int(var_while )
            segundos_int = int (var_while + 1 )
    
    var_while = var_while + 1


distancia_mtr = float(datos[0:mtr])
vel_max_p = float(datos[vel_max_p_int:vel_max_p_end])
segundos = float(datos[segundos_int:segundos_end])


vel_media = ( (distancia_mtr * 3600 ) / (segundos * 1000))

validador = (vel_max_p * 25) / 100

if (distancia_mtr < 0 ):
    print("VALORES NEGATIVOS")
else:
    if (  vel_max_p < 0  ):
        print("VALORES NEGATIVOS")
    else:
        if (segundos <0 ):
            print("VALORES NEGATIVOS")  
        else:
            if (distancia_mtr < 0 and vel_max_p < 0 and segundos <0 ):
                print("VALORES NEGATIVOS")
            else:
                if (vel_media < vel_max_p):
                    print(round(vel_media,1),"OK")
                else:
                    if ( vel_media > vel_max_p and vel_media <= (vel_max_p + validador)):
                        print(round(vel_media,1),"MULTA")
                    else:
                        if ( vel_media >= (vel_max_p + validador)):
                            print(round(vel_media,1),"CURSO")