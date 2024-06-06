from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QPushButton, QTableWidgetItem, QApplication, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5 import QtGui
from controlador import userController, AdminController, MedicoController
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class Login(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('login.ui', self)
        self.userController = userController()
        self.label_4.setPixmap(QtGui.QPixmap('imagenes\Family-Health-Care-Clinic-825x510.png'))
        self.label_4.setScaledContents(True)
        self.setup()

    def setup(self):
        self.LoginBottom.clicked.connect(self.login)
        self.password.setEchoMode(QLineEdit.Password)
        self.botonregistro.clicked.connect(self.accion_registrar)

    def login(self):
        usuario = self.user.text()
        contrasena = self.password.text()
        existeadmin = self.userController.log_in(usuario, contrasena)
        existemedico = self.userController.log_in_medico(usuario, contrasena)

        if existeadmin == 1:
            self.PacienteView = AdminView()
            self.PacienteView.show()
            self.close()

        elif existeadmin == 0 and not(existemedico == 1):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("No existe un usuario con los \ndatos proporcionados")
            msgBox.setWindowTitle('Datos incorrectos')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        elif existeadmin == 2 and not(existemedico == 1):
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Warning)
            msgBox1.setText("Contraseña erronea.\n Intente de nuevo.")
            msgBox1.setWindowTitle('Datos incorrectos')
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()

        elif existemedico == 1:
            self.userController.valor(usuario)
            self.PacienteView = MedicoView()
            self.PacienteView.show()
            self.close()

        elif existemedico == 0 and not(existeadmin == 1):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("No existe un usuario con los \ndatos proporcionados")
            msgBox.setWindowTitle('Datos incorrectos')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        elif existemedico == 2 and not(existeadmin == 1):
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Warning)
            msgBox1.setText("Contraseña erronea.\n Intente de nuevo.")
            msgBox1.setWindowTitle('Datos incorrectos')
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()



    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        try:
            if self.dragging:
                self.move(self.mapToGlobal(event.pos() - self.offset))
        except:
            pass

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def recibir_info(self, u,p):
        resultado = self.userController.log_in(u,p)
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        if resultado == 1:
            msg.setText("Usuario existente")
        else:
            self.userController.agregar_usuario(u,p)
            msg.setText("Usuario registrado con éxito")
        msg.show()

    def accion_registrar(self):
        ventana_emergente=ventanaEmergente(self)
        ventana_emergente.show()

class ventanaEmergente(QDialog):
    def __init__(self, ppl=None):
        super().__init__(ppl)
        loadUi(r'ventana_secundaria.ui',self)
        self.label_5.setPixmap(QtGui.QPixmap('imagenes\Family-Health-Care-Clinic-825x510.png'))
        self.label_5.setScaledContents(True)
        self.setup()
        self.parent = ppl

    def setup(self):
        self.buttonBox.accepted.connect(self.conectarRegistro)
        self.buttonBox.rejected.connect(lambda:self.close())

    def conectarRegistro(self):
        usuario = self.usuarioregistro.text()
        password = self.contrasenaregistro.text()
        self.parent.recibir_info(usuario, password)
        self.close()

