# Instalación: pip install requests
# Documentación de requests: https://requests.readthedocs.io/en/latest/

import requests

URL_DATA_FILE = 'https://fpaniaguapython.github.io/datos/encuesta_poblacion.csv'

def guardar_fichero(contenido : str, nombre_fichero='pepito.csv') -> None:
    with open(nombre_fichero, mode='wt', encoding='utf-8') as fichero:
        fichero.write(contenido)

respuesta = requests.get(URL_DATA_FILE)

codigo_status = respuesta.status_code

if codigo_status==200:
    datos = respuesta.text
    guardar_fichero(datos, 'encuesta.csv')
else:
    print('No se ha podido atender la petición:', codigo_status)

print('FIN')



