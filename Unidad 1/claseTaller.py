# Persona - parametros - metodos - Padre
# Estudiante - Profesor _ Herencia y Polimorfismo - super()

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property  # getter
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property  # getter
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property  # getter
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, creditos, promedioAnterior):
        super().__init__(nombre, apellido, edad)
        self.__creditos = creditos
        self.__promedio = promedioAnterior

    @property  # getter
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, creditos):
        self.__creditos = creditos

    @property
    def promedio(self):
        return self.__promedio
    
    @promedio.setter
    def promedio(self,promedio):
        self.__promedio = promedio
        
    def __str__(self):
        return f'{super().__str__()}, creditos: {self.creditos}, promedio: {self.promedio}'


class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self.__sueldo = sueldo

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        self.__sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}, Sueldo: {self.sueldo}'


persona1 = Persona("Miguel", "Camilo", 23)
print(persona1)

persona1.nombre = "Andres"
persona1.apellido = "Gutierrez"
persona1.edad = 18

print(persona1)

Karla = Estudiante("Karla","Maria",114,8,3)
print(Karla)
Karla.creditos = 24
print(Karla)

Arturo = Profesor("Arturo","Espitia",25,500)
print(Arturo)
Arturo.sueldo = 900
print(Arturo)
Arturo.sueldo = 999999
print(Arturo)
