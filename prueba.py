# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.__nombre = nombre
#         self.__apellido = apellido
#         self.__edad = edad
       
#     def __str__(self):
#         return f"{self.__nombre} {self.__apellido} tiene {self.__edad} años de edad"
   
# persona1 = Persona("Pepito", "Perez", 50)
# persona1.edad = 22
# persona1.nombre = "Andrés"
# print(persona1)

# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.__nombre = nombre
#         self.__apellido = apellido
#         self.__edad = edad
       
#     def nombre(self):
#         return self.__nombre
#     def apellido(self):
#         return self.apellido
#     def edad(self):
#         return self.edad
#     def set_nombre(self, nombre):
#         self.__nombre = nombre
#     def set_apellido(self, apellido):
#         self.__apellido = apellido
#     def set_edad(self, edad):
#         self.__edad = edad
       
#     def __str__(self):
#         return f"{self.__nombre} {self.__apellido} tiene {self.__edad} años de edad"
   
# persona1 = Persona("Pepito", "Perez", 50)
# print(persona1)
# persona1.set_nombre("Andres")
# persona1.set_edad(22)
# print(persona1)

# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
       
#     def __str__(self):
#         return f"{self.nombre} {self.apellido} tiene {self.edad} años de edad"
   
# persona1 = Persona("Pepito", "Perez", 50)
# persona1.edad = 22
# print(persona1)

# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.__nombre = nombre
#         self.__apellido = apellido
#         self.__edad = edad
       
#     def set_variable1(self, nuevoNombre):
#         self.__nombre = nuevoNombre
        
#     def set_variable2(self, nuevoApellido):
#         self.__apellido = nuevoApellido
        
#     def set_variable3(self, nuevaEdad):
#         self.__edad = nuevaEdad    
        
#     def __str__(self):
#         return f"{self.__nombre} {self.__apellido} tiene {self.__edad} años de edad"
    
# carlos = Persona('Carlos','Guzman',22)
# print(carlos)

# carlos.set_variable1('Randy')
# carlos.set_variable2('Garcia')
# carlos.set_variable3(18)

# print(carlos)

# def main():
#     persona1 = Persona("Alberto", "Mandril", 55)
#     persona2 = Persona("Camilo", "Medina", 12)
#     print(persona1)
#     print(persona2)
#     persona2.set_variable3(35)
#     persona2.set_variable1("Andrés")
#     persona2.set_variable2("Zapata")
#     print(persona2)
    
# main()

# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.__nombre = nombre
#         self.__apellido = apellido
#         self.__edad = edad
       
#     def set_variable1(self, nuevoNombre):
#         self.__nombre = nuevoNombre
        
#     def set_variable2(self, nuevoApellido):
#         self.__apellido = nuevoApellido
        
#     def set_variable3(self, nuevaEdad):
#         self.__edad = nuevaEdad    
        
#     def __str__(self):
#         return f"{self.__nombre} {self.__apellido} tiene {self.__edad} años de edad"
        
# def main():
#     persona1 = Persona("Alberto", "Mandril", 55)
#     persona2 = Persona("Camilo", "Medina", 12)
#     print(persona1)
#     print(persona2)
#     persona2.set_variable3(35)
#     persona2.set_variable1("Andrés")
#     persona2.set_variable2("Zapata")
#     print(persona2)
    
# main()

# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.__nombre = self.validar_nombre(nombre)
#         self.__apellido = self.validar_apellido(apellido)
#         self.__edad = self.validar_edad(edad)

#     def validar_nombre(self, nombre):
#         if not isinstance(nombre, str):
#             raise ValueError("El nombre debe ser una cadena de caracteres")
#         return nombre

#     def validar_apellido(self, apellido):
#         if not isinstance(apellido, str):
#             raise ValueError("El apellido debe ser una cadena de caracteres")
#         return apellido

#     def validar_edad(self, edad):
#         if not isinstance(edad, int) or edad < 0:
#             raise ValueError("La edad debe ser un número entero no negativo")
#         return edad

#     def set_nombre(self, nuevo_nombre):
#         self.__nombre = self.validar_nombre(nuevo_nombre)

#     def set_apellido(self, nuevo_apellido):
#         self.__apellido = self.validar_apellido(nuevo_apellido)

#     def set_edad(self, nueva_edad):
#         self.__edad = self.validar_edad(nueva_edad)

#     def __str__(self):
#         return f"{self.__nombre} {self.__apellido} tiene {self.__edad} años de edad"

# # Ejemplo de uso
# try:
#     persona1 = Persona(5, "Perez", 50)
#     print(persona1)
# except ValueError as e:
#     print(f"Error: {e}")

class Paciente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __eq__(self, other):
        if isinstance(other, Paciente):
            return self.cedula == other.cedula
        return False

class Medico:
    listaPacientes = []

    @classmethod
    def adicionarPaciente(cls, paciente):
        if paciente in cls.listaPacientes:
            print("El paciente ya ha sido ingresado")
        else:
            cls.listaPacientes.append(paciente)
            print("Paciente agregado correctamente")

# Ejemplo de uso
paciente1 = Paciente("Juan", 123456789)
paciente2 = Paciente("Ana", 987654321)

Medico.adicionarPaciente(paciente1)
Medico.adicionarPaciente(paciente2)
Medico.adicionarPaciente(paciente1)  # Intentar agregar el mismo paciente nuevamente

print(Medico.listaPacientes)