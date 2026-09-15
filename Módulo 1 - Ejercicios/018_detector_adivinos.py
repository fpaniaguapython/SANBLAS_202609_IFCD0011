import random

NUMERO_MINIMO = 1
NUMERO_MAXIMO = 9
NUMERO_MAXIMO_INTENTOS = 3

numero_secreto = random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)
# print(f'Número secreto:{numero_secreto}')
# Pide números hasta que el usuario acierte el número secreto.
# Si ha necesitado más de 3 intentos es un fraude.
# Si ha necesitado 3 o menos intentos es un adivino.

numero_candidato = int(input('Introduce número:'))
numero_intentos = 1
while (numero_candidato!=numero_secreto):
# while (numero_candidato!=numero_secreto and numero_intentos<NUMERO_MAXIMO_INTENTOS):
    print('ERROR')
    numero_candidato = int(input('Introduce número:'))
    numero_intentos+=1
print(f'Has realizado {numero_intentos} intentos')
if (numero_candidato==numero_secreto and numero_intentos<=NUMERO_MAXIMO_INTENTOS):
    print('Eres un adivino')
else:
    print('Eres un fraude')
