numero_secreto = 8
numero_candidato = -1
numero_intentos = 0

while numero_intentos < 3:
    numero_candidato = int(input('Número:'))
    numero_intentos+=1
    if numero_secreto==numero_candidato:
        # break # Aborta la ejecución del bucle
        continue # Aborta la ejecución de la iteracción
    nombre = input('Nombre:')
    edad = int(input('Edad:'))
    print(f'{nombre}, tienes {edad} años y eres un fraude')
else:
    print('Se ejecuta si sale por la condición del While')
    print('en este caso, por llegar a los 3 intentos')



    
