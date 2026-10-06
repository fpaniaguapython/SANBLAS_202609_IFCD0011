"""Aplicación principal del proyecto.

Este módulo contiene la función principal de la aplicación y muestra
un ejemplo de uso de la suma del módulo calculadora.
"""

from util.calculadora import suma


def main():
    """Ejecuta la aplicación principal.

    Returns:
        None: Muestra el resultado de la suma en la consola.
    """
    resultado = suma(5, 3)
    print(f"La suma es: {resultado}")


if __name__ == "__main__":
    main()
