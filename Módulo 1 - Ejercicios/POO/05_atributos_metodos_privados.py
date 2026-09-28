class Empleado:
    def __init__(self, nombre, categoria, salario):
        self.nombre = nombre
        self.categoria = categoria
        self.__salario = salario # Atributo privado

    # Método de acceso (de lectora)
    def get_salario(self):
        if (self.categoria=='JEFAZO'):
            raise Exception('No tienes acceso')
        return self.__salario

    def modificar_categoria_profesional(self, nueva_categoria):
        self.categoria = nueva_categoria
        # Uso interno de un método privado
        self.__modificar_salario(self, self.__salario*2)

    # Método privado
    def __modificar_salario(self, nuevo_salario):
        self.__salario = nuevo_salario

ramon = Empleado('Ramón', 'Desarrollador', 40_000)
print(ramon.nombre) # Ramón
print(ramon.categoria) # Desarrollador
# print(ramon.__salario) # Error
print(ramon._Empleado__salario) # 40000. Funciona pero no se usa.
salario = ramon.get_salario()