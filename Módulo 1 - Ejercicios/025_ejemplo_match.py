print('1. Saltar')
print('2. Bailar')
print('3. Pelear')
opcion = int(input('Opción:'))

# Opción if
if opcion==1:
    print('Saltando...')
elif opcion==2:
    print('Bailando...')
elif opcion==3:
    print('Peleando...')
else:
    print('No te entiendo')

# Opción match
match opcion:
    case 1:
        print('Saltando...')
    case 2:
        print('Bailando...')
    case 3:
        print('Peleando...')
    case _: # Por defecto
        print('No te entiendo')