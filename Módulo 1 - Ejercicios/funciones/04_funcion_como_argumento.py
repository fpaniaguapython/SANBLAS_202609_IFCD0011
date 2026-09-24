import time

def retardador(funcion: function, retardo: int, *args, **kwargs) -> None:
    print('Durmiendo...')
    time.sleep(retardo)
    funcion(*args, **kwargs)

def saludar() -> None:
    print('Hola Python')

retardador(print, 5, 'Vamos', 'al', 'recreo', sep='*')


