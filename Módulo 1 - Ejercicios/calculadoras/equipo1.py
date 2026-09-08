'''
bla, bla, bla
'''
def calcular_area_circunferencia(radio: float): 
    '''
    Calcula el area de una circunferencia

    Params:
    - radio : Radio de la circunferencia
    
    Return:
    - Area de la circunferencia
    '''          
    PI = 3.14
    area = PI*(radio*radio) 
    
    return area


def multiplicacion_enteros(numero_1 : int, numero_2 : int): 
    '''
    Calcula la multiplicacion de dos numeros enteros

    Params:
    - numero_1:El primer número a multiplicar
    - numero_2:El segundo número a multiplicar
    
    Return:
    - Resultado de la multiplicacion
    '''  
    resultado=numero_1*numero_2
    return resultado
        
def suma_enteros(num1, num2) -> int:
    '''
    Devuelve la suma de dos números enteros.

    params:
    - num1: Primer sumando
    - num2: Segundo sumando
    '''
    suma = num1 + num2
    return suma

def calcular_area_rectangulo(base: float, altura: float) -> float:
    '''
    Devuelve el área de un rectángulo.

    params:
    - base: Es la longitud de la base del rectángulo
    - altura: Es la longitud de la altura del rectángulo

    return:
    - Área del rectángulo
    '''
    
    area = base * altura
    
    return area
  