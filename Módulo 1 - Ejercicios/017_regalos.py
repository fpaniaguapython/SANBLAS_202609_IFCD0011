
'''
Pedir al usuario que introduzca un regalo
hasta que acierte con alguno de los que quiere
el del cumpleaños.
'''
regalos = ['PS5', 'FERRARI', 'RANCHO']
regalo_acertado = input('Di un regalo:').upper()
while regalo_acertado not in regalos:
    print('No es el regalo correcto')
    regalo_acertado = input('Di un regalo:').upper()
print('Regalo válido')
