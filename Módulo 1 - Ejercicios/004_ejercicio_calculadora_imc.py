'''
Crear una calculadora de Índice de Masa Corporal (IMC)
Con el IMC, indicar en qué rango se encuentra el paciente
NOTA: Utilizar float para la conversión a decimal
'''
import calculadora_imc

peso = float(input('Introduce tu peso (en kilogramos):'))
altura = float(input('Introduce tu altura (en metros):'))
imc = calculadora_imc.calculate_bmi(peso, altura)
print(imc)