'''
id - int autoincremental
titulo - str
genero - str
duracion - int
anyo_estreno - int
director - str
'''
class Pelicula:
    def __init__(self, id: int, titulo: str, genero: str, 
                 duracion: int, anyo_estreno: int, director: str):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.anyo_estreno = anyo_estreno
        self.director = director