import json

COLOR_FONDO = 'COLOR_FONDO'
TITULO_VENTANA = 'TITULO_VENTANA'
ANCHO_VENTANA = 'ANCHO_VENTANA'
ALTO_VENTANA = 'ALTO_VENTANA'

color_fondo = input('Color del fondo:')
titulo_ventana = input('Título de la ventana:')
ancho_ventana = int(input('Ancho de la ventana:'))
alto_ventana = int(input('Alto de la ventana:'))

# parametros_configuracion = {}
parametros_configuracion = dict()

parametros_configuracion[COLOR_FONDO]=color_fondo
parametros_configuracion[TITULO_VENTANA]=titulo_ventana
parametros_configuracion[ANCHO_VENTANA]=ancho_ventana
parametros_configuracion[ALTO_VENTANA]=alto_ventana

with open('config_ventana.json', 'wt', encoding='utf-8') as fichero:
    json.dump(parametros_configuracion, fichero, ensure_ascii=False)