import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ANCHO = 250
ALTO = 300
DIMENSIONES = f'{ANCHO}x{ALTO}'

def sumar():
    try:
        numero_1 = int(entry_primer_numero.get())
        numero_2 = int(entry_segundo_numero.get())
        resultado = numero_1+numero_2
        messagebox.showinfo('Suma',f'{numero_1}+{numero_2}={resultado}')
    except:
        messagebox.showerror('Suma', 'Has introducido valores erróneos')

def restar():
    numero_1 = int(entry_primer_numero.get())
    numero_2 = int(entry_segundo_numero.get())
    resultado = numero_1-numero_2
    messagebox.showinfo('Resta',f'{numero_1}-{numero_2}={resultado}')

def multiplicar():
    numero_1 = int(entry_primer_numero.get())
    numero_2 = int(entry_segundo_numero.get())
    resultado = numero_1*numero_2
    messagebox.showinfo('Multiplicación',f'{numero_1}x{numero_2}={resultado}')

def dividir():
    numero_1 = int(entry_primer_numero.get())
    numero_2 = int(entry_segundo_numero.get())
    resultado = numero_1/numero_2
    messagebox.showinfo('División',f'{numero_1}/{numero_2}={resultado}')
   

# Creación de la ventana principal
main_window=tk.Tk()

# Configuración de la ventana principal
main_window.title('Calculadora 1.0')
main_window.geometry(DIMENSIONES)
main_window.resizable(False, False)
main_window.config(bg='white')

# Widgets
# Labels
label_primer_numero = ttk.Label(
    main_window, 
    text='Primer número', 
    background='white')
label_primer_numero.place(x=20,y=20)

entry_primer_numero = ttk.Entry(
    main_window, 
    justify=tk.RIGHT,
    font=("Arial", 20))
entry_primer_numero.place(x=20,y=40, width=210, height=40)

label_segundo_numero = ttk.Label(
    main_window, 
    text='Segundo número', 
    background='white')
label_segundo_numero.place(x=20,y=90)

entry_segundo_numero = ttk.Entry(
    main_window, 
    justify=tk.RIGHT,
    font=("Arial", 20))
entry_segundo_numero.place(x=20,y=110, width=210, height=40)

boton_sumar = tk.Button(main_window, text='+SUMAR', command=sumar, bg="#7651AE", fg='white')
boton_sumar.place(x=20,y=160, width=100, height=40)

boton_restar = tk.Button(main_window, text='-RESTAR', command=restar, bg="#7651AE", fg='white')
boton_restar.place(x=130,y=160, width=100, height=40)

boton_multiplicar = tk.Button(main_window, text='+MULTIPLICAR', command=multiplicar, bg="#7651AE", fg='white')
boton_multiplicar.place(x=20,y=220, width=100, height=40)

boton_dividir = tk.Button(main_window, text='-DIVIDIR', command=dividir, bg="#7651AE", fg='white')
boton_dividir.place(x=130,y=220, width=100, height=40)

main_window.mainloop()