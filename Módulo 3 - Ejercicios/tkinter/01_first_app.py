import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def salir():
    salir = messagebox.askquestion("Salir", "¿Estás seguro?")
    #if salir == 'yes':
    if salir == messagebox.YES:
        main_window.destroy()


def funcion_aceptar():
    print('Aceptando...')

def funcion_cancelar():
    print('Cancelando...')


ANCHO = 800
ALTO = 600
ANCHO_MINIMO = 640
ALTO_MINIMO = 480
DIMENSIONES = f'{ANCHO}x{ALTO}'

BASIC_BUTTON_BG = 'gray'
BASIC_BUTTON_FG = 'white'

# Creación de la ventana principal
main_window=tk.Tk()

# Configuración de la ventana principal
main_window.title('Gestor alarmas v1.0')
main_window.geometry(DIMENSIONES)
main_window.minsize(ANCHO_MINIMO, ALTO_MINIMO)
# main_window.maxsize(ANCHO_MAXIMO, ALTO_MAXIMO)
# main_window.resizable(False, False) # Bloque las dimensiones


# Widgets
boton_aceptar = tk.Button(
    main_window, 
    text='Aceptar', 
    command=funcion_aceptar,
    bg=BASIC_BUTTON_BG,
    fg=BASIC_BUTTON_FG)
boton_cancelar = ttk.Button(main_window, text='Cancelar', command=salir)
boton_aceptar.place(x=100,y=100,width=80,height=50)
boton_cancelar.place(x=200,y=100,width=80,height=50)

entry=tk.Entry(main_window, width=30)
entry.place(x=300,y=100)

# Inicio del bucle principal
main_window.mainloop()