### MANEJO DE EXCEPCIONES

try:
    res = 10/0
    print(res)
except ZeroDivisionError:
    print("Error de división 0")
except ValueError:
    print("Error: Valor inválido")

## FINALLY

try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    print("No se puede cerrar el archivo por q no existe")
    #archivo.close()

## EXCEPCIONES PERSONALIZADAS

def funcion():
    # excepcion personalizada
    print("Entre a la funcion")
    if 3>0:
        raise Exception("Descripcion del error")
    
try:
    funcion()
except Exception as e:
    print(f"Error : {e}")