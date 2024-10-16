#Ejercicio de Sets y for

def procesar_lista(lista_numeros, valor_comparacion):

  #1 Crea un programa que reciba una lista de números y realice las siguientes operaciones
  #Crear un set a partir de una lista para eliminar duplicados
  conjunto_numeros = set(lista_numeros)

  #2 Iterar sobre el set e imprimir cada número
  print("Números únicos en el set: ")
  for numero in conjunto_numeros:
    print(numero)

  #3 Contar cuántos números son mayores que un valor dado y almacenarlos en un nuevo set
  numeros_mayores = set(numero for numero in conjunto_numeros if numero > valor_comparacion)
  print(f"Números mayores a {valor_comparacion}: ")
  print(f"{numeros_mayores}")

  return numeros_mayores
lista_original = [0, 1, 2, 2, 3, 4, 4, 5]
valor_a_comparar = 2

resultado = procesar_lista(lista_original, valor_a_comparar)
