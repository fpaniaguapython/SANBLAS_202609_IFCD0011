'''
Solicitar al usuario:
Nombre
Año de nacimiento
Año actual

Indicar si está en edad de jubilación (>=67)
Si no, indicar cuántos años le quedan para la jubilación
'''
EDAD_JUBILACION = 67

nombre = input('Introduce tu nombre:')
anyo_nacimiento = int(input('Introduce el año de nacimiento:'))
anyo_actual = int(input('Introduce el año actual:'))

edad = anyo_actual - anyo_nacimiento

if (edad>=EDAD_JUBILACION):
    print('Jubilación permitida')
else:
    anyos_pendientes = EDAD_JUBILACION - edad
    print('Te quedan', anyos_pendientes, 'años para jubilarte')
    print(f'Te quedan {anyos_pendientes} para jubilarte')
    # Te quedan 10 años para jubilarte
