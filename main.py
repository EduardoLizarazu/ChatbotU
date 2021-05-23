from ubicacion import *
from conexion import *
import conexion

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
def limpieza(ubicacion_sucia):
    ubicacion_final = []
    for i in ubicacion_sucia:
        if i != None:
            ubicacion_final.append(i) # NOMBRE_UBICACION_LISTA
    return ubicacion_final

ubicacion_limpia = tuple(limpieza(ubicacionFinal))
print(f"la ubicacion final es {ubicacion_limpia}")

insertar(conexion, ubicacion_limpia)


print('Fin del programa') 
