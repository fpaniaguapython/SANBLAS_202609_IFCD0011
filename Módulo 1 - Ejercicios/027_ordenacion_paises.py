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

# 1. Ordenar la lista por la superficie en orden descendente
def cuantificar_superficie(tupla_pais : tuple) -> int:
    return tupla_pais[3]    

paises_eur.sort(key=cuantificar_superficie, reverse=True)
for pais in paises_eur:
    print(pais)

print('*'*50)

# 2. Ordenar por densidad de población (habitantes por km²) ascendente
def cuantificar_densidad(tupla_pais : tuple) -> int:
    return tupla_pais[1]/tupla_pais[3]

paises_eur.sort(key=cuantificar_densidad)
for pais in paises_eur:
    print(pais)
