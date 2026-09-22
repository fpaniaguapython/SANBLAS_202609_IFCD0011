# DECLARACIÓN DE LA CLASE
class Motor:
    # CONSTRUCTOR
    def __init__(self, nombre, potencia, cilindrada, combustible):
        # ATRIBUTOS
        self.nombre = nombre
        self.potencia = potencia
        self.cilindrada = cilindrada
        self.combustible = combustible
        self.arrancado = False
        self.velocidad = 0

    # MÉTODOS
    def arrancar(self):
        self.arrancado = True

    def acelerar(self, incremento):
        if self.arrancado==True:
            # self.velocidad=self.velocidad+incremento        
            self.velocidad+=incremento        

# INSTANCIACIÓN --> CREACIÓN DE UNA INSTANCIA U OBJETO
motor_v8 = Motor('MOTOR SUPER V8', 400, 1000, 'GASOLINA')
motor_v16 = Motor('MOTOR SUPER V16', 600, 3000, 'GASOIL')

# INVOCAR AL MÉTODO arrancar
motor_v8.arrancar()

# Acelera el motor en 100km/h
motor_v8.acelerar(100)
print(motor_v8.velocidad)