# Ejercicio 2: Verificacón de elementos en una tupla

mi_tupla = (3, 6, 9, 12, 15)

valor_buscado = 6

if valor_buscado in mi_tupla:
    indice = mi_tupla.index(valor_buscado)
    print(f"El número {valor_buscado} esta presente en la tupla")
else:
    print("El número {valor_buscado} no esta presente en la tupla")
