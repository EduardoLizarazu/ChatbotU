from os import pipe
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
        destino_final TEXT NOT NULL
    )'''
    cursor.execute(sentencia_sql)
    conexion.commit()

def insertar(conexion, ubicacion): 
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (destino_final) VALUES (?)' 
    datos = (ubicacion,)
    cursor.execute(sentencia_sql, datos) # CURIOSIDAD 1
    conexion.commit() 



