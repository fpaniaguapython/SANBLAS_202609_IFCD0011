'''
Pedir dos números al usuario.
Hay que calcular la suma, la resta y
la división.

Capturar y tratar los errores de conversión.
Cuando se divide entre 0 se produce un 
error. Hay que capturarlo y tratarlo.
'''
try:
    numero_1 = int(input('Número 1:'))
    numero_2 = int(input('Número 2:'))
    suma = numero_1 + numero_2
    print(f'La suma es {suma}')
    resta = numero_1 - numero_2
    print(f'La resta es {resta}')
    division = numero_1 / numero_2
    print(f'La division es {division}')
except ValueError:
    print('Has introducido mal los números')
except ZeroDivisionError:
    print('No se puede dividir entre 0')