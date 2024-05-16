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
        return f""" Fecha de Revision: {self.fechaRevision},
                    Mantenimiento: {self.mantenimiento},
                    Tiempo de vida util: {self.vidaUtil} """


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
        return f""" \t\tTipo de implante: {MarcapasosCardiacos.tipoImplante},
                    {super().__str__()},
                    Numero de Electrodos: {self.nElectrodos},
                    Tipo de marcapasos: {self.tipo},
                    Frecuencia de estimulacion: {self.fEstimulador}"""  

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
        return f""" Tipo de implante: {StentsCoronarios.tipoImplante},
                    {super().__str__()},
                    Longitud: {self.longitud},
                    Diametro: {self.diametro},
                    Material: {self.material}"""
        

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
        return f""" Tipo de implante: {ImplanteDental.tipoImplante},
                    {super().__str__()},
                    Forma: {self.forma},
                    Material: {self.material},
                    Sistema de Fijacion: {self.sistemaFijacion}"""
    
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
        return f""" Tipo de implante: {ImplanteRodilla.tipoImplante},
                    {super().__str__()},
                    Material: {self.material},
                    Tamaño: {self.tamaño},
                    Tipo de fijacion: {self.tipoFijacion}"""
    
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
        return f""" Tipo de implante: {ImplanteCadera.tipoImplante},
                    {super().__str__()},
                    Material: {self.material},
                    Tamaño: {self.tamaño},
                    Tipo de fijacion: {self.tipoFijacion}"""

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
                                                    6) Salir
                                                                          """))   
        if submenu == 1:
            fechaRevisionmp = input("Ingrese la fecha de revision: ")
            mantenimientomp = input("Ingrese si se ha hecho algun mantenimiento: ")
            nElectrodos = input("Ingrese el numero de electrodos que tiene el marcapasos cardiaco: ")
            tipo = input("Ingrese el tipo de marcapasos cardiaco: ")
            fEstimulador = input("Ingrese la frecuencia del estimulador del marcapasos cardiaco: ")
            VidaUtilmp = input("Ingrese la vida util del marcapasos cardiaco: ")
            marcapasos = MarcapasosCardiacos(fechaRevisionmp,mantenimientomp,nElectrodos,tipo,fEstimulador,VidaUtilmp)

        elif submenu == 2:
            fechaRevisionsc = input("Ingrese la fecha de revision: ")
            mantenimientosc = input("Ingrese si se ha hecho algun mantenimiento: ")
            VidaUtilsc = input("Ingrese la vida util del stent coronario: ")
            longitud = input("Ingrese la longitud: ")
            diametro = input("Ingrese el diametro: ")
            material = input("Ingrese el material: ")
            stentCoronario = StentsCoronarios(fechaRevisionsc,mantenimientosc,longitud,diametro,material,VidaUtilsc)

        elif submenu == 3:
            fechaRevisionid = input("Ingrese la fecha de revision: ")
            mantenimientoid = input("Ingrese si se ha hecho algun mantenimiento: ")
            VidaUtilid = input("Ingrese la vida util del implante dental: ")
            forma = input("Ingrese la forma: ")
            materialid = input("Ingrese el material: ")
            sFijacion = input("Ingrese el sistema de fijacion: ")
            implanteDental1 = ImplanteDental(fechaRevisionid,mantenimientoid,forma,sFijacion,materialid,VidaUtilid)

        elif submenu == 4:
            fechaRevisionir = input("Ingrese la fecha de revision: ")
            mantenimientoir = input("Ingrese si se ha hecho algun mantenimiento: ")
            VidaUtilir = input("Ingrese la vida util del implante de rodilla: ")
            materialir = input("Ingrese el material: ")
            tamañoir = input("Ingrese el tamaño: ")
            tFijacion = input("Ingrese el tipo de fijacion: ")

        elif submenu == 5:
            fechaRevisionic = input("Ingrese la fecha de revision: ")
            mantenimientoic = input("Ingrese si se ha hecho algun mantenimiento: ")
            VidaUtilic = input("Ingrese la vida util del implante de cadera: ")
            materialic = input("Ingrese el material: ")
            tamañoic = input("Ingrese el tamaño: ")
            tFijacionic = input("Ingrese el tipo de fijacion: ")

        elif submenu == 6:
            break

    elif menu == 2:
                
        submenu1 = int(input(""" Seleccione el tipo de implante de interes:

                                                    1) Marcapasos 
                                                    2) Stent coronario
                                                    3) Implante dental
                                                    4) Implante de rodilla
                                                    5) Implante de cadera
                                                                          """))
        if submenu1 == 1:
            for h in Implante.numeroMarcapasos:
                print(f'\tN°: { Implante.numeroMarcapasos.index(h) + 1}, \n{h}')
            eleccion = int(input("\nIngrese el numero de implante que desea eliminar: "))
            eleccion -= 1
            Implante.numeroImplantes.remove(Implante.numeroMarcapasos[eleccion])
            Implante.numeroMarcapasos.pop(eleccion)
            print("-"*50 + "Se ha eliminado exitosamente" + "-"*50)
            # for m in Implante.numeroMarcapasos:
            #     print(m)
        
        elif submenu1 == 2:
            for st in Implante.numero_Stents_Coronarios:
                print(f'\tN°: { Implante.numero_Stents_Coronarios.index(st) + 1}, \n{st}')
            eleccion1 = int(input("\nIngrese el numero de implante que desea eliminar: "))
            eleccion1 -= 1
            Implante.numeroImplantes.remove(Implante.numero_Stents_Coronarios[eleccion1])
            Implante.numero_Stents_Coronarios.pop(eleccion1)
            print("-"*50 + "Se ha eliminado exitosamente" + "-"*50)

        elif submenu1 == 3:
            for id in Implante.numeroDental:
                print(f'\tN°: { Implante.numeroDental.index(id) + 1}, \n{id}')
            eleccion2 = int(input("\nIngrese el numero de implante que desea eliminar: "))
            eleccion2 -= 1
            Implante.numeroImplantes.remove(Implante.numeroDental[eleccion2])
            Implante.numeroDental.pop(eleccion2)
            print("-"*50 + "Se ha eliminado exitosamente" + "-"*50)

        elif submenu1 == 4:
            for ir in Implante.numeroRodilla:
                print(f'\tN°: { Implante.numeroRodilla.index(ir) + 1}, \n{ir}')
            eleccion3 = int(input("\nIngrese el numero de implante que desea eliminar: "))
            eleccion3 -= 1
            Implante.numeroImplantes.remove(Implante.numeroRodilla[eleccion3])
            Implante.numeroRodilla.pop(eleccion3)
            print("-"*50 + "Se ha eliminado exitosamente" + "-"*50)

        elif submenu1 == 5:
            for ic in Implante.numeroCadera:
                print(f'\tN°: { Implante.numeroCadera.index(ic) + 1}, \n{ic}')
            eleccion4 = int(input("\nIngrese el numero de implante que desea eliminar: "))
            eleccion4 -= 1
            Implante.numeroImplantes.remove(Implante.numeroCadera[eleccion4])
            Implante.numeroCadera.pop(eleccion4)
            print("-"*50 + "Se ha eliminado exitosamente" + "-"*50)

    elif menu == 3:
             
        submenu2 = int(input(""" Seleccione el tipo de implante de interes:

                                                    1) Marcapasos 
                                                    2) Stent coronario
                                                    3) Implante dental
                                                    4) Implante de rodilla
                                                    5) Implante de cadera
                                                                          """))  
        if submenu2 == 1:
            for mp in Implante.numeroMarcapasos:
                print(f'\tN°: { Implante.numeroMarcapasos.index(mp) + 1}, \n{mp}')
            opcion = int(input("\nIngrese el numero de implante que desea editar: "))
            opcion -= 1
            print(Implante.numeroMarcapasos[opcion])
            edicion = int(input("""" \nSeleccione el dato que desea actualizar:

                                                    1) Fecha de revision 
                                                    2) Mantenimiento
                                                    3) Numero de electrodos
                                                    4) Tipo
                                                    5) Frecuencia del estimulador
                                                    6) Vida util
                                                                          """))
            if edicion == 1:
                nuevaFecha = input("Ingrese la nueva fecha de revision: ")
                Implante.numeroMarcapasos[opcion].fechaRevision = nuevaFecha
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion == 2:
                nuevoMantenimiento = input("Ingrese el nuevo dato de mantenimiento: ")
                Implante.numeroMarcapasos[opcion].mantenimiento = nuevoMantenimiento
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion == 3:
                nuevoElectrodo = input("Ingrese el nuevo numero de Electrodo: ")
                Implante.numeroMarcapasos[opcion].nElectrodos = nuevoElectrodo
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion == 4:
                nuevoTipo = input("Ingrese el nuevo tipo: ")
                Implante.numeroMarcapasos[opcion].tipo = nuevoTipo
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion == 5: 
                nuevafEstimulador = input("Ingrese la nueva frecuencia del estimulador: ")
                Implante.numeroMarcapasos[opcion].fEstimulador = nuevafEstimulador
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion == 6:
                nuevavUtil = input("Ingrese la nueva vida util: ")
                Implante.numeroMarcapasos[opcion].vidaUtil = nuevavUtil
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            #   longitud, diametro, material   
        if submenu2 == 2:
            for sc in Implante.numero_Stents_Coronarios:
                print(f'\tN°: { Implante.numero_Stents_Coronarios.index(sc) + 1}, \n{sc}')
            opcion1 = int(input("\nIngrese el numero de implante que desea editar: "))
            opcion1 -= 1
            print(Implante.numero_Stents_Coronarios[opcion1])
            edicion1 = int(input("""" \nSeleccione el dato que desea actualizar:

                                                    1) Fecha de revision 
                                                    2) Mantenimiento
                                                    3) Longitud
                                                    4) Diametro
                                                    5) Material
                                                    6) Vida util
                                                                          """))
            if edicion1 == 1:
                nuevaFecha1 = input("Ingrese la nueva fecha de revision: ")
                Implante.numero_Stents_Coronarios[opcion1].fechaRevision = nuevaFecha1
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion1 == 2:
                nuevoMantenimiento1 = input("Ingrese el nuevo dato de mantenimiento: ")
                Implante.numero_Stents_Coronarios[opcion1].mantenimiento = nuevoMantenimiento1
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion1 == 3:
                nuevaLongitud = input("Ingrese la nueva longitud: ")
                Implante.numero_Stents_Coronarios[opcion1].longitud = nuevaLongitud
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion1 == 4:
                nuevoDiametro = input("Ingrese el nuevo diametro: ")
                Implante.numero_Stents_Coronarios[opcion1].diametro = nuevoDiametro
            elif edicion1 == 5: 
                nuevoMaterial = input("Ingrese el nuevo material: ")
                Implante.numero_Stents_Coronarios[opcion1].material = nuevoMaterial
            elif edicion1 == 6:
                nuevavUtil1 = input("Ingrese la nueva vida util: ")
                Implante.numero_Stents_Coronarios[opcion1].vidaUtil = nuevavUtil1
#  forma, sistemaFijacion, material
        if submenu2 == 3:
            for idd in Implante.numeroDental:
                print(f'\tN°: { Implante.numeroDental.index(idd) + 1}, \n{idd}')
            opcion2 = int(input("\nIngrese el numero de implante que desea editar: "))
            opcion2 -= 1
            print(Implante.numeroDental[opcion2])
            edicion2 = int(input("""" \nSeleccione el dato que desea actualizar:

                                                    1) Fecha de revision 
                                                    2) Mantenimiento
                                                    3) Forma
                                                    4) Sistema de Fijacion
                                                    5) Material
                                                    6) Vida util
                                                                          """))
            if edicion2 == 1:
                nuevaFecha2 = input("Ingrese la nueva fecha de revision: ")
                Implante.numeroDental[opcion2].fechaRevision = nuevaFecha2
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion2 == 2:
                nuevoMantenimiento2 = input("Ingrese el nuevo dato de mantenimiento: ")
                Implante.numeroDental[opcion2].mantenimiento = nuevoMantenimiento2
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion2 == 3:
                nuevaForma = input("Ingrese la nueva forma: ")
                Implante.numeroDental[opcion2].forma = nuevaForma
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion2 == 4:
                nuevosFijacion = input("Ingrese el nuevo sistema de fijacion: ")
                Implante.numeroDental[opcion2].sistemaFijacion = nuevosFijacion
            elif edicion2 == 5: 
                nuevoMaterial1 = input("Ingrese el nuevo material: ")
                Implante.numeroDental[opcion2].material = nuevoMaterial1
            elif edicion2 == 6:
                nuevavUtil2 = input("Ingrese la nueva vida util: ")
                Implante.numeroDental[opcion2].vidaUtil = nuevavUtil2
# material, tipoFijacion, tamaño
        if submenu2 == 4:
            for irr in Implante.numeroRodilla:
                print(f'\tN°: { Implante.numeroRodilla.index(irr) + 1}, \n{irr}')
            opcion3 = int(input("\nIngrese el numero de implante que desea editar: "))
            opcion3 -= 1
            print(Implante.numeroRodilla[opcion3])
            edicion3 = int(input("""" \nSeleccione el dato que desea actualizar:

                                                    1) Fecha de revision 
                                                    2) Mantenimiento
                                                    3) Tamaño
                                                    4) Tipo de Fijacion
                                                    5) Material
                                                    6) Vida util
                                                                          """))
            if edicion3 == 1:
                nuevaFecha3 = input("Ingrese la nueva fecha de revision: ")
                Implante.numeroRodilla[opcion3].fechaRevision = nuevaFecha3
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion3 == 2:
                nuevoMantenimiento3 = input("Ingrese el nuevo dato de mantenimiento: ")
                Implante.numeroRodilla[opcion3].mantenimiento = nuevoMantenimiento3
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion3 == 3:
                nuevatamaño = input("Ingrese el nuevo tamaño: ")
                Implante.numeroRodilla[opcion3].tamaño = nuevatamaño
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion3 == 4:
                nuevotFijacion = input("Ingrese el nuevo tipo de fijacion: ")
                Implante.numeroRodilla[opcion3].tipoFijacion = nuevotFijacion
            elif edicion3 == 5: 
                nuevoMaterial2 = input("Ingrese el nuevo material: ")
                Implante.numeroRodilla[opcion3].material = nuevoMaterial2
            elif edicion3 == 6:
                nuevavUtil3 = input("Ingrese la nueva vida util: ")
                Implante.numeroRodilla[opcion3].vidaUtil = nuevavUtil3
# material, tipoFijacion, tamaño
        if submenu2 == 5:
            for icc in Implante.numeroCadera:
                print(f'\tN°: { Implante.numeroCadera.index(icc) + 1}, \n{icc}')
            opcion4 = int(input("\nIngrese el numero de implante que desea editar: "))
            opcion4 -= 1
            print(Implante.numeroCadera[opcion4])
            edicion4 = int(input("""" \nSeleccione el dato que desea actualizar:

                                                    1) Fecha de revision 
                                                    2) Mantenimiento
                                                    3) Tamaño
                                                    4) Tipo de Fijacion
                                                    5) Material
                                                    6) Vida util
                                                                          """))
            if edicion4 == 1:
                nuevaFecha4 = input("Ingrese la nueva fecha de revision: ")
                Implante.numeroCadera[opcion4].fechaRevision = nuevaFecha4
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion4 == 2:
                nuevoMantenimiento4 = input("Ingrese el nuevo dato de mantenimiento: ")
                Implante.numeroCadera[opcion4].mantenimiento = nuevoMantenimiento4
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion4 == 3:
                nuevatamaño1 = input("Ingrese el nuevo tamaño: ")
                Implante.numeroCadera[opcion4].tamaño = nuevatamaño1
                print("-"*50 + "Se ha editado exitosamente" + "-"*50)
            elif edicion4 == 4:
                nuevotFijacion1 = input("Ingrese el nuevo tipo de fijacion: ")
                Implante.numeroCadera[opcion4].tipoFijacion = nuevotFijacion1
            elif edicion4 == 5: 
                nuevoMaterial3 = input("Ingrese el nuevo material: ")
                Implante.numeroCadera[opcion4].material = nuevoMaterial3
            elif edicion4 == 6:
                nuevavUtil4 = input("Ingrese la nueva vida util: ")
                Implante.numeroCadera[opcion4].vidaUtil = nuevavUtil4

    elif menu == 4:
        for j in Implante.numeroImplantes:
            print(j)            


    elif menu == 5:
        print()
        break