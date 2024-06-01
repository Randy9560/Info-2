from Modelo import *
from vista import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec_())

class userController:
    def __init__(self, user_model:object = Modelo()):
        self.user_model = user_model
        
    def log_in(self, username:str, password:str):
        result = self.user_model.verificarUsuario(username, password)
        return result
    
class PatientsController:
    def __init__(self, paciente_model = Modelo()):
        self.paciente_model = paciente_model

    def newPatient(self,name:str,apellido:str,id:str, edad:str ):
        self.nuevopaciente = self.paciente_model.creador_de_diccionarios(name,apellido,id,edad)
        self.paciente  = self.paciente_model.añadir_paciente()
        return self.paciente
    
    def getPatient(self, initName:str = ''):
        return self.paciente_model.buscar_paciente(initName)
    
    def delPatient(self, id:str):
        return self.paciente_model.eliminar_paciente(id)
    
