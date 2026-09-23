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

#Función 5
def obtener_maximo(*numeros) -> int:
    return max(numeros)

maximo = obtener_maximo(
    1, 30, 4, 8, 3, 5, 1, 7, 12, 25, 9, 16, 2, 18, 6, 11,
    22, 14, 29, 10, 15
)
print(f'Máximo:{maximo}')
