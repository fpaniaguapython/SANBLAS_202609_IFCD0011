class Mascota:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

pulguitas = Mascota('Pulguitas', 'Perro')

print(pulguitas.__dict__)