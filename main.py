from ubicacion import *
from conexion import *


conexion = conectar()
crear_tablas(conexion)

chatU = input("Hola soy Alicie, en puedo ayudarle ? ") 
palabras = chatU.split(" ")

salir = True # ENTRADA
ubicacionFinal = [] 

while salir:
    for p in palabras:
        aux_ubicacion_final = tienda.buscar(p)
        ubicacionFinal.append(aux_ubicacion_final)

        aux_ubicacion_final = cine.buscar(p)
        ubicacionFinal.append(aux_ubicacion_final)

        aux_ubicacion_final = comida.buscar(p)
        ubicacionFinal.append(aux_ubicacion_final)

        if p.lower() == "salir":
            print("Nos vemos")
            salir = False # SALIDA    
    
    if p.lower() != "salir":
        chatU = input("En que otra cosa puedo ayudarle? ") 
        palabras = chatU.split(" ")


# LIMPIEZA DE NONE
ubicacion_final = []
for i in ubicacionFinal:
    if i != None:
        ubicacion_final.append(i)
print(f"la ubicacion final es {ubicacion_final}")



print('Fin del programa')  