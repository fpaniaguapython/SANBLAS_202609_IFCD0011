class Motor:
    def __init__(self, nombre, potencia, cilindrada, combustible):
        self.nombre = nombre
        self.potencia = potencia
        self.cilindrada = cilindrada
        self.combustible = combustible

motor_v8 = Motor('MOTOR SUPER V8', 400, 1000, 'GASOLINA')
motor_v16 = Motor('MOTOR SUPER V16', 600, 3000, 'GASOIL')

print(motor_v8.__dict__)