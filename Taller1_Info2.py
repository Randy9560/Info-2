class Implante:
    numeroImplantes = []

    numeroMarcapasos = []

    numero_Stents_Coronarios = []

    numeroDental = []

    numeroRodilla = []

    numeroCadera = []

    def __init__(self,fechaRevision, mantenimiento, vidaUtil):
        self.__fechaRevision = fechaRevision
        self.__mantenimiento = mantenimiento
        self.__vidaUtil = vidaUtil

    @property
    def fechaRevision(self):
        return self.__fechaRevision

    @fechaRevision.setter
    def fechaRevision(self, fecha):
        self.__fechaRevision = fecha

    @property
    def mantenimiento(self):
        return self.__mantenimiento
    
    @mantenimiento.setter
    def mantenimiento(self,bol):
        self.__mantenimiento = bol

    @property
    def vidaUtil(self):
        return self.__vidaUtil
    
    @vidaUtil.setter
    def vidaUtil(self, tiempo):
        self.__vidaUtil= tiempo

    @property
    def tipoImplante(self):
        return self.__tipoImplante
    @tipoImplante.setter
    def tipoImplante(self, tipoim):
        self.__tipoImplante = tipoim

    def __str__(self):
        return f" Fecha de Revision: {self.fechaRevision}, Mantenimiento: {self.mantenimiento}, Tiempo de vida util: {self.vidaUtil} "


    @classmethod
    def adicionarImplante(cls, implante):
        if implante in cls.numeroImplantes:
            print("El implante ya ha sido creado")
        else:
            cls.numeroImplantes.append(implante)

    @classmethod
    def adicionarMarcapasos(cls, implante):
        if implante in cls.numeroMarcapasos:
            print("El implante ya ha sido creado")
        else:
            cls.numeroMarcapasos.append(implante)
    
    @classmethod
    def adicionarStens(cls, implante):
        if implante in cls.numero_Stents_Coronarios:
            print("El implante ya ha sido creado")
        else:
            cls.numero_Stents_Coronarios.append(implante)

    @classmethod
    def adicionarDental(cls, implante):
        if implante in cls.numeroDental:
            print("El implante ya ha sido creado")
        else:
            cls.numeroDental.append(implante)

    @classmethod
    def adicionarRodilla(cls, implante):
        if implante in cls.numeroRodilla:
            print("El implante ya ha sido creado")
        else:
            cls.numeroRodilla.append(implante)
    
    @classmethod
    def adicionarCadera(cls, implante):
        if implante in cls.numeroCadera:
            print("El implante ya ha sido creado")
        else:
            cls.numeroCadera.append(implante)    

class MarcapasosCardiacos(Implante):
    tipoImplante = 'Marcapasos Cardiaco'

    def __init__(self, fechaRevision, mantenimiento, nElectrodos, tipo, fEstimulador, vidaUtil):
        super().__init__(fechaRevision, mantenimiento, vidaUtil)
        self.__nElectrodos = nElectrodos
        self.__tipo = tipo
        self.__fEstimulador = fEstimulador
        Implante.adicionarImplante(self)
        Implante.adicionarMarcapasos(self)
        

    @property
    def nElectrodos(self):
        return self.__nElectrodos
    @nElectrodos.setter
    def nElectrodos(self, numero):
        self.__nElectrodos = numero

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo

    @property
    def fEstimulador(self):
        return self.__fEstimulador
    @fEstimulador.setter
    def fEstimulador(self, frecuencia):
        self.__fEstimulador = frecuencia

    def __str__(self):
        return f'Tipo de implante: {MarcapasosCardiacos.tipoImplante}, {super().__str__()}, Numero de Electrodos: {self.nElectrodos}, Tipo de marcapasos: {self.tipo}, Frecuencia de estimulacion: {self.fEstimulador}'  

class StentsCoronarios(Implante):
    tipoImplante = 'Stent coronario'

    def __init__(self, fechaRevision, mantenimiento, longitud, diametro, material, vidaUtil):
        super().__init__(fechaRevision, mantenimiento, vidaUtil)
        self.__longitud = longitud
        self.__diametro = diametro
        self.__material = material
        Implante.adicionarImplante(self)
        Implante.adicionarStens(self)

    @property
    def longitud(self):
        return self.__longitud
    @longitud.setter
    def longitud(self, longitud):
        self.__longitud = longitud

    @property
    def diametro(self):
        return self.__diametro
    @diametro.setter
    def diametro(self, diametro):
        self.__diametro = diametro

    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self, material):
        self.__material = material

    def __str__(self):
        return f'Tipo de implante: {StentsCoronarios.tipoImplante}, {super().__str__()}, Longitud: {self.longitud}, Diametro: {self.diametro}, Material: {self.material}'
        

