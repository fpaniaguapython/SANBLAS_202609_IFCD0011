# Una función que sume dos enteros (comprobando que son dos enteros)
# Hay que usar la función isinstance

def sumar(sumando_1: int, sumando_2: int) -> int:
    if isinstance(sumando_1, int) and isinstance(sumando_2, int):
        return sumando_1+sumando_2
    else:
        raise TypeError('Los tipos de los argumentos no son enteros')


try:
    resultado = sumar('1','2')
    print(resultado)
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
except (FloatingPointError, ZeroDivisionError) as ae:
    print(ae)
except BaseException as be:
    print(be)
        