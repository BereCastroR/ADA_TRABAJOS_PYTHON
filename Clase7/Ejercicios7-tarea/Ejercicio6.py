#6. Ejercicio de List Comprehension y range

#1. Use range para generar una lista de números del 1 al 15.
numeros = list(range(1, 16))

#2. Utilice list comprehension para crear una nueva lista con el cubo de los números pares.
cubos_pares = [num**3 for num in numeros if num % 2 == 0]

print("Esta es la lista de números empleada:\n", numeros)
print("\nEsta es la lista de números al cubo que son pares \n", cubos_pares)
