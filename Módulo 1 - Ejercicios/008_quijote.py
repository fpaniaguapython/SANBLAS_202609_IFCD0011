# find --> Proporciona la primera posición de una subcadena o -1
# index --> Proporciona la primera posición de una subadena o error
# count --> Indica cuantas veces aparece la subcadena 
import re

with open('el_quijote.txt', mode='rt', encoding='utf-8') as fichero:
    texto = fichero.read()

palabra = input('Introduce una palabra:')

# ¿Existe la palabra?
# ¿Cuántas veces se usa la palabra?
# numero_ocurrencias = texto.upper().count(palabra.upper()) # 91
ocurrencias = re.findall(rf"\b{palabra}\b", texto, re.IGNORECASE) 
numero_ocurrencias = len(ocurrencias) # 90
print(f'He encontrado {numero_ocurrencias} veces {palabra}')
