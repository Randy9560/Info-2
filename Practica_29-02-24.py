class Pasajeros:
    def __init__(self, nombre, apellido, edad, pasaporte):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.pasaporte = pasaporte

    def mostarInformacion(self):
        print(f""" 
                    El nombre del pasajer es: {self.nombre}

                    El apellido del pasajero es: {self.apellido}

                    La edad del pasajero es: {self.edad} años

                    El pasaporte del pasajero es: {self.pasaporte}

                               """)

# pasajero2.mostarInformacion()


class Vuelo:
    def __init__(self,numeroV,origen,destino,cantidad):
        self.numeroVuelo = numeroV
        self._origen = origen
        self._destino = destino
        self.cantidadA = cantidad
        self.reservasAsientop=[]
        reservaVuelo.adicionVuelos(self)
        #Hacer dependecia Reserva vuelo(Ya esta hecha)
    
    def mostarInformacion(self):
        return f""" 
                    El vuelo N°: {self.numeroVuelo}

                    Origen:     {self._origen}

                    destino:    {self._destino}

                    Asientos disponibles: {self.cantidadA}

                    """
    
    def reservaAsiento(self,pasajero): #relacion de asociacion
        if pasajero in self.reservasAsientop:
            print(f"El pasajero {pasajero.nombre} ya tiene una reserva en este vuelo ")
        elif self.cantidadA > 0:
            self.reservasAsientop.append(pasajero)
            self.cantidadA -= 1
            print(f"El pasajero {pasajero.nombre} realizo la reserva exitosamente")
        else: 
            print("No hay asientos disponibles")

    #Hacer el de cancelar asiento(Ya esta hecho) 
    def removerAsiento(self,pasajero):
        if pasajero in self.reservasAsientop:
            self.reservasAsientop.remove(pasajero)
            self.cantidadA += 1
            print(f"se ha eliminado la reserva del pasajero '{pasajero.nombre}' del vuelo N° '{self.numeroVuelo}")
        else:
            print(f"No se ha encontrado ninguna reserva a nombre de '{pasajero.nombre}'. Por favor vuelva a intentar")
  

class reservaVuelo:

    listaVuelos=[]

    def __init__(self,aereolinia): 
        self.nombreAereolinia = aereolinia

    @classmethod
    def adicionVuelos(cls,vuelo):
        if vuelo in cls.listaVuelos:
            print(f"El vuelo con N° '{vuelo.numeroVuelo}' ya se ha agreagado")
        else:
            cls.listaVuelos.append(vuelo)
            print(f"El vuelo con N° '{vuelo.numeroVuelo}' ha sido añadido correctamente")

    def busquedaVuelo(self,numero): #Validar cuando no hay un vuelo(Hacer)
        for i in reservaVuelo.listaVuelos:
            if i.numeroVuelo == numero:
                print(f"Vuelo encontrado")
                return i.mostarInformacion()
          
    def vuelosDisponibles(self):
        for j in reservaVuelo.listaVuelos:
            # print(j.numeroVuelo)
            # print("Los vuelos disponibles son: ")
            print(j.mostarInformacion())

    def realizarReserva(self, pasajero, vuelo):
        return vuelo.reservaAsiento(pasajero)

    def cancelarReserva(self, pasajero, vuelo):
        return vuelo.removerAsiento(pasajero) 
    
pasajero1 = Pasajeros("Randy", "Garcia",15,"PA54684")

pasajero2 = Pasajeros("Juan","Perez",42,"PO25542")

pasajero3 = Pasajeros("Juana","Lopez",21,"PI635542")

# vuelo1.reservaAsiento(pasajero2)

# vuelo1.reservaAsiento(pasajero1)

# vuelo1.removerAsiento(pasajero3)

# vuelo1.mostarInformacion()

# for pasajero in vuelo1.reservasAsientop:
#     print(pasajero.nombre)

vuelo1 = Vuelo("HK21685","Medellin","Cartagena",80)

vuelo2 = Vuelo("KJ52465","Medellin", "Bogota",32)

latam = reservaVuelo("Latam")

# latam.busquedaVuelo("HK21685")
# # print(latam.nombreAereolinia)

# latam.realizarReserva(pasajero1,vuelo1)

latam.vuelosDisponibles()