import sqlite3 
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect('database.db')
        return conexion
    except Error:
        print('Ha ocurrido un error')

def crear_tablas(conexion):
    cursor = conexion.cursor()
    sentencia_sql = '''CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,                         
        destino_final TEXT NOT NULL,
        satisfaccion TEXT NOT NULL,
        mensaje TEXT NOT NULL
    )'''
    cursor.execute(sentencia_sql)
    conexion.commit()

def insertar(conexion, datos): 
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (destino_final, satisfaccion, mensaje) VALUES (?,?,?)' 
    cursor.execute(sentencia_sql, datos)
    conexion.commit() 
    conexion.close()  

def insertar_varios(conexion, datos): 
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (destino_final, satisfaccion, mensaje) VALUES (?,?,?)' 
    cursor.executemany(sentencia_sql, datos) # DIFERENCIA
    conexion.commit()
    conexion.close()


conexion = conectar()
#crear_tablas(conexion) # crea tabla esto se hace al comienzo
datos = ("tienda-1", "Muy buena", "Ninguno")
insertar(conexion, datos)