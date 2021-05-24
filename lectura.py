from conexion import conectar, consultar
import ubicacion

conexion = conectar()
datos = consultar(conexion) 

    
# esto puedo hacer en ubicacion.py crear un metodo ya que tengo tambien importado conexion.py

def contador_palabras_repetidas(datos):
    diccionario = {}
    lista = []
    for dato in datos:
        lista.append(dato[1])

    lista_nombres = ubicacion.tienda.obtener_keys()
    for nombre in lista_nombres:
        repeticiones = lista.count(nombre)
        diccionario[nombre] = repeticiones 

    return diccionario

print(contador_palabras_repetidas(datos))

#print(ubicacion.tienda.obtener_keys())