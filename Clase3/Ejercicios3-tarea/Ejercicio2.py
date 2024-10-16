lista_numeros = [1, 16, 25, 3, 7, 95, 30, 25, 25]
print("Lista de numeros: ", lista_numeros)
numero_buscar = int(input('ingrese el número que desea buscar: '))
aparicion_de_num = lista_numeros.count(numero_buscar)

print(f"El numero que buscas aparece {aparicion_de_num} veces")
