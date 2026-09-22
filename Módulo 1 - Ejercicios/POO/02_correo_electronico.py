class CorreoElectronico:
    def __init__(self, emisor, receptor, asunto, mensaje):
        self.emisor = emisor
        self.receptor = receptor
        self.asunto = asunto
        self.mensaje = mensaje

    def enviar(self):
        print(f'Enviando {self.mensaje} a {self.receptor}')

correo_1 = CorreoElectronico('fernando@gmail.com',
                             'redescal@gmail.com', 'Cumpleaños',
                             'Mañana es el cumpleaños de Juan')   

correo_1.enviar()