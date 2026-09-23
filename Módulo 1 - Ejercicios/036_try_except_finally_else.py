try:
    edad = int(input('Introduce tu edad:'))
    print(edad)
except ValueError as ve:
    print('HAS INTRODUCIDO UNA EDAD NO VÁLIDA')
else:
    print('ESTO SE EJECUTA SI NO HA HABIDO ERROR')
finally:
    print('ESTO SE EJECUTA SIEMPRE, CON ERROR Y SIN ERROR')

