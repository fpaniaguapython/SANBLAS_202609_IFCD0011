def sumar(sumando_1: int, sumando_2: int) -> int:
    if (not isinstance(sumando_1, int) 
        or not isinstance(sumando_2, int)):
        raise TypeError('No es entero')
    # A partir de aquí, se resuelve el problema
    resultado = sumando_1 + sumando_2
    return resultado

r = sumar('10','8')
print(r)