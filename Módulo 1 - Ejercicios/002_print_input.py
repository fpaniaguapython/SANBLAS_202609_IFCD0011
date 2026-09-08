MAYORIA_EDAD = 18

print('José_Luis','Gema','Antonio', sep='*', end='loquesea')
print('a continuación')
print('a continuación')

nombre = input('Introduce tu nombre: ')
print(nombre)
edad = int(input('Introduce tu edad: '))

if edad>=MAYORIA_EDAD:
    print('Eres mayor de edad, adelante')
else:
    print('No puedes pasar a la discoteca')

