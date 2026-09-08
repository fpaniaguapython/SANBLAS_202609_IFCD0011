'''
Crear una calculadora de Índice de Masa Corporal (IMC)
Con el IMC, indicar en qué rango se encuentra el paciente
NOTA: Utilizar float para la conversión a decimal
'''
import calculadora_imc

INSUFICIENTE = 18.5 # Inferior a este valor, por debajo del peso saludable
SALUDABLE = 24.9 # Hasta este valor, peso saludable
SOBREPESO = 29.9 # Hasta este valor, sobre peso. A partir de aquí, obesidad.

peso = float(input('Introduce tu peso (en kilogramos):'))
altura = float(input('Introduce tu altura (en metros):'))
imc = calculadora_imc.calculate_bmi(peso, altura)

print(f'El IMC es {imc}')

if imc<INSUFICIENTE:
    print('El paciente tiene un peso más bajo de lo saludable')
elif imc>INSUFICIENTE and imc<=SALUDABLE:
    print('El paciente tiene un peso más bajo de lo saludable')
elif imc<=SOBREPESO:
    print('El paciente tiene sobrepeso')
else:
    print('El paciente tiene obesidad')