class ImplanteDental(Implante):
    tipoImplante= 'Implante dental'

    def __init__(self, fechaRevision, mantenimiento, forma, sistemaFijacion, material, vidaUtil):
        super().__init__(fechaRevision, mantenimiento, vidaUtil)
        self.__forma = forma
        self.__sistemaFijacion = sistemaFijacion
        self.__material = material
        Implante.adicionarImplante(self)
        Implante.adicionarDental(self)

    @property
    def forma(self):
        return self.__forma
    @forma.setter
    def forma(self, forma):
        self.__forma = forma

    @property
    def sistemaFijacion(self):
        return self.__sistemaFijacion
    @sistemaFijacion.setter
    def sistemaFijacion(self, sf):
        self.__sistemaFijacion = sf 

    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self, material):
        self.__material = material
        
    def __str__(self):
        return f'Tipo de implante: {ImplanteDental.tipoImplante}, {super().__str__()}, Forma: {self.forma}, Material: {self.material}, Sistema de Fijacion: {self.sistemaFijacion}'
    
class ImplanteRodilla(Implante):
    tipoImplante = 'Implante de rodilla'
    
    def __init__(self, fechaRevision, mantenimiento, material, tipoFijacion, tamaño, vidaUtil):
        super().__init__(fechaRevision, mantenimiento, vidaUtil)
        self.__material = material
        self.__tipoFijacion = tipoFijacion
        self.__tamaño = tamaño
        Implante.adicionarImplante(self)
        Implante.adicionarRodilla(self)

    @property
    def tipoFijacion(self):
        return self.__tipoFijacion
    @tipoFijacion.setter
    def tipoFijacion(self, tfijacion):
        self.__tipoFijacion = tfijacion

    @property
    def tamaño(self):
        return self.__tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self.__tamaño = tamaño

    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self, material):
        self.__material = material

    def __str__(self):
        return f'Tipo de implante: {ImplanteRodilla.tipoImplante}, {super().__str__()}, Material: {self.material}, Tamaño: {self.tamaño}, Tipo de fijacion: {self.tipoFijacion}'
    
class ImplanteCadera(Implante):
    tipoImplante = 'Implante de cadera'
    def __init__(self, fechaRevision, mantenimiento, material, tipoFijacion, tamaño, vidaUtil):
        super().__init__(fechaRevision, mantenimiento, vidaUtil)
        self.material = material
        self.tamaño = tamaño
        self.tipoFijacion = tipoFijacion
        Implante.adicionarImplante(self)
        Implante.adicionarCadera(self)

    @property
    def tipoFijacion(self):
        return self.__tipoFijacion
    @tipoFijacion.setter
    def tipoFijacion(self, tfijacion):
        self.__tipoFijacion = tfijacion

    @property
    def tamaño(self):
        return self.__tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self.__tamaño = tamaño

    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self, material):
        self.__material = material

    def __str__(self):
        return f'Tipo de implante: {ImplanteCadera.tipoImplante}, {super().__str__()}, Material: {self.material}, Tamaño: {self.tamaño}, Tipo de fijacion: {self.tipoFijacion}'

# negra = MarcapasosCardiacos("17-2-20",'si',5,"nose",'hola','6 meses')

# print(negra)

while True:

    menu = int(input( """ Seleccione una opcion:
                        
                                1) Agregar nuevo implante.
                                2) Eliminar un implante.
                                3) Editar informacion de un implante.
                                4) Visualizar el inventario completo
                                5) Salir
                                                    
                                                                """))
    if menu == 1:
        
        submenu = int(input(""" Seleccione el tipo de implante de interes:

                                                    1) Marcapasos 
                                                    2) Stent coronario
                                                    3) Implante dental
                                                    4) Implante de rodilla
                                                    5) Implante de cadera
                                                                          """))
        
        if submenu == 1: 
            pass


    elif menu == 5:
        print()
        break