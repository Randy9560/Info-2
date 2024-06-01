from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QPushButton, QTableWidgetItem, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from controlador import userController, PatientsController

import sys 

class Login(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('login.ui', self)
        self.userController = userController()
        self.setup()

    def setup(self): 
        self.LoginBottom.clicked.connect(self.login) 
        self.password.setEchoMode(QLineEdit.Password)

    def login(self):
        usuario = self.user.text()
        contrasena = self.password.text()
        existe = self.userController.log_in(usuario, contrasena)
        if isinstance(existe, tuple):
            self.PacienteView = PacientesView()
            self.PacienteView.show()
            self.close()

        elif existe == 0:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("No existe un usuario con los \ndatos proporcionados")
            msgBox.setWindowTitle('Datos incorrectos')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

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

class PacientesView(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('pacientes.ui', self)

        self.PatientsController = PatientsController()
        self.setup()
        
    def setup(self):
        validator = QtGui.QIntValidator(1, 9999999, self)
        self.tableView.verticalHeader().setVisible(False)
        self.Ingreso.clicked.connect(self.newPatient)
        self.buscar.clicked.connect(self.filterPatient)
        self.id.setValidator(validator)
        self.salir.clicked.connect(self.logout)
        self.age.setValidator(validator)
        self.readPatient()
        self.tableUpdate()
        
    def logout (self):
        self.PrincipalView = Login()
        self.PrincipalView.show()
        self.close()
        
    def readPatient(self):
        self.listaPacientes = self.PatientsController.getPatient()
        
    def filterPatient(self):
        buscar = self.idbuscar.text()
        self.listaPacientes = self.PatientsController.getPatient(buscar)
        self.tableUpdate()
        
    def newPatient(self):
        id = self.id.text()
        nombre = self.name.text()
        apellido = self.lastname.text()
        edad = self.age.text()
        if not id or not nombre or not apellido or not edad:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Debe ingresar todos los datos")
            msgBox.setWindowTitle('Datos faltantes')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            isUnique = self.PatientsController.newPatient(nombre, apellido, id, edad)
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
                self.id.setText('')
                self.name.setText('')
                self.lastname.setText('')
                self.age.setText('')
            
                        
    def tableUpdate(self):
        self.tableView.setRowCount(len(self.listaPacientes)) 
        self.tableView.setColumnCount(5) 
        columnas = ["Nombre", "Apellido", "Edad", "ID", "Eliminar"]
        columnLayout = ['Nombre','Apellido','Edad','Identificacion']
        self.tableView.setHorizontalHeaderLabels(columnas)
        for row, paciente in enumerate(self.listaPacientes):
            for column in range(4):
                item = QTableWidgetItem(paciente[columnLayout[column]])
                self.tableView.setItem(row, column, item)
            
            btn = QPushButton('Borrar', self)
            btn.clicked.connect(lambda ch, r=row: self.Eliminar(r))
            self.tableView.setCellWidget(row, 4, btn)
                
        self.tableView.setColumnWidth(0, 100)  
        self.tableView.setColumnWidth(1, 100)  
        self.tableView.setColumnWidth(2, 100)  
        self.tableView.setColumnWidth(3, 100)  
        self.tableView.setColumnWidth(4, 100)  

    def Eliminar(self, row):
        id = self.tableView.item(row, 3).text()
        deleted = self.PatientsController.delPatient(id)
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
            
