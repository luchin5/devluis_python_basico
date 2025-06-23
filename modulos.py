### IMPORTACION Y CREACION DE MODULOS

import math
import random
import datetime
from math import sin
import mimodulo
from mimodulo import tinkanew
from mipaquete import modulo1,modulo2




result = math.sqrt(25) ## raiz cuadrada
senos = sin(30)

print(result)
print(senos)

## RANDOM Y FECHA
tinkanumero = random.randint(1,45)
print(tinkanumero)
print("Bienvenido a la tinka")
contador = 0
ticket = set()
while contador<6:
    numero = random.randint(1,45)
    if numero not in ticket:
        ticket.add(numero)
        contador+=1
print(ticket)

fechaactual = datetime.datetime.now()
print(fechaactual)

#
print("Me importaron ")
# mimodulo.tinkanew()
tinkanew()


modulo1.modulo1()
modulo2.modulo2()

aver = (not True) or (False and True)
print(aver)