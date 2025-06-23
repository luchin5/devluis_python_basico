print("hola mundo")

## TIPADO DE DATOS
numero = 20
decimal = 2.5551
cadena = "HOLA MUNDO LUIS GANARAS"
sera_verdad = True
a = b = c = 11325
_0 = 35

dividendo = 125
divisor = 7
base = 3
exponente = 3
print(base**exponente)
print(dividendo//divisor)
print(dividendo/divisor)
print(numero,decimal,cadena,sera_verdad,a,b,c,_0)

## ESTRUCTURAS CONDICIONALES

if dividendo>divisor:
    print("Se puede dividir")
else:
    print("NO se puede dividir")


## LOOPS O BUCLES

frutas =  ["Manzana","Papaya","Limón"]

for f in frutas:
    print(f)

contador = 5
while contador > 0:
    print("estoy disminuyendo")
    contador-=1  

conta = 0
while True:
    print("contador")
    print(conta)

    conta = conta + 1
    if(conta == 5):
        break    

for i in range(10):
    pass # bloque de codigo para implementar despues
    if i % 2  == 0:
        continue
    print(i)
    pass

for i in range(-3,3):
    print(" a ver ", i)

### ESTRUCTURA DE DATOS

## LISTAS

frutus = ["manzanita","pera","piña"]

frutus.append("arandano")
frutus.insert(0,"naranja")
frutus.remove("pera")

futa_eliminada = frutus.pop(0)
print(frutus)
frutus.sort()

print(frutus)
frutus.reverse()
print(frutus)

nuevalista = [1,3,5,6,7,8]

generaslistacomprension = [x ** 2 for x in nuevalista if x % 2 == 0]
print(generaslistacomprension)

## TUPLAS
tupla = (1,3,5,6)
cantidadele = tupla.count(6) # busca y cuenta un elemento 
print(tupla.index(3)) # devuelve el indice del elemento elegido 3 <
print(cantidadele)
print("tamaño tupla",len(tupla))

## DICCIONARIOS

midic = {
    "nombre":"Luis",
    "edad":34
}

midic2 = {
    "peso":55.3,
    "altura":1.7
}

print(midic["nombre"]) # IMPRIME EL VALOR DEL ATRIBUTO : Luis
print(midic.keys()) # DEVUELVE LAS CLAVES
print(midic.values()) # DEVUELVE LOS VALORES
print(midic.items()) # DEVUELVE EL OBJETO
midic.update(midic2) # AÑADE OTROS ATRIBUTOS AL DICCIONARIO ACTUAL O LOS JUNTA 
print(midic) 

## SETS se pueden hacer operaciones de conjuntos

miset = {13,56,3,13}
miset2 = {12,56,66,13}
print(miset)

interseccion = miset & miset2
print(interseccion)

union = miset | miset2
print(union)

diferencia = miset - miset2
print(diferencia)

miset.add(1225)
print(miset)

miset.remove(13)
print(miset)

miset.clear()
print(miset)

## FUNCIONES


# FUNCION SIN PARAMETRO


def saludo():
    print("Hola amigo")

# FUNCION CON PARAMETRO

def saludonormal(nombre):
    print(f"Hola soy {nombre}")


# FUNCION CON RETORNO
def sumar(a,b):
    return a+b

# FUNCION LAMBDA

cuadrado = lambda y: y **2
fu = lambda u : ((u ** 2) + 3)**0.5 

# VARIABLE GLOBAL

variable_global = 300
def sumita(a,b):
    c = a + b
    return c+variable_global

## FUNCIONES ARGS 

def media (*numeros): # LOS ALMACENA INTERNAMENTE EN UNA TUPLA
    """
    Calcular funcion args

    numeros => n numeros que vengan en el parametro
    """
    su = sum(numeros) 
    cantidad = len(numeros)
    return cantidad + su


### MANEJO DE ERRORES

""" Erro de sintaxis
    Error de nombre ?
    Error de tipo 3 o "4"
    Error de indice 0, 1, 2 ? y el 3
 """


if __name__ == "__main__":
    saludo()
    saludonormal("Luis")
    print(sumar(3,6))
    print(cuadrado(5))
    print(sumita(3,5))
    print(fu(3))
    print(media(45,4,9,81,81,81,8,18,1,832131,9616,2))