datos = input()

salario_base =  0 
horas_ext = 0 
bonificacion = 0

sal_base = 0
hextra = True
boni = True

var_while = 0

while ( var_while < len(datos)):
    #print(datos[var_while])
    if (datos[var_while] == " " and hextra and boni):
        sal_base = var_while
        horas_ext = int(datos[var_while + 1 ])
        hextra =False
    else: 
        if (datos[var_while] == " " and (hextra == False) and boni):
            boni = False
            bonificacion = int (datos[var_while + 1 ])
    
    var_while = var_while + 1

salario_base = float(datos[0:sal_base])


if horas_ext < 0 :
 horas_ext = 0

if bonificacion < 0 :
 bonificacion = 0

if bonificacion > 1 :
 bonificacion = 1

val_hora_normal = (salario_base / 166)
recargo_hora_extra = (val_hora_normal * 29)/100
val_hora_extra = val_hora_normal + recargo_hora_extra
val_bonificacion = (salario_base * 7.5)/100


total_hora_extra = val_hora_extra * horas_ext
toltal_bonificacion = val_bonificacion * bonificacion

salario_total = salario_base + total_hora_extra + toltal_bonificacion

salud = (salario_total * 3.5)/100
pension = (salario_total * 5)/100
caja = (salario_total * 5)/100

salario_total_desc = salario_total -  (salud + pension + caja)

print(round(salario_total, 1), round(salario_total_desc, 1))

