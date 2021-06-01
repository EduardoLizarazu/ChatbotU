from ubicacion import *
from conexion import *
import lectura

conexion = conectar()
crear_tablas(conexion)

chatU = input("Hola soy Alicie, en puedo ayudarle ? ")
palabras = chatU.split(" ")

for i in lectura.mayor_frecuencia_palabras.keys(): # Palabra de sugerencia
    print(f"La palabra mas frecuente es {i}")

salir = True # ENTRADA
ubicacionFinal = [] 

while salir:
    for p in palabras:
        tienda.buscar(p)
        cine.buscar(p)
        comida.buscar(p)

        if p.lower() == "salir":
            print("Nos vemos")
            salir = False # SALIDA    
    
    if p.lower() != "salir":
        chatU = input("En que otra cosa puedo ayudarle? ") 
        palabras = chatU.split(" ")

print('Fin del programa') 