class AdminView(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('admin.ui', self)
        self.label_7.setPixmap(QtGui.QPixmap('imagenes\pngtree-medical-clipart-cartoon-character-of-a-couple-of-doctor-characters-vector-png-image_11053952.png'))
        self.label_7.setScaledContents(True)
        self.AdminController = AdminController()
        self.setup()

    def setup(self):
        validator = QtGui.QIntValidator(1, 9999999, self)
        self.tableView.verticalHeader().setVisible(False)
        self.Ingreso.clicked.connect(self.newMedico)
        self.buscar.clicked.connect(self.filterMedico)
        self.id.setValidator(validator)
        self.salir.clicked.connect(self.logout)
        self.age.setValidator(validator)
        self.estadisticas.clicked.connect(self.graficar_medicos)
        self.actualizar.clicked.connect(self.actualizar_datos)
        self.readMedico()
        self.tableUpdate()

    def actualizar_datos(self):
        self.AdminController.actualizar()
        self.tableUpdate()
        

    def graficar_medicos(self):
        self.ventana_graficos_medicos = GraficosMedicos()
        self.ventana_graficos_medicos.show()

    def logout (self):
        self.PrincipalView = Login()
        self.PrincipalView.show()
        self.close()

    def readMedico(self):
        self.listaMedicos = self.AdminController.getMedico()

    def filterMedico(self):
        buscar = self.idbuscar.text()
        self.listaMedicos = self.AdminController.getMedico(buscar)
        self.tableUpdate()

    def newMedico(self):
        id = self.id.text()
        nombre = self.name.text()
        apellido = self.lastname.text()
        edad = self.age.text()
        genero = self.genero.itemText(self.genero.currentIndex())
        if not id or not nombre or not apellido or not edad or not genero:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Debe ingresar todos los datos")
            msgBox.setWindowTitle('Datos faltantes')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            isUnique = self.AdminController.newMedico(nombre, apellido, id, edad,genero)
            if not isUnique:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("El medico con está identificación ya se encuentra registrado")
                msgBox.setWindowTitle('Id repetida')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            else:
                self.readMedico()
                self.tableUpdate()
                self.id.setText('')
                self.name.setText('')
                self.lastname.setText('')
                self.age.setText('')
                


    def tableUpdate(self):
        self.tableView.setRowCount(len(self.listaMedicos))
        self.tableView.setColumnCount(6)
        columnas = ["Nombre", "Apellido", "Edad","Genero", "ID", "Eliminar"]
        columnLayout = ['Nombre','Apellido','Edad',"Genero",'Identificacion']
        self.tableView.setHorizontalHeaderLabels(columnas)
        for row, paciente in enumerate(self.listaMedicos):
            for column in range(5):
                item = QTableWidgetItem(paciente[columnLayout[column]])
                self.tableView.setItem(row, column, item)

            btn = QPushButton('Borrar', self)
            btn.clicked.connect(lambda ch, r=row: self.Eliminar(r))
            self.guardarDatos_grafica(row)
            self.guardarDatos_grafica_pie(row)
            self.tableView.setCellWidget(row, 5, btn)

        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 100)
        self.tableView.setColumnWidth(2, 100)
        self.tableView.setColumnWidth(3, 100)
        self.tableView.setColumnWidth(4, 100)
        self.tableView.setColumnWidth(5, 100)
        self.traer_valores_grafica_edad()
        self.traer_Valores_pie()

    def guardarDatos_grafica(self, row):
        edad = self.tableView.item(row, 2).text()
        self.AdminController.guardarinfografica(edad)

    def guardarDatos_grafica_pie(self, row):
        genero = self.tableView.item(row, 3).text()
        self.AdminController.guardarinfografica_pie(genero)
        
        
    def traer_Valores_pie(self):
          valores = self.AdminController.traer_valores_genero()
          grafica_medico_genero.traerDatos_pie(self,valores) 
    

    def traer_valores_grafica_edad(self):
        valores = self.AdminController.traer_valores_edad()
        grafica_medico_edad.traerDatos_x(self,valores)


        

    def Eliminar(self, row):
        id = self.tableView.item(row, 4).text()
        deleted = self.AdminController.delMedico(id)
        if deleted == False:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Este error nunca deberia mostrarse\nen caso de verse usted hizo algo que\nlos desarrolladores nunca esperaban que\nsucediera.")
            msgBox.setWindowTitle('Error')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        self.readMedico()
        self.tableUpdate()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        try:
            if self.dragging:
                self.move(self.mapToGlobal(event.pos() - self.offset))
        except:
            pass

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

