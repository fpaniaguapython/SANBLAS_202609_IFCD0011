'''
1000 tuplas.
Título de película
Director
Género
Año

1. Buscar todas las películas de terror del año 1989.
2. Buscar todas las películas de terror de los años 80.
3. Buscar todas las películas de terror de John Carpenter.
4. Buscar la primera película de terror de John Carpenter.
NO SE PUEDEN UTILIZAR COMPRENSIÓN DE LISTAS.
'''

peliculas = [
    ("Halloween", "John Carpenter", "Terror", 1978),
    ("La niebla", "John Carpenter", "Terror", 1980),
    ("Escape from New York", "John Carpenter", "Ciencia ficción", 1981),
    ("The Thing", "John Carpenter", "Terror / Ciencia ficción", 1982),
    ("Christine", "John Carpenter", "Terror", 1983),
    ("Starman", "John Carpenter", "Ciencia ficción / Romance", 1984),
    ("Golpe en la pequeña China", "John Carpenter", "Acción / Fantasía", 1986),
    ("Prince of Darkness", "John Carpenter", "Terror", 1987),
    ("They Live", "John Carpenter", "Ciencia ficción / Acción", 1988),
    ("Asalto a la comisaría del distrito 13", "John Carpenter", "Acción / Thriller", 1976),

    ("El resplandor", "Stanley Kubrick", "Terror", 1980),
    ("Viernes 13", "Sean S. Cunningham", "Terror", 1980),
    ("El hombre elefante", "David Lynch", "Drama", 1980),
    ("El exorcista II: El hereje", "John Boorman", "Terror", 1977),
    ("Alien, el octavo pasajero", "Ridley Scott", "Terror / Ciencia ficción", 1979),
    ("Aliens: El regreso", "James Cameron", "Ciencia ficción / Acción", 1986),
    ("Depredador", "John McTiernan", "Acción / Ciencia ficción", 1987),
    ("Terminator", "James Cameron", "Ciencia ficción / Acción", 1984),
    ("Terminator 2: El juicio final", "James Cameron", "Ciencia ficción / Acción", 1991),
    ("RoboCop", "Paul Verhoeven", "Ciencia ficción / Acción", 1987),

    ("Pesadilla en Elm Street", "Wes Craven", "Terror", 1984),
    ("Pesadilla en Elm Street 2: La venganza de Freddy", "Jack Sholder", "Terror", 1985),
    ("Pesadilla en Elm Street 3: Los guerreros del sueño", "Chuck Russell", "Terror", 1987),
    ("Pesadilla en Elm Street 4: El amo del sueño", "Renny Harlin", "Terror", 1988),
    ("Viernes 13 Parte 2", "Steve Miner", "Terror", 1981),
    ("Viernes 13 Parte 3", "Steve Miner", "Terror", 1982),
    ("Viernes 13: El capítulo final", "Joseph Zito", "Terror", 1984),
    ("Viernes 13 Parte VI: Jason vive", "Tom McLoughlin", "Terror", 1986),
    ("Viernes 13 Parte VII: Sangre nueva", "John Carl Buechler", "Terror", 1988),
    ("Viernes 13 Parte VIII: Jason toma Manhattan", "Rob Hedden", "Terror", 1989),

    ("Halloween II", "Rick Rosenthal", "Terror", 1981),
    ("Halloween III: El día de la bruja", "Tommy Lee Wallace", "Terror", 1982),
    ("Halloween 4: El regreso de Michael Myers", "Dwight H. Little", "Terror", 1988),
    ("Halloween 5: La venganza de Michael Myers", "Dominique Othenin-Girard", "Terror", 1989),
    ("La matanza de Texas", "Tobe Hooper", "Terror", 1974),
    ("Poltergeist", "Tobe Hooper", "Terror", 1982),
    ("Los chicos del maíz", "Fritz Kiersch", "Terror", 1984),
    ("Hellraiser", "Clive Barker", "Terror", 1987),
    ("Hellbound: Hellraiser II", "Tony Randel", "Terror", 1988),
    ("La mosca", "David Cronenberg", "Terror / Ciencia ficción", 1986),

    ("Videodrome", "David Cronenberg", "Terror / Ciencia ficción", 1983),
    ("La zona muerta", "David Cronenberg", "Terror / Thriller", 1983),
    ("Scanners", "David Cronenberg", "Terror / Ciencia ficción", 1981),
    ("Invasores de Marte", "Tobe Hooper", "Ciencia ficción / Terror", 1986),
    ("El retorno de los muertos vivientes", "Dan O'Bannon", "Terror / Comedia", 1985),
    ("Re-Animator", "Stuart Gordon", "Terror / Comedia", 1985),
    ("From Beyond", "Stuart Gordon", "Terror / Ciencia ficción", 1986),
    ("La noche de los demonios", "Kevin S. Tenney", "Terror", 1988),
    ("El príncipe de las tinieblas", "John Carpenter", "Terror", 1987),
    ("La cosa", "John Carpenter", "Terror / Ciencia ficción", 1982),

    ("Gremlins", "Joe Dante", "Terror / Comedia", 1984),
    ("Gremlins 2: La nueva generación", "Joe Dante", "Terror / Comedia", 1990),
    ("Un hombre lobo americano en Londres", "John Landis", "Terror / Comedia", 1981),
    ("Aullidos", "Joe Dante", "Terror", 1981),
    ("Noche de miedo", "Tom Holland", "Terror / Comedia", 1985),
    ("El terror llama a su puerta", "Fred Dekker", "Terror / Comedia", 1986),
    ("House: Una casa alucinante", "Steve Miner", "Terror / Comedia", 1986),
    ("House II: La casa de los horrores", "Ethan Wiley", "Terror / Comedia", 1987),
    ("El cementerio viviente", "Mary Lambert", "Terror", 1989),
    ("Muñeco diabólico", "Tom Holland", "Terror", 1988),

    ("La princesa prometida", "Rob Reiner", "Aventura / Fantasía", 1987),
    ("Los Goonies", "Richard Donner", "Aventura / Comedia", 1985),
    ("Regreso al futuro", "Robert Zemeckis", "Ciencia ficción / Comedia", 1985),
    ("Regreso al futuro II", "Robert Zemeckis", "Ciencia ficción / Comedia", 1989),
    ("E.T., el extraterrestre", "Steven Spielberg", "Ciencia ficción / Aventura", 1982),
    ("Indiana Jones y el templo maldito", "Steven Spielberg", "Aventura / Acción", 1984),
    ("Indiana Jones y la última cruzada", "Steven Spielberg", "Aventura / Acción", 1989),
    ("Los cazafantasmas", "Ivan Reitman", "Comedia / Fantasía", 1984),
    ("Los cazafantasmas II", "Ivan Reitman", "Comedia / Fantasía", 1989),
    ("Dentro del laberinto", "Jim Henson", "Fantasía / Aventura", 1986),

    ("El secreto de la pirámide", "Barry Levinson", "Aventura / Misterio", 1985),
    ("Willow", "Ron Howard", "Fantasía / Aventura", 1988),
    ("Conan el bárbaro", "John Milius", "Fantasía / Acción", 1982),
    ("Conan el destructor", "Richard Fleischer", "Fantasía / Acción", 1984),
    ("Highlander", "Russell Mulcahy", "Fantasía / Acción", 1986),
    ("Lady Halcón", "Richard Donner", "Fantasía / Aventura", 1985),
    ("Legend", "Ridley Scott", "Fantasía", 1985),
    ("Brazil", "Terry Gilliam", "Ciencia ficción / Comedia", 1985),
    ("Akira", "Katsuhiro Otomo", "Animación / Ciencia ficción", 1988),
    ("Nausicaä del Valle del Viento", "Hayao Miyazaki", "Animación / Fantasía", 1984),

    ("Blade Runner", "Ridley Scott", "Ciencia ficción / Thriller", 1982),
    ("Tron", "Steven Lisberger", "Ciencia ficción / Aventura", 1982),
    ("Dune", "David Lynch", "Ciencia ficción / Aventura", 1984),
    ("Mad Max 2: El guerrero de la carretera", "George Miller", "Acción / Ciencia ficción", 1981),
    ("Mad Max: Más allá de la cúpula del trueno", "George Miller", "Acción / Ciencia ficción", 1985),
    ("Robocop", "Paul Verhoeven", "Ciencia ficción / Acción", 1987),
    ("Desafío total", "Paul Verhoeven", "Ciencia ficción / Acción", 1990),
    ("El vuelo del navegante", "Randal Kleiser", "Ciencia ficción / Aventura", 1986),
    ("Cortocircuito", "John Badham", "Ciencia ficción / Comedia", 1986),
    ("Starman", "John Carpenter", "Ciencia ficción / Romance", 1984),

    ("Scarface", "Brian De Palma", "Crimen / Drama", 1983),
    ("Los intocables de Eliot Ness", "Brian De Palma", "Crimen / Drama", 1987),
    ("Platoon", "Oliver Stone", "Drama / Bélico", 1986),
    ("La chaqueta metálica", "Stanley Kubrick", "Drama / Bélico", 1987),
    ("Top Gun", "Tony Scott", "Acción / Drama", 1986),
    ("Arma letal", "Richard Donner", "Acción / Thriller", 1987),
    ("Jungla de cristal", "John McTiernan", "Acción / Thriller", 1988),
    ("Arma letal 2", "Richard Donner", "Acción / Thriller", 1989),
    ("Desaparecido en combate", "Joseph Zito", "Acción / Bélico", 1984),
    ("Rambo: Acorralado Parte II", "George P. Cosmatos", "Acción", 1985),

    ("El silencio de los corderos", "Jonathan Demme", "Thriller / Terror", 1991),
    ("El sexto sentido", "M. Night Shyamalan", "Terror / Thriller", 1999),
    ("Scream", "Wes Craven", "Terror / Thriller", 1996),
    ("Misery", "Rob Reiner", "Terror / Thriller", 1990),
    ("It", "Tommy Lee Wallace", "Terror", 1990),
    ("En la boca del miedo", "John Carpenter", "Terror", 1994),
]

# APARTADO 1
anyo_buscado = int(input('Introduce año:'))
genero_buscado = input('Introduce el género:')
print('*** APARTADO 1 - SOLUCION 1 ***')
for pelicula in peliculas:
    if pelicula[3]==anyo_buscado and genero_buscado in pelicula[2]:
        print(pelicula)

print('*** APARTADO 1 - SOLUCION 2 ***')
for titulo, director, genero, anyo in peliculas:
    if anyo==anyo_buscado and genero_buscado in genero:
        print(titulo, director, genero, anyo)

# APARTADO 2
print('*** APARTADO 2 ***')
for titulo, director, genero, anyo in peliculas:
    if anyo>1979 and anyo<1990 and 'Terror' in genero:
        print(titulo, director, genero, anyo)

# APARTADO 3
print('*** APARTADO 3 ***')
for titulo, director, genero, anyo in peliculas:
    if director=='John Carpenter' and 'Terror' in genero:
        print(titulo, director, genero, anyo)

# APARTADO 4
print('*** APARTADO 4 ***')
for titulo, director, genero, anyo in peliculas:
    if director=='John Carpenter' and 'Terror' in genero:
        print(titulo, director, genero, anyo)
        break
