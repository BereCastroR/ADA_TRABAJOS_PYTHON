# Definicion de una funcion que utiliza parametros posicionales, con nombre y predeterminadas
def presentar_persona(nombre, edad, ciudad="Desconocida", profesion="Desconocida"):
    """_summary_

    Parametros:
        nombre: (str) Nombre de la persona
        edad (int): Edad de la persona
        ciudad (str, optional): Ciudad donde vive la persona. Defaults to "Desconocida".
        pofesion (str, optional): Profesion de la persona. Defaults to "Desconocida".
    """
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Profesion: {profesion}")
    print() # Linea en blanco para separar la salida de diferentes llamados a la funcion

# Ejemplos de llamado a la funcion
    
# Usando argumentos posicionales
print("Ejemplo con argumentos posicionales:")
presentar_persona("Ana", 30) # "Ciudad" y "Profesion" usaran el valor predeterminado

# Usando argumentos posicionales y con nombre
print("Ejemplo con argumentos posicionales y con nombre:")
presentar_persona("Luis", 25, ciudad="Madrid", profesion="Ingeniero")
# Nombre y edad son posicionales, ciudad y profesion son con nombre

# Usando todos los argumentos con nombre:
print("Ejemplo con todos los argumentos con nombre:")
presentar_persona(nombre="Marta", edad=28, ciudad="Barcelona", profesion="Diseñadora")

# Usando argumentos posicionales y un argumento con nombre
print("Ejemplo con argumentos posicionales y un argumento con nombre:")
presentar_persona("Carlos", 35, profesion="Profesor")
