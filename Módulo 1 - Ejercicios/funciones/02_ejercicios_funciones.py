'''
1. Función que muestra por pantalla la cadena 'HOLA, PYTHON'
2. Función que suma dos números enteros y devuelve el resultado.
3. Función que recibe un diccionario y lo guarda en un fichero json.
4. Función que recibe un nombre de fichero y devuelve el contenido.
5. Función que recibe 1000 números y devuelve el valor máximo.
(TIENE TRAMPA)
6. Función que suma dos números enteros y devuelve el resultado.
El segundo número tiene el valor por defecto de 10.
7. Función que calcula el área de una circunferencia.
8. Función que calcula el área de un rectángulo.
'''
import json
from math import pi

# Función 1
def mostrar_saludo() -> None:
    print('HOLA, PYTHON')

# Función 2
def sumar_enteros(numero_1: int, numero_2:int) -> int:
    resultado = numero_1+numero_2
    return resultado

# Función 3
def guardar_diccionario_en_fichero_json(
        diccionario: dict, nombre_fichero: str) -> None:
    with open(nombre_fichero, mode='wt', encoding='utf-8') as fichero:
        json.dump(diccionario, fichero, ensure_ascii=False, indent=2)

# Función 4
def leer_fichero(nombre_fichero: str) -> str:
    with open(nombre_fichero, mode='rt', encoding='utf-8') as fichero:
        contenido = fichero.read()
    return contenido

# Función 5
def obtener_maximo(*numeros) -> int:
    return max(numeros)

# Función 6
def sumar_enteros_con_defecto(numero_1: int, numero_2: int=10) -> int:
    resultado = numero_1+numero_2
    return resultado

# Función 7
def calcular_area_circunferencia(radio: float) -> float:
    area = pi * (radio**2)
    return area

# Función 8
def calcular_area_rectangulo(base: float, altura: float) -> float:
    area = base * altura
    return area

# Ejecución Función 3
diccionario = {'Hola':'Hello','Pan':'Bread','Agua':'Water'}
guardar_diccionario_en_fichero_json(diccionario, 'es-en.json')

# Ejecución Función 4
try:
    datos = leer_fichero('02_ejercicios_funciones.pxy')
    print(datos)
except FileNotFoundError:
    print('El fichero no existe')


# Ejecución Función 5
maximo = obtener_maximo(
    1, 30, 4, 8, 3, 5, 1, 7, 12, 25, 9, 16, 2, 18, 6, 11,
    22, 14, 29, 10, 15
)
print(f'Máximo:{maximo}')
