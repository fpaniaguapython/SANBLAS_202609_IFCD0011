import tkinter as tk

ANCHO = 800
ALTO = 600
ANCHO_MINIMO = 640
ALTO_MINIMO = 480
DIMENSIONES = f'{ANCHO}x{ALTO}'

def saludar():
    texto = entry_email.get()
    print('Hola',texto)

# Creación de la ventana principal
main_window=tk.Tk()

# Configuración de la ventana principal
main_window.title('Calculadora 1.0')
main_window.geometry(DIMENSIONES)
main_window.minsize(ANCHO_MINIMO, ALTO_MINIMO)

# Widgets
entry_email = tk.Entry(main_window, width=20)
entry_email.place(x=20,y=20)

boton_aceptar = tk.Button(main_window, text='Saludar', command=saludar)
boton_aceptar.place(x=100,y=20)


main_window.mainloop()