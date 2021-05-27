from conexion import conectar, consultar
import ubicacion

conexion = conectar()
datos = consultar(conexion) 

def funcion_aux(lista, lista_nombres):
    diccionario = {}
    for nombre in lista_nombres:
        repeticiones = lista.count(nombre)
        diccionario[nombre] = repeticiones
    return diccionario

def contador_palabras_repetidas(datos):
    diccionario = {}
    lista = []
    for dato in datos:
        lista.append(dato[1])

    diccionario_aux = funcion_aux(lista, ubicacion.tienda.obtener_keys())
    diccionario.update(diccionario_aux)

    diccionario_aux = funcion_aux(lista, ubicacion.cine.obtener_keys())
    diccionario.update(diccionario_aux)

    diccionario_aux = funcion_aux(lista, ubicacion.comida.obtener_keys())
    diccionario.update(diccionario_aux)

    return diccionario

def mayor_frecuencia(dic):
    lista = []
    for frecuencia in dic.values():
        lista.append(frecuencia)
    numeroMayor = max(lista)
    
    mayorFrecuencia = {}
    for i,j in dic.items():
        if dic[i] == numeroMayor:
             mayorFrecuencia[i] = j
    return mayorFrecuencia


#print(mayor_frecuencia(contador_palabras_repetidas(datos)))

mayor_frecuencia_palabras = mayor_frecuencia(contador_palabras_repetidas(datos))


