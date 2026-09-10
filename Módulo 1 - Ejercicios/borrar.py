if len(contrasenya)<LONGITUD_MINIMA or len(contrasenya)>LONGITUD_MAXIMA or not contrasenya.isalpha():
        return False