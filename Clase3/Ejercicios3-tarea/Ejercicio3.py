lista_numeros = [1, 16, 25, 3, 7, 95, 30, 1, 4, 25, 25]
print('Lista de números: ', lista_numeros)

inicio = int(input("Ingrese el índice de inicio de la sublista: "))
fin = int(input("Ingrese el índice de fin de la sublista: "))

sublista = lista_numeros[inicio:fin]
print("La sublista es: ", sublista)

suma = sum(sublista)
print("La suma de la sublista es: ", suma)
