import json


class Modelo(object):
    def __init__(self, base_datos = 'datos.json'):
        self.base_datos = base_datos
        self.load()
        self.__usuarios = {}
        self.__usuarios['contrasena123'] = 'admin123'
        self.__usuarios['admin'] = 'admin'

    def load(self):
        try:
            with open(self.base_datos, 'r') as archivo:
                self.datos = json.load(archivo)
        except FileNotFoundError:
            self.datos = []
            print("No se ha encontrado el archivo con la base de datos")
    
    def verificarUsuario(self, u:str, p:str):
        try:
            if self.__usuarios[p] == u:
                return (1, f'{u} bienvenido')
            
            return 0
        except: 
            return 2
        
    def guardar_info(self):
        with open(self.base_datos, 'w') as archivo:
            json.dump(self.datos,archivo, indent = 4)

    def creador_de_diccionarios(self,n:str,a:str,id:str, edad:str): #Primordial hacer este punto primero
        self.dic =       {
                        'Nombre': f'{n}',
                        'Apellido': f'{a}',
                        'Edad': f'{edad}',
                        'Identificacion': f'{id}'                            
                        
                    }
        return self.dic
    
    def añadir_paciente(self):
        paciente = self.dic
        if not any(p['Identificacion'] == paciente['Identificacion'] for p in self.datos):
            self.datos.append(paciente)
            self.guardar_info()
            return True
        return False
    
    def eliminar_paciente(self, id_paciente:str):
        try:
            self.datos = [p for p in self.datos if p['Identificacion'] != id_paciente]
            self.guardar_info()
        except:
            return False

    def buscar_paciente(self, nombre_paciente:str):
        nombre_paciente = nombre_paciente.lower().strip()
        return [p for p in self.datos if p['Nombre'].lower().startswith(nombre_paciente)]
    
        