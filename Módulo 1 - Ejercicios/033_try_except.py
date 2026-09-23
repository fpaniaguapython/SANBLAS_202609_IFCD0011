# Except genérico sin tratar el error
print('Comienzo el proceso...')
try:
    fichero = open('kfsdjdlj.txt', mode='r')
    datos = fichero.read()
    fichero.close()    
except:
    print('Ha ocurrido un error')
print('Fin del proceso.')


# Except controlando el tipo de error
print('Comienzo el proceso...')
try:
    fichero = open('kfsdjdlj.txt', mode='r')
    datos = fichero.read()
    fichero.close()    
except FileNotFoundError as fnfe:
    print('Ha ocurrido un error de tipo FileNotFoundError:', fnfe)
print('Fin del proceso.')


