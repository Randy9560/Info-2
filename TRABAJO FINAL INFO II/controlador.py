from Modelo import *
from vista import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec_())

class userController:
    def __init__(self, user_model:object = Modelo()):
        self.user_model = user_model

    def valor(self, valor):
        self.user_model.obtenerValor(valor)

    def log_in(self, username:str, password:str):
        result = self.user_model.verificarUsuarioAdmin(username, password)
        return result
    
    def log_in_medico(self, username:str, password:str):
        result = self.user_model.verificarUsuariomedico(username, password)
        return result
    
    def agregar_usuario(self, u, p): 
        return self.user_model.registro(u,p)
    
class AdminController:
    def __init__(self, admin_model = Modelo()):
        self.admin_model = admin_model

    def newMedico(self,name:str,apellido:str,id:str, edad:str, genero:str ):
        self.nuevomedico = self.admin_model.creador_de_diccionarios(name,apellido,id,edad,genero)
        self.medico  = self.admin_model.añadir_medico()
        return self.medico
    
    def getMedico(self, initName:str = ''):
        return self.admin_model.buscar_medico(initName)
    
    def delMedico(self, id:str):
        return self.admin_model.eliminar_medico(id)
    
    def guardarinfografica(self, edad):
        return self.admin_model.lista_Datos_edad(edad)
    
    def guardarinfografica_pie(self,genero):
        return self.admin_model.lista_Datos_genero(genero)
    
    
    def traer_valores_edad(self):
        return self.admin_model.listas_datos_completos()
    
    def traer_valores_genero(self):
        return self.admin_model.listas_datos_generos_completos()
    
    def actualizar(self):
        self.admin_model.actualizar_lista()

class MedicoController:
    def __init__(self, medico_model = Modelo()):
        self.medico_model = medico_model

    def verificarinfo(self):
        self.medico_model.VerificarJson()

    def actualizar(self):
        self.medico_model.actualizar_listas_p()

    def newPatient(self,name:str,apellido:str,id:str, edad:str, genero:str, enfermo:str ):
        self.nuevopaciente= self.medico_model.creador_de_diccionarios_p(name,apellido,id,edad,genero,enfermo)
        self.paciente  = self.medico_model.añadir_paciente()
        return self.paciente
    
    def guardarinfografica_p(self, edad):
        return self.medico_model.lista_Datos_edad_p(edad)
    
    def traer_valores_edad_p(self):
        return self.medico_model.listas_datos_edad_completos_p()
    
    def guardarinfogenero_pie(self,genero):
        return self.medico_model.lista_Datos_genero_p(genero)
    
    def traer_valores_genero_p(self):
        return self.medico_model.listas_datos_generos_completos_p()
    
    def guardarinfoenfermo(self,enfermo):
        return self.medico_model.lista_Datos_enfermo(enfermo)
    
    def traer_valores_enfermo_p(self):
        return self.medico_model.lista_datos_todos_enfermos()
    
    def getPatient(self, initName:str = ''):
        return self.medico_model.buscar_paciente(initName)
    
    
    def delPatient(self, id:str):
        return self.medico_model.eliminar_paciente(id)
    
