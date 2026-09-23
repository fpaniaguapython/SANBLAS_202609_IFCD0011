try:
    edad = int(input('Edad:'))
    print(edad)
except ValueError as ve:
    print(ve)
except KeyboardInterrupt as ki:
    print('Ha pulsado ctrl+c')
except BaseException as be:
    print('Ha ocurrido un error inesperado', be)
print('Seguimos...')