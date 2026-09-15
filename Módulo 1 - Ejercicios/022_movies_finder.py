import csv

peliculas = []
# peliculas = list() # Alternativa a la línea anterior
with open('movies.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        peliculas.append(row) # ['131231', 'Standby (2014)' , 'Comedy|Romance']
        #peliculas.append((int(row[0]),row[1][:-7],int(row[1][-5:-1]),row[2]))
    del peliculas[0]

# Pedir una palabra al usuario
# Buscar las películas cuyo título contiene esa palabra
