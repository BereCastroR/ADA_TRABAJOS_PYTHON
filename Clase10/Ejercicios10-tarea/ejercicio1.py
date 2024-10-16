class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def aprobo(self):
        promedio = self.calcular_promedio()
        return promedio >= 7  # Puedes ajustar el puntaje mínimo de aprobación aquí

class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_aprobados(self):
        print("Estudiantes aprobados:")
        for estudiante in self.estudiantes:
            if estudiante.aprobo():
                print(f"- {estudiante.nombre}")

# Ejemplo de uso:
curso_programacion = Curso()

estudiante1 = Estudiante("Juan Pérez", 20, [8, 7, 9])
estudiante2 = Estudiante("María López", 19, [6, 5, 4])
estudiante3 = Estudiante("Pedro Gómez", 21, [10, 10, 10])

curso_programacion.agregar_estudiante(estudiante1)
curso_programacion.agregar_estudiante(estudiante2)
curso_programacion.agregar_estudiante(estudiante3)

curso_programacion.mostrar_aprobados()
