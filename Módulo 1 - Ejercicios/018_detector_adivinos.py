import random

numero_secreto = random.randint(1,9)

# Pide números hasta que el usuario acierte el número secreto
# Si ha necesitado más de 3 intentos es un fraude.
# Si ha necesitado 3 o menos intentos es un adivino.

numero_candidato = int(input('Introduce número:'))
numero_intentos = 1
while (numero_candidato!=numero_secreto):
    print('ERROR')
    numero_candidato = int(input('Introduce número:'))
    numero_intentos+=1


