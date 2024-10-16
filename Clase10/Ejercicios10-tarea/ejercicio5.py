class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.numero_puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada} cc")

# Ejemplo de uso
coche1 = Coche("Toyota", "Corolla", 4)
moto1 = Motocicleta("Honda", "CBR600RR", 600)

coche1.mostrar_info()
print()
moto1.mostrar_info()
