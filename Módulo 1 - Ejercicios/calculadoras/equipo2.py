'''
Módulo de funciones aritméticas y de área
  
- suma_enteros( num_1: int, num_2: int)
- multiplica_enteros( num_1: int, num_2: int)
- area_cuadrado (lado : float)
- calcula_area_circunferencia(radio: float)
'''
import math

def suma_enteros( num_1: int, num_2: int) -> int:
    '''
    Suma dos numeros enteros

    Params:
        - num_1: un entero
        - num_2: otro entero
    Return:
        - Devuelve la suma de num1 y num2
    '''
    return num_1+num_2

def multiplica_enteros( num_1: int, num_2: int) -> int:
    '''
    Multiplicación dos numeros enteros
    
    Params:
       - num_1: un entero
       - num_2: otro entero
    Return:
       - Devuelve la multiplicación de num1 y num2
    '''
    return num_1*num_2


def area_cuadrado (lado : float) -> float:
    '''
    Cálculo del área de un cuadrado indicando el valor en cms de su lado    
    
    Params:
    - Lado: Centímetros del cuadrado
    
    Return:
    - Devuelve el valor del área del cuadrado
    '''
    return lado * lado


def calcula_area_circunferencia(radio: float)-> float:
    '''
    Calcula el área de la circunferencia

    Params:
        radio: radio en metros        
    Return:
        Devuelve el área de la circunferencia
    '''
    
    area = math.pi * radio **2
    return area