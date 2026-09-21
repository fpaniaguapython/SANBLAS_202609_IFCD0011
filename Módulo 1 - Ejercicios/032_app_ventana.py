import tkinter as tk # Importación de tkinter
import json

COLOR_FONDO = 'COLOR_FONDO'
TITULO_VENTANA = 'TITULO_VENTANA'
ANCHO_VENTANA = 'ANCHO_VENTANA'
ALTO_VENTANA = 'ALTO_VENTANA'

with open('config_ventana.json', mode='rt', encoding='utf-8') as fichero:
    configuracion = json.load(fichero)

main_window=tk.Tk() # Creación de un objeto de la clase Tk

main_window.title(configuracion[TITULO_VENTANA])
main_window.geometry('800x400')
main_window.configure(bg=configuracion[COLOR_FONDO])

main_window.mainloop() # Pone en bucle infinito la aplicación