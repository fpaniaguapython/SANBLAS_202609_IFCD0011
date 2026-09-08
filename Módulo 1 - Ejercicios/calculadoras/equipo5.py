'''
Libreria para algunos calculos algebraicos y de áreas
'''

import math

def calcular_area_circulo( radius : float) -> float:
    """
    Calcula el área de un círculo a partir de su radio.

    Args:
        radius : Radio del círculo, expresado en metros.

    Returns:
        Área del círculo, expresada en metros cuadrados (m²).
    """

    return math.pi * radius**2
    

def calculate_suma(numero_1: int, numero_2: int) -> int:
    """
    Calcula la suma de dos números enteros.

    Args:
        numero_1: Primer número entero.
        numero_2: Segundo número entero.

    Returns:
        Resultado de sumar los dos números.
    """
    return numero_1 + numero_2
    

def multiplica_dos_entros(numero_1: int, numero_2: int) -> int:
    '''
    Calcula la multiplicación de dos números enteros
    
    Args:
        numero_1: Primer número entero.
        numero_2: Segundo número entero.

    Returns:
        Resultado de la multiplicación.

    '''
    return numero_1 * numero_2



def rectangle_area (base: float, altura:float):
    '''
    Calcula el area de un rectángulo (basándose en la base y la altura) 
    Args:
        base: lado más largo, en metros (óptimo para contexto agrario o de construcción)
        altura: lado más corto, en metros
    Returns:
        el área del rectángulo, en mts cuadrados
    '''

    area= base*altura
    return area
    