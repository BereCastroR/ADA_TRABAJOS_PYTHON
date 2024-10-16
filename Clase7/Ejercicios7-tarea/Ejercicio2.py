#2Ejercicio Integrador
#1. Usar un bucle for con range para iterar sobre los números del 1 al 20.
#2. Usar continue para saltar los números divisibles por 3.
#3. Usar break para detener la iteración si se encuentra un número mayor que 15.
#4. Crear un set con los números restantes y verificar si algún número es par.
print("Lista completa de números del 1 al 20:")
for numero in range(1, 21):
    print(numero, end=" ")
numeros = set()
for numero in range(1, 21):
    if numero % 3 == 0:
        continue  

    if numero > 15:
        break  

    numeros.add(numero)
print("\nLista de números restantes:", list(numeros))

# Numeros par 
if any(numero % 2 == 0 for numero in numeros):
    print("Sí, hay al menos un número par.")
else:
    print("No hay números pares.")
