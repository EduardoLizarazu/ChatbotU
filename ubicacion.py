
from conexion import *

conexion = conectar()
crear_tablas(conexion)


class Ubicacion:
    def __init__(self, nombre, localidad):
        self.localidad = localidad
        self.nombre = nombre
        
    
    def buscar(self, palabra):
        if palabra.lower() == self.nombre:
            for n in self.localidad.keys():
                print(n)

        for nombre, lugar in self.localidad.items():
            if palabra.lower() == nombre:
                print(nombre, lugar)
                insertar(conexion, nombre) # INSERTAR A DB




############ INSTANCIAS ################

# TIENDAS
tiendas = {
            "tienda-1": "ubicacion-1",
            "tienda-2": "ubicacion-2",
            "tienda-3": "ubicacion-3"
        }

tienda = Ubicacion("tiendas", tiendas)

# CINES
cines = {
        "cine-1": "ubicacion-1",
        "cine-2": "ubicacion-2"
    }

cine = Ubicacion("cines", cines)

# PATIOS DE COMIDA
restaurantes = {
        "patio-1": "ubicacion-1",
        "patio-2": "ubicacion-2"
    }

comida = Ubicacion("comida", restaurantes)







