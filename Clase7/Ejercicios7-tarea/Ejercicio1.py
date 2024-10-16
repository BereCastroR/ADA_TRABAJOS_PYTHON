#Ejercicio de List Comprehension con range y for

# Genero mi la lista de números del 1 al 10
numeros = list(range(1, 11))

# Creo la lista de cuadrados de los números impares
cuadrados_impares = [num**2 for num in numeros if num % 2 != 0]

print("Lista de números empleada:", numeros)
print("\nLista de valores al cuadrados que son impares:", cuadrados_impares)
