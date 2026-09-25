"""
Implementa el CRUD de una base de datos de películas
en SQLITE.

- id - int autoincremental
- titulo - str
- genero - str
- duracion - int
- anyo_estreno - int
- director - str
"""

import sqlite3
from pelicula import Pelicula

conn = None

def establecer_conexion() -> sqlite3.Connection:
    """
    Crea una conexión con la base datos bbdd_peliculas.db. 
    Si no existe el fichero lo crea.

    Return:
    - Conexión abierta con la base de datos
    """
    conn=sqlite3.connect("bbdd_peliculas.db")
    return conn

def crear_tablas(conn: sqlite3.Connection):
    sql ='''CREATE TABLE IF NOT EXISTS peliculas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        genero TEXT NOT NULL,
        duracion INTEGER NOT NULL,
        anyo_estreno INTEGER NOT NULL,
        director TEXT NOT NULL)'''
    cursor =conn.cursor()
    cursor.execute(sql)
    conn.commit()

def create(conn: sqlite3.Connection, pelicula: Pelicula):
    if (conn==None):
        conn = establecer_conexion()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO peliculas 
    (titulo, genero, duracion, anyo_estreno, director) VALUES (?,?,?,?,?)''',
    (pelicula.titulo, pelicula.genero, pelicula.duracion,
     pelicula.anyo_estreno, pelicula.director))
    conn.commit()

def read_all(conn: sqlite3.Connection) -> list:
    if (conn==None):
            conn = establecer_conexion()
    sql = 'SELECT * FROM peliculas'
    cursor = conn.cursor()
    cursor.execute(sql)
    lista_peliculas = cursor.fetchall()
    return lista_peliculas

def find_by_id(conn: sqlite3.Connection, id: int) -> tuple:
    if (conn==None):
        conn = establecer_conexion()
    sql = 'SELECT * FROM peliculas WHERE id=?'
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    pelicula = cursor.fetchone()
    return pelicula
    
def find_by_title(conn: sqlite3.Connection, titulo: str) -> list:
    if (conn==None):
        conn = establecer_conexion()
    sql = 'SELECT * FROM peliculas WHERE titulo LIKE ?'
    cursor = conn.cursor()
    cursor.execute(sql, (f'%{titulo}%',))
    peliculas = cursor.fetchall()
    return peliculas           


def cerrar_conexion(conn: sqlite3.Connection):
    # if conn != None:
    if conn is not None:
        conn.close()


