#Ejercicio 5 for con enumerate y break/continue

nombres = ["Ana", "Pedro", "Jesus", "Berenice", "Carlos", "María", "Antonio", "Laura"]

for indice, nombre in enumerate(nombres):
    # 3 Salto si el nombre empieza con A
    if nombre[0] == "A":
        continue

    # 4 Detener la iteración si el nombre es 'Carlos'
    if nombre == "Carlos":
        break
    print(f"Índice: {indice}, Nombre: {nombre}")
