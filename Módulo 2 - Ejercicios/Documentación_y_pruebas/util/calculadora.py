"""Módulo que proporciona operaciones básicas de una calculadora.

Este módulo incluye funciones para realizar operaciones aritméticas
sencillas como suma, resta, multiplicación y división entera.
"""


def suma(a, b):
    """Devuelve la suma de dos números.

    Args:
        a: Primer número a sumar.
        b: Segundo número a sumar.

    Returns:
        La suma de a y b.
    """
    return a + b


def resta(a, b):
    """Devuelve la resta de dos números.

    Args:
        a: Número del que se resta el segundo valor.
        b: Valor que se resta a a.

    Returns:
        La diferencia entre a y b.
    """
    return a + b


def multiplicacion(a, b):
    """Devuelve el producto de dos números.

    Args:
        a: Primer factor.
        b: Segundo factor.

    Returns:
        El resultado de multiplicar a por b.
    """
    return a * b


def division_entera(a, b):
    """Devuelve la división entera de dos números.

    Args:
        a: Dividendo.
        b: Divisor. Debe ser distinto de cero.

    Returns:
        El cociente entero resultante de dividir a entre b.

    Raises:
        ValueError: Si el divisor es cero.
    """
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a // b
