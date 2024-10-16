# Programa para adivinar un numero secreto

#Definimos el numero secreto
numero_secreto = 7

# Inicializar la variable para almacenar el numero del usuario
numero_adivinado = None

# Mostrar mensaje inicial
print(f"Adivina el numero secreto (entre 1 y 10): ")

# Bucle While que continua hasta que el usuario adivine el numero secreto
while numero_adivinado != numero_secreto:
    #solicitar al usuario que ingrese un numero
    numero_adivinado = int(input("Introduce tu numero: "))

    #Comprobar si el numero adivinado es correcto
    if numero_adivinado < numero_secreto:
        print("Demesiado bajo. Intenta de nuevo.")
    elif numero_adivinado > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("Felicidades! Has adivinado el numero secreto.")

# Mensaje de finalizacion del juego
print("Gracias por jugar!")
