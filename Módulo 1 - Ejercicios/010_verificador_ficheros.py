'''
Crear una función que recibe una cadena de 
caracteres y verifica:
- No contiene la cadena 'xyz'
- Termina por 'jpg', 'png' o 'gif'

Devuelve True si cumple con las reglas 
o False en caso contrario
NOTA: utilizamos el operador in (o not in)
y el método endswith
'''
def verificar_fichero(cadena : str) -> bool:
    # FIN - 15:18
    if 'xyz' in cadena:
        return False
    #if cadena.endswith('.jpg') or cadena.endswith(
    #     '.png') or cadena.endswith('.gif'):
    if (cadena.endswith(('.jpg','.png','.gif'))):
        return True
    return False

nombre_fichero = input('Nombre de fichero:')
resultado = verificar_fichero(nombre_fichero)
if resultado==True:
    print('Nombre de fichero válido')
else:
    print('Nombre de fichero erróneo')