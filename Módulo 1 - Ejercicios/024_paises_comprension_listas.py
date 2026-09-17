# Lista de países con (Nombre, Población, PIB en €, Superficie en km²)
paises_eur = [
    ("España", 48000000, 1472000000000, 505990),
    ("México", 128500000, 1343200000000, 1964375),
    ("Estados Unidos", 335000000, 25760000000000, 9833520),
    ("China", 1410000000, 16560000000000, 9596961),
    ("Japón", 124500000, 3864000000000, 377975),
    ("Brasil", 215000000, 1978000000000, 8515767),
    ("Alemania", 84400000, 4048000000000, 357022),
    ("India", 1430000000, 3496000000000, 3287263),
    ("Francia", 68000000, 2760000000000, 551695),
    ("Argentina", 46200000, 588800000000, 2780400)
]
# Crear una nueva Lista en la que aparezcan:
# Nombre del país
# Densidad de Habitantes por km^2
# PIB/habitante

paises = [(pais[0], round(pais[1]/pais[3],1), int(pais[2]/pais[1])) 
          for pais in paises_eur]
print(paises)

paises_densos = [(pais[0], round(pais[1]/pais[3],1), int(pais[2]/pais[1])) 
          for pais in paises_eur if round(pais[1]/pais[3],1)>100]
print(paises_densos)

paises_todos = [(pais[0], round(pais[1]/pais[3],1), int(pais[2]/pais[1])) 
                if round(pais[1]/pais[3],1)>100 else (pais[0],'DESPOBLADO', int(pais[2]/pais[1]))
                for pais in paises_eur]
print(paises_todos)