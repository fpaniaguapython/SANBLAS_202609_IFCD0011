import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ANCHO = 250
ALTO = 300
DIMENSIONES = f'{ANCHO}x{ALTO}'

def ampliar(evento):
    el_boton.place(x=20,y=20,width=200, height=200)
   

def reducir(evento):
    el_boton.place(x=20,y=20,width=100, height=100)

# Creación de la ventana principal
main_window=tk.Tk()

# Configuración de la ventana principal
main_window.title('Eventos')
main_window.geometry(DIMENSIONES)
main_window.resizable(False, False)
main_window.config(bg='white')

el_boton = tk.Button(
    main_window, 
    text='Soy un botón', 
    bg="#7651AE", 
    fg='white',
    cursor='heart')
el_boton.place(x=20,y=20, width=100, height=100)
el_boton.bind("<Enter>",ampliar)
el_boton.bind("<Leave>",reducir)

main_window.mainloop()