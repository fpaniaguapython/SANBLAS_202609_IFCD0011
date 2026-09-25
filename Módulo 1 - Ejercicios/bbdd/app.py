import gestor_peliculas as gp
from pelicula import Pelicula

if __name__=='__main__':
    # Establecer conexión
    conn = gp.establecer_conexion()

    # Creación de las tablas
    # gp.crear_tablas(conn)
    
    # Crear película
    # titulo = input('Título:')
    # genero = input('Género:')
    # duracion = int(input('Duración (minutos):'))
    # anyo_estreno = int(input('Año de estreno:'))
    # director = input('Director:')
    # pelicula = Pelicula(None, titulo, genero, 
    #                     duracion, anyo_estreno, director)
    # gp.create(conn, pelicula)

    # Consultar todas
    # peliculas = gp.read_all(conn)
    # for pelicula in peliculas:
    #     print(pelicula)

    # Buscar por id
    # id = int(input('Identificador de la película:'))
    # pelicula = gp.find_by_id(conn, id)
    # print(pelicula)

    # Buscar por título
    titulo = input('Introduce título:')
    peliculas = gp.find_by_title(conn, titulo)
    print(peliculas)

    # Cerrar conexión
    gp.cerrar_conexion(conn=conn)