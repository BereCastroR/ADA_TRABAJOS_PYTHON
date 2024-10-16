# Ejercicio 4: Manipulacion de tuplas y comprobación de índices

frutas = ("manzana", "banana", "cereza")

posicion_banana = frutas.index("banana")
print(f"La fruta 'banana' se encuentra en la posicion: {posicion_banana}" )

fruta_buscada = "naranja"

if fruta_buscada in frutas:
    indice = frutas.index(fruta_buscada)
    print(f"La fruta {fruta_buscada} esta presente en la tupla")
else:
    print(f"La fruta {fruta_buscada} no esta presente en la tupla")
