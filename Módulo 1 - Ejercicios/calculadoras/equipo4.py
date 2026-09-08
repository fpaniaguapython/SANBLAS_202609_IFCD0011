'''
Este módulo contiene: 
- una funcion que suma dos numeros enteros
- una funcion que multiplica dos numeros enteros
- una función que calcula el área de un rectángulo
- una funcion que calcula el área de una circunferencia 
'''
def sumar(sumando_1: int, sumando_2: int) -> int:
    '''
    Funciòn para la suma de 2 nùmeros enteros

    Parametros:
        sumando_1:  Primer número entero.
        sumando_2:  Segundo número entero.
    
    Return:
        dato:   La suma de los 2 nùmero enteros
    '''
    dato = sumando_1 + sumando_2
    return dato

def multiplicar (a: int,b: int) -> int:
    '''
    Función para la multiplicaciòn de 2 número enteros
    
    Parametros:
        a:  Primer número entero
        b:  Segundo número entero
    
    Return:
        dato: Resultado de la multiplicaciòn
    '''
    dato = a * b
    return dato
    

def calcular_area_rectangulo(base: float, altura: float) -> float:
    '''
    Funciòn que calula el area de un rectangulo

    Parametros:
        base:   Longitud de la base expresada en metros
        altura: Longitud de la altura expresada en metros

    Return:
        El area del rectangulo

    Enlaces:
        https://www.superprof.es/diccionario/matematicas/geometria/area-rectangulo.html

    '''
    area_rectangulo = base * altura
    return area_rectangulo

def calcular_area_circunferencia(radio: float) ->float:
    '''
    Funciòn para el area de una circunferencia

    Parametros:
        radio:  radio de la circunferencia expresado en metros

    Return:
        Devuelve el area de la circunferencia

    Enlaces:
         https://www.sangakoo.com/es/temas/area-y-perimetro-de-una-circunferencia

    '''
    PI = 3.1415
    area_circunferencia = PI*radio**2
    return area_circunferencia