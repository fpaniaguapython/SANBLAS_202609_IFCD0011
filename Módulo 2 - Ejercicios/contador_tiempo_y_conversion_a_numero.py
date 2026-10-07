import random
import time

from text_to_num import text2num, alpha2digit

numero_conversiones = int(input('Introduce el número de conversiones:'))
lista = ('ocho', 'quince', 'mil doscientos', 'cincuenta millones', 'joseluis')

inicio = time.perf_counter()

for i in range(numero_conversiones):
    try:
        entrada = random.choice(lista)
        # numero = alpha2digit(entrada, "es")
        numero = text2num(entrada, 'es')
        #print(type(numero))
        #print(numero)
    except ValueError as ve:
        print(f'Ha ocurrido un error al convertir {entrada}')

fin = time.perf_counter()

print(f"Tiempo: {fin - inicio:.6f} segundos")