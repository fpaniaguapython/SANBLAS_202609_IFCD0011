'''
1. Verificar que el identificador de usuario es correcto.
- El identificador de usuario es una dirección de correo válida.
2. Verificar que la contraseña es válida:
- Longitud mínima 6 caracteres.
- Longitud máxima 15 caracteres.
- Sólo puede contener caracteres alfabéticos (método isalpha o regexp)
3. Almacenar la contraseña en un fichero.
- jose.maria@gmail.com -> jose.maria_gmail.com
4. Recuperar la contraseña a partir de un identificador de usuario.
5. Compara la contraseña introducida con la almacenada.
'''
import re
import getpass

def verificar_identificador(identificador : str) -> bool:
    patron = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}$'
    # Si hace match resultado recibe un objeto; si no, recibe None
    resultado = re.match(patron, identificador)
    if resultado==None:
        return False
    else:
        return True

def verificar_contrasenya(contrasenya : str) -> bool:
    LONGITUD_MINIMA = 6
    LONGITUD_MAXIMA = 15
    if len(contrasenya)<LONGITUD_MINIMA:
        return False
    if len(contrasenya)>LONGITUD_MAXIMA:
        return False
    if not contrasenya.isalpha():
        return False
    return True

def guardar_contrasenya(identificador : str, contrasenya : str) -> None:
    # Opción 1 (hace falta close)
    # fichero = open(identificador.replace('@','_'), mode='wt', encoding='utf-8')
    # fichero.write(contrasenya)
    # fichero.close()

    # Opción 2 (se cierra solo)
    with open(identificador.replace('@','_'), mode='wt', encoding='utf-8') as fichero:
        fichero.write(contrasenya)

def leer_contrasenya(identificador : str) -> str:
    nombre_fichero = identificador.replace('@','_')
    with open(nombre_fichero, mode='rt', encoding='utf-8') as fichero:
            contrasenya = fichero.read().strip()
    return contrasenya

print('1. Registrar usuario')
print('2. Validar usuario')
print('3. Salir')
opcion = 0
while (opcion!=3):
    opcion = int(input('Introduce una opción:'))
    if opcion==1:
        ##################################################
        # REGISTRO DE USUARIOS
        ##################################################
        identificador = input('Introduce tu email:')
        identificador = identificador.strip().lower()
        es_identificador_valido = verificar_identificador(identificador)
        if es_identificador_valido:
            password = getpass.getpass('Introduce tu contraseña:', echo_char='*')
            es_password_valida = verificar_contrasenya(password)
            if es_password_valida:
                guardar_contrasenya(identificador, password)
            else:
                print('La contraseña no es válida')
        else:
            print('El identificador no es un correo electrónico válido')
    elif opcion==2:
        ##################################################
        # VALIDACIÓN DE USUARIOS
        ##################################################
        identificador = input('Introduce tu email:')
        password = getpass.getpass(prompt='Introduce la contraseña:', echo_char='*')
        password_almacenada = leer_contrasenya(identificador)
        if password==password_almacenada:
            print('OK')
        else:
            print('Contraseña incorrecta')



        
        