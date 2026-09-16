import csv

peliculas = []
# peliculas = list() # Alternativa a la línea anterior
with open('movies.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader) # "Leer" la fila de los encabezados (se descarta)
    for row in reader:
        #peliculas.append(row) # ['131231', 'Standby (2014)' , 'Comedy|Romance']
        try:
            row[1]=row[1].strip() # Eliminamos los espacios en blanco del título
            peliculas.append((int(row[0]),row[1][:-7],int(row[1][-5:-1]),row[2].split('|')))
        except:
            print(f'Error en {row}')

# Pedir una palabra al usuario
# Buscar las películas cuyo título contiene esa palabra

palabra_buscada = input('Introduce una palabra:')
for pelicula in peliculas:
    if (palabra_buscada.casefold() in pelicula[1].casefold()):
        print(pelicula)
