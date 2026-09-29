class Ordenador:
    def __init__(self, marca, modelo, ram, hd):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.hd = hd

    # Método mágico utilizado por print
    def __str__(self):
        #return f'Marca:{self.marca}. Modelo:{self.modelo}.'
        return str(self.__dict__)

    # Método mágico utilizado por print de listas, tuplas, etc.
    def __repr__(self):
        return str(self.__dict__)

mi_pc = Ordenador('HP', 'Elitebook', 16, 250)
print(mi_pc)
lista_pcs = [mi_pc]
print(lista_pcs)