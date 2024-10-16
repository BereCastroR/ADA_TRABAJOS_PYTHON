class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"Habitación {self.numero} liberada.")
        else:
            print(f"Habitación {self.numero} ya está libre.")

class Hotel:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def reservar_habitacion(self, numero_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                habitacion.reservar()
                return
        print(f"No se encontró la habitación {numero_habitacion}.")

    def cancelar_reserva(self, numero_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                habitacion.liberar()
                return
        print(f"No se encontró la habitación {numero_habitacion}.")

    def mostrar_disponibles(self):
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if not habitacion.ocupada:
                print(f"- Habitación {habitacion.numero} ({habitacion.tipo}, ${habitacion.precio})")

# Ejemplo de uso:
hotel = Hotel()

habitacion1 = Habitacion(101, "Sencilla", 50)
habitacion2 = Habitacion(202, "Doble", 80)
habitacion3 = Habitacion(303, "Suite", 150)

hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)
hotel.agregar_habitacion(habitacion3)

hotel.reservar_habitacion(202)
hotel.mostrar_disponibles()
hotel.cancelar_reserva(202)
hotel.mostrar_disponibles()
