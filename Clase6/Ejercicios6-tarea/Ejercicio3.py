#Ejercicio 3
#Escribe un programa que itere sobre una lista de cadenas usando enumerate para mostrar el índice y el valor
#Utilizar continue y break

lista = ["Pato", " ", "Cabra", "León", "Jirafa", " ", "Elefante"]

for indice, palabra in enumerate(lista):
    if palabra == " ":
        continue  # Saltar cadenas vacías
    if len(palabra) > 5:
        break  # Detener si la palabra es muy larga
    print(f"Índice: {indice}, Animal: {palabra}")
