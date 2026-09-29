# Un función que sume dos números enteros que sean pares
# Hay que usar la función isinstance y lanzar una excepción propia
class ImparError(ValueError):
    pass

def sumar(sumando_1: int, sumando_2: int) -> int:
    if sumando_1%2==0 and sumando_2%2==0:
        return sumando_1+sumando_2
    else:
        raise ImparError('Alguno de los sumandos es impar')

try:
    resultado = sumar(4,9)
    print(resultado)
except ImparError as te:
    print(te)
        