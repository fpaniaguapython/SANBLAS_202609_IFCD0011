import tkinter as tk
from tkinter import ttk
import sys

def funcion_aceptar():
    print('Aceptando...')

def funcion_cancelar():
    print('Cancelando...')


ANCHO = 800
ALTO = 600
ANCHO_MINIMO = 640
ALTO_MINIMO = 480
DIMENSIONES = f'{ANCHO}x{ALTO}'

# Creación de la ventana principal
main_window=tk.Tk()

# Configuración de la ventana principal
main_window.title('Gestor alarmas v1.0')
main_window.geometry(DIMENSIONES)
main_window.minsize(ANCHO_MINIMO, ALTO_MINIMO)
# main_window.maxsize(ANCHO_MAXIMO, ALTO_MAXIMO)
# main_window.resizable(False, False) # Bloque las dimensiones


# Widgets
boton_aceptar = tk.Button(main_window, text='Aceptar', command=funcion_aceptar)
boton_cancelar = ttk.Button(main_window, text='Cancelar', command=lambda: sys.exit(0))
boton_aceptar.place(x=100,y=100,width=80,height=50)
boton_cancelar.place(x=200,y=100,width=80,height=50)

# Inicio del bucle principal
main_window.mainloop()