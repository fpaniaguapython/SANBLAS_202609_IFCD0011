import json
import _32_contantes

color_fondo = input('Color del fondo:')
titulo_ventana = input('Título de la ventana:')
ancho_ventana = int(input('Ancho de la ventana:'))
alto_ventana = int(input('Alto de la ventana:'))

# parametros_configuracion = {}
parametros_configuracion = dict()

parametros_configuracion[_32_contantes.COLOR_FONDO]=color_fondo
parametros_configuracion[_32_contantes.TITULO_VENTANA]=titulo_ventana
parametros_configuracion[_32_contantes.ANCHO_VENTANA]=ancho_ventana
parametros_configuracion[_32_contantes.ALTO_VENTANA]=alto_ventana

with open('config_ventana.json', 'wt', encoding='utf-8') as fichero:
    json.dump(parametros_configuracion, fichero, ensure_ascii=False)