import tkinter as tk
from tkinter import messagebox


# ---------------- FUNCIONES ----------------

def calcular(operacion):
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())

        if operacion == "+":
            resultado = numero1 + numero2
            simbolo = "+"

        elif operacion == "-":
            resultado = numero1 - numero2
            simbolo = "−"

        elif operacion == "×":
            resultado = numero1 * numero2
            simbolo = "×"

        elif operacion == "÷":
            if numero2 == 0:
                messagebox.showerror(
                    "Error",
                    "No se puede dividir entre cero.",
                    parent=ventana
                )
                return

            resultado = numero1 / numero2
            simbolo = "÷"

        mostrar_resultado(numero1, numero2, simbolo, resultado)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Introduce dos números válidos.",
            parent=ventana
        )


def mostrar_resultado(numero1, numero2, simbolo, resultado):
    # Crear ventana flotante
    ventana_resultado = tk.Toplevel(ventana)

    ventana_resultado.title("Resultado")
    ventana_resultado.geometry("360x260")
    ventana_resultado.resizable(False, False)

    ventana_resultado.configure(bg="#FCEEF2")

    # Hacer que aparezca delante de la calculadora
    ventana_resultado.transient(ventana)
    ventana_resultado.grab_set()

    # Centrar la ventana
    ventana.update_idletasks()

    x = ventana.winfo_x() + (ventana.winfo_width() // 2) - 180
    y = ventana.winfo_y() + (ventana.winfo_height() // 2) - 130

    ventana_resultado.geometry(f"360x260+{x}+{y}")

    # ---------------- CONTENIDO ----------------

    tk.Label(
        ventana_resultado,
        text="✨ Resultado ✨",
        font=("Arial", 22, "bold"),
        bg="#FCEEF2",
        fg="#5B566B"
    ).pack(pady=(25, 10))

    # Operación realizada
    tk.Label(
        ventana_resultado,
        text=f"{numero1:g}  {simbolo}  {numero2:g}",
        font=("Arial", 15),
        bg="#FCEEF2",
        fg="#8A8495"
    ).pack(pady=5)

    # Resultado grande
    tk.Label(
        ventana_resultado,
        text=f"{resultado:g}",
        font=("Arial", 32, "bold"),
        bg="#FFFDFD",
        fg="#5B566B",
        width=12,
        pady=12
    ).pack(pady=10)

    # Botón cerrar
    tk.Button(
        ventana_resultado,
        text="Cerrar",
        font=("Arial", 11, "bold"),
        bg="#DCCEF3",
        fg="#5B566B",
        activebackground="#DCCEF3",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=ventana_resultado.destroy
    ).pack(
        ipadx=20,
        ipady=5,
        pady=5
    )


# ---------------- VENTANA PRINCIPAL ----------------

ventana = tk.Tk()

ventana.title("Calculadora Pastel")
ventana.geometry("420x520")
ventana.resizable(False, False)
ventana.configure(bg="#FCEEF2")


# ---------------- COLORES ----------------

BLANCO = "#FFFDFD"
TEXTO = "#5B566B"

VERDE = "#BFE8D4"
ROSA = "#F5C6D6"
AZUL = "#C7E6F5"
LILA = "#DCCEF3"


# ---------------- CONTENEDOR ----------------

contenedor = tk.Frame(
    ventana,
    bg=BLANCO,
    padx=30,
    pady=30
)

contenedor.pack(
    padx=25,
    pady=25,
    fill="both",
    expand=True
)


# ---------------- TÍTULO ----------------

tk.Label(
    contenedor,
    text="Calculadora",
    font=("Arial", 26, "bold"),
    bg=BLANCO,
    fg=TEXTO
).pack(pady=(0, 5))


tk.Label(
    contenedor,
    text="Calcula fácilmente 🐈",
    font=("Arial", 11),
    bg=BLANCO,
    fg="#9993A3"
).pack(pady=(0, 25))


# ---------------- PRIMER NÚMERO ----------------

tk.Label(
    contenedor,
    text="Primer número",
    font=("Arial", 11, "bold"),
    bg=BLANCO,
    fg=TEXTO
).pack(anchor="w")

entrada1 = tk.Entry(
    contenedor,
    font=("Arial", 16),
    justify="center",
    bg="#EDF7F8",
    fg=TEXTO,
    relief="flat"
)

entrada1.pack(
    fill="x",
    ipady=10,
    pady=(5, 15)
)


# ---------------- SEGUNDO NÚMERO ----------------

tk.Label(
    contenedor,
    text="Segundo número",
    font=("Arial", 11, "bold"),
    bg=BLANCO,
    fg=TEXTO
).pack(anchor="w")

entrada2 = tk.Entry(
    contenedor,
    font=("Arial", 16),
    justify="center",
    bg="#EDF7F8",
    fg=TEXTO,
    relief="flat"
)

entrada2.pack(
    fill="x",
    ipady=10,
    pady=(5, 25)
)


# ---------------- BOTONES ----------------

frame_botones = tk.Frame(
    contenedor,
    bg=BLANCO
)

frame_botones.pack(fill="x")


botones = [
    ("+", VERDE, "+"),
    ("−", ROSA, "-"),
    ("×", AZUL, "×"),
    ("÷", LILA, "÷")
]


for columna, (texto, color, operacion) in enumerate(botones):

    boton = tk.Button(
        frame_botones,
        text=texto,
        font=("Arial", 22, "bold"),
        bg=color,
        fg=TEXTO,
        activebackground=color,
        activeforeground=TEXTO,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda op=operacion: calcular(op)
    )

    boton.grid(
        row=0,
        column=columna,
        padx=4,
        pady=5,
        ipadx=8,
        ipady=8,
        sticky="nsew"
    )

    frame_botones.columnconfigure(
        columna,
        weight=1
    )


# ---------------- INICIO ----------------

entrada1.focus()

ventana.mainloop()