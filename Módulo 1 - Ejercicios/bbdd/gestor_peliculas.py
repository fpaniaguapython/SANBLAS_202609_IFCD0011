'''
id - int autoincremental
titulo - str
genero - str
duracion - int
anyo_estreno - int
director - str
'''
import sqlite3
from pelicula import Pelicula

conn = None

def establecer_conexion() -> sqlite3.Connection:
    conn=sqlite3.connect("bbdd_peliculas.db")
    return conn

def crear_tablas(conn):
    sql ='''CREATE TABLE IF NOT EXISTS peliculas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        genero TEXT NOT NULL,
        duracion INTEGER NOT NULL,
        anyo_estreno INTEGER NOT NULL,
        director TEXT NOT NULL)'''
    cursor =conn.cursor()
    cursor.execute(sql)

def create_movie(conn, pelicula: Pelicula):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO peliculas 
    (titulo, genero, duracion, anyo_estreno, director) VALUES (?,?,?,?,?)''',
    (pelicula.titulo, pelicula.genero, pelicula.duracion,
     pelicula.anyo_estreno, pelicula.director))
    conn.commit()


if __name__=='__main__':
    conn = establecer_conexion()
    crear_tablas(conn)
    
    # Crear película
    titulo = input('Título:')
    genero = input('Género:')
    duracion = int(input('Duración (minutos):'))
    anyo_estreno = int(input('Año de estreno:'))
    director = input('Director:')
    pelicula = Pelicula(None, titulo, genero, 
                        duracion, anyo_estreno, director)
    create_movie(conn, pelicula)