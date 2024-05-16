class Persona():
    def __init__(self, nombre, cedula,genero):
        self._nombre = nombre
        self._genero = genero
        self.__cedula = cedula

persona1 = Persona("Juan",123,"M")

class Paciente(Persona):
    def __init__(self, servicio,nombre,cedula,genero):
        self.servicio = servicio
        Persona.__init__()

