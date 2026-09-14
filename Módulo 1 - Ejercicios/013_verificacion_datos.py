# nivel_ingles: BAJO, MEDIO o ALTO
def comprobar_datos(nombre : str, edad : int, nivel_ingles : str, 
                    tiene_auto : bool):
    '''
    Devuelve True si es mayor de edad, tiene menos de 67 años,
    el nivel de inglés es 'MEDIO' o 'ALTO'
    y tiene auto (coche, moto, bici...)
    '''
    EDAD_MINIMA = 18
    EDAD_MAXIMA = 67
    if edad<EDAD_MINIMA or edad>=EDAD_MAXIMA:
        return False

    # Versión Fernando
    if nivel_ingles=='BAJO':
        return False

    # Versión Jose
    # niveles_aceptados = ('MEDIO','ALTO')
    # if nivel_ingles not in niveles_aceptados:
    #     return False

    if tiene_auto==False:
        return False

    return True

resultado = comprobar_datos('Gema', 25, 'ALTO', True)
print(resultado)