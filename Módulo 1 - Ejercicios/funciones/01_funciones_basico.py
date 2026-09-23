# SIN ARGUMENTOS, SIN RETORNO
def escribir_saludo() -> None:
    print('Hola')

# SIN ARGUMENTOS, CON RETORNO
def generar_saludo() -> str:
    return 'Hola'

# CON ARGUMENTOS Y CON RETORNO
def saludar(nombre: str) -> str:
    return f'Hola {nombre}'

# CON ARGUMENTOS Y SIN RETORNO
def saludar_a_persona(nombre: str) -> None:
    print(f'Hola {nombre}')