
from typing import TypeVar


boolcontroladorCiclo = True

while (boolcontroladorCiclo):
        numeroEntero = input("Digite número entero :")
        if numeroEntero.isnumeric():
           numeroEntero = int(numeroEntero)
           if (numeroEntero < 10):
              print("Número digitado es correcto: ",numeroEntero)
              boolcontroladorCiclo = False    
        else:                  
            None            
            print (type(numeroEntero))

