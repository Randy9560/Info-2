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

                    La edad del pasajero es: {self.edad}

                    El pasaporte del pasajero es: {self.pasaporte}

                               """)

pasajero1 = Pasajeros("Randy", "Garcia",15,"PA54684")

#pasajero1.mostarInformacion()


class Vuelo:
    def __init__(self,numeroV,origen,destino,cantidad):
        self.numeroVuelo = numeroV
        self._origen = origen
        self._destino = destino
        self.cantidadA = cantidad
        self.reservasAsientop=[]
        #Hacer dependecia Reserva vuelo
    
    def mostarInformacion(self):
        print(f""" 
                    El vuelo N°: {self.numeroVuelo}

                    Origen:     {self._origen}

                    destino:    {self._destino}

                    Asientos disponibles: {self.cantidadA}

                    """)
    
    def reservaAsiento(self,pasajero): #relacion de asociacion
        if pasajero in self.reservasAsientop:
            print(f"El pasajero {pasajero.nombre} ya tiene una reserva en este vuelo ")
        elif self.cantidadA > 0:
            self.reservasAsientop.append(pasajero)
            self.cantidadA -= 1
            print(f"El pasajero {pasajero.nombre} realizo la reserva exitosamente")
        else: 
            print("No hay asientos disponibles")

    #Hacer el de cancelar asiento 

vuelo1 = Vuelo("HK21685","Medellin","Cartagena",80)

#vuelo1.mostarInformacion()

vuelo1.reservaAsiento(pasajero1)

vuelo1.mostarInformacion()