class MedicoView(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('medico.ui', self)
        self.label_8.setPixmap(QtGui.QPixmap('imagenes\patient-on-the-hospital-bed-and-doctor-visitor-graphic-illustration-png.webp'))
        self.label_8.setScaledContents(True)
        self.MedicoController = MedicoController()
        self.setup()

    def setup(self):
        validator = QtGui.QIntValidator(1, 9999999, self)
        self.tableView.verticalHeader().setVisible(False)
        self.Ingresopaciente.clicked.connect(self.newPatient)
        self.buscarpaciente.clicked.connect(self.filterPatient)
        self.idpaciente.setValidator(validator)
        self.salir.clicked.connect(self.logout)
        self.edadpaciente.setValidator(validator)
        self.estadisticas_p.clicked.connect(self.graficar_paciente)
        self.actualizar_p.clicked.connect(self.actualizar_paciente)
        self.verificarArch()
        self.readPatient()
        self.tableUpdate()

    def logout (self):
        self.PrincipalView = Login()
        self.PrincipalView.show()
        self.close()

    def actualizar_paciente(self):
        self.MedicoController.actualizar()
        self.tableUpdate()

    def graficar_paciente(self):
        self.ventana_graficos_paciente = GraficosPaciente()
        self.ventana_graficos_paciente.show()

    def verificarArch(self):
        self.MedicoController.verificarinfo()

    def readPatient(self):
        self.listaPacientes = self.MedicoController.getPatient()

    def filterPatient(self):
        buscar = self.idbuscarpac.text()
        self.listaPacientes = self.MedicoController.getPatient(buscar)
        self.tableUpdate()

    def newPatient(self):
        id = self.idpaciente.text()
        nombre = self.nombrepaciente.text()
        apellido = self.apellidopaciente.text()
        edad = self.edadpaciente.text()
        genero = self.generopaciente.itemText(self.generopaciente.currentIndex())
        enfermo = self.enfermobox.itemText(self.enfermobox.currentIndex())
        if not id or not nombre or not apellido or not edad or not genero or not enfermo:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Debe ingresar todos los datos")
            msgBox.setWindowTitle('Datos faltantes')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            isUnique = self.MedicoController.newPatient(nombre, apellido, id, edad,genero,enfermo)
            if not isUnique:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("El paciente con está identificación ya se encuentra registrado")
                msgBox.setWindowTitle('Id repetida')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            else:
                self.readPatient()
                self.tableUpdate()
                self.idpaciente.setText('')
                self.nombrepaciente.setText('')
                self.apellidopaciente.setText('')
                self.edadpaciente.setText('')
               


    def tableUpdate(self):
        self.tableView.setRowCount(len(self.listaPacientes))
        self.tableView.setColumnCount(7)
        columnas = ["Nombre", "Apellido", "Edad","Genero","Enfermo", "ID", "Eliminar"]
        columnLayout = ['Nombre','Apellido','Edad',"Genero","Enfermo",'Identificacion']
        self.tableView.setHorizontalHeaderLabels(columnas)
        for row, paciente in enumerate(self.listaPacientes):
            for column in range(6):
                item = QTableWidgetItem(paciente[columnLayout[column]])
                self.tableView.setItem(row, column, item)

            btn = QPushButton('Borrar', self)
            btn.clicked.connect(lambda ch, r=row: self.Eliminar(r))
            self.guardarDatos_grafica_bar(row)
            self.guardarDatos_genero_pie_p(row)
            self.guardarDatos_enfermos_pie_p(row)
            self.tableView.setCellWidget(row, 6, btn)

        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 100)
        self.tableView.setColumnWidth(2, 100)
        self.tableView.setColumnWidth(3, 100)
        self.tableView.setColumnWidth(4, 100)
        self.tableView.setColumnWidth(5, 100)
        self.tableView.setColumnWidth(6, 100)
        self.traer_valores_grafica_edad_p()
        self.traer_Valores_genero_p()
        self.traer_Valores_enfermo()

    def guardarDatos_grafica_bar(self, row):
        edad = self.tableView.item(row, 2).text()
        self.MedicoController.guardarinfografica_p(edad)

    def traer_valores_grafica_edad_p(self):
        valores = self.MedicoController.traer_valores_edad_p()
        grafica_paciente_edad.traerDatos_bar_p(self,valores)    

    def guardarDatos_genero_pie_p(self, row):
        genero = self.tableView.item(row, 3).text()
        self.MedicoController.guardarinfogenero_pie(genero)
               
    def traer_Valores_genero_p(self):
          valores = self.MedicoController.traer_valores_genero_p()
          grafica_paciente_genero.traer_genero_pie_p(self,valores) 

    def guardarDatos_enfermos_pie_p(self, row):
        enfermo = self.tableView.item(row, 4).text()
        self.MedicoController.guardarinfoenfermo(enfermo)

    def traer_Valores_enfermo(self):
        enfermo = self.MedicoController.traer_valores_enfermo_p()
        grafica_enfermos.traer_enfermos(self,enfermo)
    


    def Eliminar(self, row):
        id = self.tableView.item(row, 5).text()
        deleted = self.MedicoController.delPatient(id)
        if deleted == False:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Este error nunca deberia mostrarse\nen caso de verse usted hizo algo que\nlos desarrolladores nunca esperaban que\nsucediera.")
            msgBox.setWindowTitle('Error')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        self.readPatient()
        self.tableUpdate()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        try:
            if self.dragging:
                self.move(self.mapToGlobal(event.pos() - self.offset))
        except:
            pass

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

