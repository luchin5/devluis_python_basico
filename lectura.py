### LECTURA DE ARCHIVOS

archivo = open("archivo.txt","r")
contenido = archivo.read()
print(contenido)
archivo.close()

## ESCRITURA DE ARCHIVOS
nuevoarchivo = open("nuevo.txt","w")
print("Bienvenido escribe un libro")
while True:
    entrada = input()
    if entrada == "FIN":
        break
    
    nuevoarchivo.write(entrada + "\n")
nuevoarchivo.close()

## ---- version moderna -----

print("Escribe tu nuevo libro")

with open("segundo.txt","w") as segundoarchivo:
    while True:
        enter = input()
        if enter == "FIN":
            break
        segundoarchivo.write(enter+"\n")