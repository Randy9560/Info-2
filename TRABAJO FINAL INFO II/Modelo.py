import json
import os
from collections import Counter


class Modelo(object):
    usermedico = None
    def __init__(self, base_datos = 'datos.json'):
        self.base_datos = base_datos
        self.load()
        self.__usuarios_admin = {}
        self.__usuarios_admin['contrasena123'] = 'admin123'
        self.__usuarios_admin['admin'] = 'admin'
        self.__usuarios_medicos = {}
        self.__usuarios_medicos['jose123'] = 'jose'
        self.__usuarios_medicos['123'] = 'randy'
        self.lista_edad_medicos = []
        self.lista_genero_medicos = []
        self.lista_edad_medicos_p = []
        self.lista_generos_paciente = []
        self.lista_enfermos = []

        
    
    def obtenerValor(self,u):
        Modelo.usermedico = u
        

    def verificarUsuarioAdmin(self, u:str, p:str):
        try:
            if self.__usuarios_admin[p] == u:
                return 1
            
            return 0
        except: 
            return 2
        
    def verificarUsuariomedico(self, u:str, p:str):
        try:
            if self.__usuarios_medicos[p] == u:
                
                return 1
            
            return 0
        except: 
            return 2        
        
    def registro(self,u,p):
        self.__usuarios_medicos[p] = u
      
    def load(self):
        try:
            with open(self.base_datos, 'r') as archivo:
                self.datos = json.load(archivo)
        except FileNotFoundError:
            self.datos = []
            print("No se ha encontrado el archivo con la base de datos")
        
    def guardar_info(self):
        with open(self.base_datos, 'w') as archivo:
            json.dump(self.datos,archivo, indent = 4)

    def creador_de_diccionarios(self,n:str,a:str,id:str, edad:str, genero:str): 
        self.dic =       {
                        'Nombre': f'{n}',
                        'Apellido': f'{a}',
                        'Edad': f'{edad}',
                        'Genero': f'{genero}',
                        'Identificacion': f'{id}'                            
                        
                    }
        return self.dic
    
    def añadir_medico(self):
        medico = self.dic
        if not any(p['Identificacion'] == medico['Identificacion'] for p in self.datos):
            self.datos.append(medico)
            self.guardar_info()
            return True
        return False
    
    def eliminar_medico(self, id_medico:str):
        try:
            self.datos = [p for p in self.datos if p['Identificacion'] != id_medico]
            self.guardar_info()
        except:
            return False

    def buscar_medico(self, nombre_medico:str):
        nombre_medico = nombre_medico.lower().strip()
        return [p for p in self.datos if p['Nombre'].lower().startswith(nombre_medico)]
         

    def VerificarJson(self):
        self.nombrejson = f'{Modelo.usermedico}.json'
        dic = []
        try:
            with open(self.nombrejson, 'r') as archivo:
                self.datos1 = json.load(archivo)
        except :
            self.datos1 = []
            with open(self.nombrejson, 'w') as archivo:
                json.dump(dic,archivo,indent= 4)

    def guardar_info_p(self):
        with open(self.nombrejson, 'w') as archivo:
            json.dump(self.datos1,archivo, indent = 4)

    def creador_de_diccionarios_p(self,n:str,a:str,id:str, edad:str, genero:str,enfermo: str): 
        self.dic =       {
                        'Nombre': f'{n}',
                        'Apellido': f'{a}',
                        'Edad': f'{edad}',
                        'Genero': f'{genero}',
                        'Enfermo': f'{enfermo}',
                        'Identificacion': f'{id}'                            
                        
                    }
        return self.dic

    def añadir_paciente(self):
        paciente = self.dic
        if not any(p['Identificacion'] == paciente['Identificacion'] for p in self.datos1):
            self.datos1.append(paciente)
            self.guardar_info_p()
            return True
        return False

    def eliminar_paciente(self, id_medico:str):
        try:
            self.datos1 = [p for p in self.datos1 if p['Identificacion'] != id_medico]
            self.guardar_info_p()
        except:
            return False


    def buscar_paciente(self, nombre_paciente:str):
        nombre_paciente = nombre_paciente.lower().strip()
        return [p for p in self.datos1 if p['Nombre'].lower().startswith(nombre_paciente)]

    def lista_Datos_edad(self, edad):
        self.lista_edad_medicos.append(edad)
        return self.lista_edad_medicos   
    
    def lista_Datos_edad_p(self,edad):
        self.lista_edad_medicos_p.append(edad)
        return self.lista_edad_medicos_p

    def lista_Datos_genero(self, genero):
        self.lista_genero_medicos.append(genero)
        return self.lista_genero_medicos
    
    def lista_Datos_genero_p(self,genero):
        self.lista_generos_paciente.append(genero)
        return self.lista_generos_paciente
    
    def lista_Datos_enfermo(self,enfermo):
        self.lista_enfermos.append(enfermo)
        return self.lista_enfermos
    

    def listas_datos_edad_completos_p(self):
        valores = Counter(self.lista_edad_medicos_p)
        valores_ejex = list(valores.keys())
        valores_ejey = list(valores.values())
        return [valores_ejex,valores_ejey]

    def listas_datos_completos(self):
        valores = Counter(self.lista_edad_medicos)
        valores_ejex = list(valores.keys())
        valores_ejey = list(valores.values())
        return [valores_ejex,valores_ejey]
    
    def listas_datos_generos_completos(self):
        valores = Counter(self.lista_genero_medicos)
        colores = ['Blue','Pink']
        nombres = ['Masculinos','Femeninos']
        datos = list(valores.values())
        genero = list(valores.keys())
        return[datos,nombres,colores,genero]
    
    def listas_datos_generos_completos_p(self):
        valores = Counter(self.lista_generos_paciente)
        colores = ['Blue','Pink']
        nombres = ['Masculinos','Femeninos']
        datos = list(valores.values())
        genero = list(valores.keys())
        return[datos,nombres,colores,genero]
    
    def lista_datos_todos_enfermos(self):
        valores = Counter(self.lista_enfermos)
        colores = ['red','purple']
        nombres = ['Enfermos','Sanos']
        datos = list(valores.values())
        diagnostico = list(valores.keys())
        return[datos,nombres,colores,diagnostico]
    
    def actualizar_lista(self):
        self.lista_edad_medicos = []
        self.lista_genero_medicos = []

    def actualizar_listas_p(self):
        self.lista_edad_medicos_p = []
        self.lista_generos_paciente = []
        self.lista_enfermos = []