class GraficosMedicos(QDialog):
    def __init__(self):
        super(GraficosMedicos,self).__init__()
        loadUi(r'graficas_medicos.ui',self)
        self.setup()

    def setup(self):
        self.grafica_medicos =  grafica_medico_edad()
        self.grafica_genero = grafica_medico_genero()
        self.graficaedad.addWidget(self.grafica_medicos)
        self.graficagenero.addWidget(self.grafica_genero)

class grafica_medico_edad(FigureCanvas):
    datos_to_use_x = None
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.datos_grafica()


    def traerDatos_x(self,datos):
        grafica_medico_edad.datos_to_use_x = datos
      
           
    def datos_grafica(self):
        
        plt.title("Grafica edades de los medicos")
        x = np.array(grafica_medico_edad.datos_to_use_x[0])
        y = np.array(grafica_medico_edad.datos_to_use_x[1])
        self.ax.bar(x, y , edgecolor="blue", linewidth=2) 
        QtCore.QTimer.singleShot(10, self.datos_grafica)

class grafica_medico_genero(FigureCanvas):

    datos_to_use_pie = None
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.datos_grafica_genero()


    def traerDatos_pie(self,datos):
        grafica_medico_genero.datos_to_use_pie = datos

    def datos_grafica_genero(self):
        
        plt.title("Grafica Genero de los medicos")
        x = grafica_medico_genero.datos_to_use_pie[0]
        try:
            if len(x) != 1 :
                self.ax.pie(x, labels = [f'{grafica_medico_genero.datos_to_use_pie[1][0]} - {x[0]} '
                                        ,f'{grafica_medico_genero.datos_to_use_pie[1][1]} - {x[1]}'], 
                                        colors = grafica_medico_genero.datos_to_use_pie[2]) 
                QtCore.QTimer.singleShot(10, self.datos_grafica_genero)
            elif len(x) == 1:
                if grafica_medico_genero.datos_to_use_pie[3][0] == 'Masculino':     
                    self.ax.pie(x, labels = [f'M {x}'], colors = ['Blue']) 
                    QtCore.QTimer.singleShot(10, self.datos_grafica_genero)
                else:
                    self.ax.pie(x, labels = [f'F {x}'], colors = ['pink']) 
                    QtCore.QTimer.singleShot(10, self.datos_grafica_genero)
        except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("No hay datos de generos ")
                msgBox.setWindowTitle('Sin muestras')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

