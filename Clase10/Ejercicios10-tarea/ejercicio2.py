import math

class Forma:
    def area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio**2

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return 0.5 * self.base * self.altura

# Crear una lista de formas
formas = [
    Rectangulo(5, 3),
    Circulo(2),
    Triangulo(4, 6)
]

# Calcular y mostrar el área de cada forma
for forma in formas:
    print(f"El área de la forma es: {forma.area()}")
