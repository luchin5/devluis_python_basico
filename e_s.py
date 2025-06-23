## ENTRADAS Y  SALIDAS DE DATOS

## ENTRADAS input siempre devuelve una cadena de texto

nombre = input("Ingrese su nombre:\n")
apellidos = input("Ingresa tu apellido:\n")

print(f"Sus datos son: {nombre} {apellidos}")


## ENTRADAS especificas con tipo de datos

edad = int(input("Ingresa tu edad:\n"))
peso = float(input("Ingresa tu peso:\n"))

if(edad>=18):
    print(f"Eres mayor de edad y tu peso es: {peso}")
else:
    print("Eres menor de edad. Adiós")