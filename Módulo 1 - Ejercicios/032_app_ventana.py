import tkinter as tk # Importación de tkinter
import json
import _32_contantes

with open('config_ventana.json', mode='rt', encoding='utf-8') as fichero:
    configuracion = json.load(fichero)

main_window=tk.Tk() # Creación de un objeto de la clase Tk

main_window.title(configuracion[_32_contantes.TITULO_VENTANA])
main_window.geometry(f'{configuracion[_32_contantes.ANCHO_VENTANA]}x{configuracion[_32_contantes.ALTO_VENTANA]}')
main_window.configure(bg=configuracion[_32_contantes.COLOR_FONDO])

main_window.mainloop() # Pone en bucle infinito la aplicación