# mimodulo.py
## IMPORTAR MODULOS PROPIOS
import random

def sumarenteros(a,b):
    return a+b

def tinkanew():
    contador = 0
    ticket = set()
    while contador <6:
        numero = random.randint(1,45)
        if numero not in ticket:
            ticket.add(numero)
            contador+=1
    print(ticket)