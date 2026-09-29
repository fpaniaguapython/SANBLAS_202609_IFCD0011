"""
Crear un clase que recoja la ficha de inscripción en un gimnasio.
Los atributos son:
- Nombre.
- Edad.
- Número de teléfono.
- Email.

Crear los métodos siguiente:
- Mostrar los datos de la ficha por pantalla.
- Comprobar que todos los atributos tienen valor (no son None)
- Escribir los datos de la ficha en un fichero de texto.
- Escribir los datos de la ficha en un fichero json.
- Escribir la ficha en un fichero pdf.
"""
import json

class Ficha:
    def __init__(self, nombre: str, edad: int, telefono: str, email: str):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.email = email

    def mostrar_datos(self):
        print(f'Nombre:{self.nombre}')
        print(f'Edad:{self.edad}')
        print(f'Teléfono:{self.telefono}')
        print(f'Email:{self.email}')

    def has_todos_con_valor(self):
        if (self.nombre is None or self.edad is None or 
            self.telefono is None or self.email is None):
            return False
        else:
            return True

    def guardar_en_fichero(self):
        nombre_fichero = self.nombre.replace(' ','_').lower()+'.txt'
        with open(nombre_fichero, mode='wt', encoding='utf-8') as fichero:
            fichero.write(f'Nombre:{self.nombre}')
            fichero.write('\n')
            fichero.write(f'Edad:{self.edad}')
            fichero.write('\n')
            fichero.write(f'Teléfono:{self.telefono}')
            fichero.write('\n')
            fichero.write(f'Email:{self.email}')

    def guardar_en_json(self):
        nombre_fichero = self.nombre.replace(' ','_').lower()+'.json'
        with open(nombre_fichero, mode='wt', encoding='utf-8') as fichero:
            json.dump(self.__dict__, fichero, ensure_ascii=False)


ficha_1 = Ficha('José Luis', 34, '630881100', 'ernesto38@yahoo.com')
ficha_1.mostrar_datos()
print(ficha_1.has_todos_con_valor())
ficha_1.guardar_en_fichero()
ficha_1.guardar_en_json()


