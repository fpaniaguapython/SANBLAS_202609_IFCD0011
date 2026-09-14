'''
Solicitar un número entero al usuario.
Indicar si el número es par o impar (operador %). 
NO USAR EXPRESIONES TERNARIAS
'''
numero = int(input('Número:'))
if numero%2==0:
    resultado = 'Es par'
else:
    resultado = 'Es impar'
print(resultado)

resultado = 'Es par' if numero%2==0 else 'Es impar'
print(resultado)