class GraficosPaciente(QDialog):
    def __init__(self):
        super(GraficosPaciente,self).__init__()
        loadUi(r'graficas_pacientes.ui',self)
        self.setup()

    def setup(self):
        self.grafica_pacientes_edad =  grafica_paciente_edad()
        self.grafica_genero_p = grafica_paciente_genero()
        self.graficaedad_p.addWidget(self.grafica_pacientes_edad)
        self.graficagenero_p.addWidget(self.grafica_genero_p)
        self.grafica_enfermos = grafica_enfermos()
        self.graficaenfermo.addWidget(self.grafica_enfermos)

class grafica_paciente_edad(FigureCanvas):
    datos_x = None
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.datos_grafica_p()

    def traerDatos_bar_p(self,datos):
        grafica_paciente_edad.datos_x = datos

    def datos_grafica_p(self):
        
        plt.title("Grafica edades de los pacientes")
        x = np.array(grafica_paciente_edad.datos_x[0])
        y = np.array(grafica_paciente_edad.datos_x[1])
        self.ax.bar(x, y , edgecolor="green", linewidth=2) 
        QtCore.QTimer.singleShot(10, self.datos_grafica_p)

class grafica_paciente_genero(FigureCanvas):
    datos_pie_p = None
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.datos_grafica_genero_p()

    def traer_genero_pie_p(self,datos):
        grafica_paciente_genero.datos_pie_p = datos

    def datos_grafica_genero_p(self):
        
        plt.title("Grafica Genero de los Pacientes")
        x = grafica_paciente_genero.datos_pie_p[0]
        try:
            if len(x) != 1 :
                self.ax.pie(x, labels = [f'{grafica_paciente_genero.datos_pie_p[1][0]} - {x[0]} '
                                            ,f'{grafica_paciente_genero.datos_pie_p[1][1]} - {x[1]}'], 
                                            colors = grafica_paciente_genero.datos_pie_p[2]) 
                QtCore.QTimer.singleShot(10, self.datos_grafica_genero_p)
            elif len(x) == 1:
                if grafica_paciente_genero.datos_pie_p[3][0] == 'Masculino':     
                    self.ax.pie(x, labels = [f'M {x}'], colors = ['Blue']) 
                    QtCore.QTimer.singleShot(10, self.datos_grafica_genero_p)
                else:
                    self.ax.pie(x, labels = [f'F {x}'], colors = ['pink']) 
                    QtCore.QTimer.singleShot(10, self.datos_grafica_genero_p)
        except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("No hay datos de genero ")
                msgBox.setWindowTitle('Sin muestras')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

class grafica_enfermos(FigureCanvas):
    datos_pie_enfermos = None
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.datos_grafica_enfermos()

    def traer_enfermos(self,enfermo):
        grafica_enfermos.datos_pie_enfermos = enfermo

    def datos_grafica_enfermos(self):
        
        plt.title("Grafica de Pacientes enfermos")
        x = grafica_enfermos.datos_pie_enfermos[0]
        try:
            if len(x) != 1 :
                self.ax.pie(x, labels = [f'{grafica_enfermos.datos_pie_enfermos[1][1]} - {x[0]} '
                                        ,f'{grafica_enfermos.datos_pie_enfermos[1][0]} - {x[1]}'], 
                                        colors = grafica_enfermos.datos_pie_enfermos[2]) 
                QtCore.QTimer.singleShot(10, self.datos_grafica_enfermos)
            elif len(x) == 1:
                if grafica_enfermos.datos_pie_enfermos[3][0] == 'SI':     
                    self.ax.pie(x, labels = [f'Enf. {x}'], colors = ['red']) 
                    QtCore.QTimer.singleShot(10, self.datos_grafica_enfermos)
                else:
                    self.ax.pie(x, labels = [f'No Enf. {x}'], colors = ['purple']) 
                    QtCore.QTimer.singleShot(10, self.datos_grafica_enfermos)
        except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("No hay datos de diagnostico ")
                msgBox.setWindowTitle('Sin muestras')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            
    

