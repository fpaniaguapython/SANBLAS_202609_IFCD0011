import json

COLOR_FONDO = 'COLOR_FONDO'
COLOR_TEXTO = 'COLOR_TEXTO'
FONT_SIZE = 'FONT_SIZE'
IDIOMA = 'IDIOMA'
VOLUMEN = 'VOLUMEN'

color_fondo = input('Color del fondo:')
color_texto = input('Color del texto:')
font_size = int(input('Tamaño del texto:'))
idioma = input('Idioma:')
volumen = int(input('Volumen:'))

# parametros_configuracion = {}
parametros_configuracion = dict()

parametros_configuracion[COLOR_FONDO]=color_fondo
parametros_configuracion[COLOR_TEXTO]=color_texto
parametros_configuracion[FONT_SIZE]=font_size
parametros_configuracion[IDIOMA]=idioma
parametros_configuracion[VOLUMEN]=volumen

print(parametros_configuracion)

with open('config.json', 'wt', encoding='utf-8') as fichero:
    json.dump(parametros_configuracion, fichero, ensure_ascii=False)