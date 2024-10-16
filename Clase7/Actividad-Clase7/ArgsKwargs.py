# Ejemplo 1: funcion que usa *args
def sumar_numeros(*args):
    """
    Esta funcion acepta un numero variable de argumentos numericos y retorna su suma.
    :param args: Un numero variable de argumentos numericos.
    :return: La suma de los argumentos
    """
    total = 0
    for numero in args:
        total += numero
    return total

#Llamada a la funcion con diferentes numeros de argumentos
print("Ejemplo de *args:")
print(f"Suma de 1, 2, 3: {sumar_numeros(1, 2, 3)}")
print(f"Suma de 4, 5, 6, 7, 8: {sumar_numeros(4, 5, 6, 7, 8)}")
print()

# Ejemplo 2 - funcion que usa **kwargs
def mostrar_detalles(**kwargs):
    """
    Esta funcion acepta un numero variable de argumentos nombrados clave-valor y los imrpime.
    :param kwargs: Un numero variable de argumentos nombrados (clave-valor)
    """
    print("Detalles:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamada a la funcion con diferentes argumentos nombrados
print("Ejemplo de **kwarsg:")
mostrar_detalles(nombre="Ana", edad=30, ciudad="Madrid")
print()
