class Animal:
    def __init__(self, nombre, familia, genero):
        self.nombre = nombre
        self.familia = familia
        self.genero = genero

    def nacer(self):
        print('Naciendo...')

    def reproducir(self):
        print('Reproduciéndose...')


class AnimalPicorro(Animal):
    def __init__(self, nombre, familia, genero, tipo_pico):
        super().__init__(nombre, familia, genero)
        self.tipo_pico = tipo_pico

    def picar(self):
        print('Pica, pica...')

alacrán = AnimalPicorro('Alacrán', 'Ortrópodo', 'Bicho')
alacrán.nacer() # Viene de Animal
alacrán.reproducir() # Viene de Animal
alacrán.picar() # Viene de AnimalPicorro

felix = Animal('Gato', 'Mamífero', 'Felino')
felix.nacer()
felix.reproducir()
# felix.picar() # NO