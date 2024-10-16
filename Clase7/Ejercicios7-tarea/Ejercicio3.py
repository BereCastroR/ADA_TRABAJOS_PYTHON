#Ejercicio 3

#1. Dos sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

#2.1 Operación-Unión
union_sets = set1.union(set2)
print("Unión:", union_sets)

#2.2 Operación-intersección
interseccion_sets = set1.intersection(set2)
print("Intersección:", interseccion_sets)

#2.3 Operación-diferencia
diferencia_set1 = set1.difference(set2)
print("Diferencia (set1 - set2):", diferencia_set1)

#Impresión de resultados
diferencia_set2 = set2.difference(set1)
print("Diferencia (set2 - set1):", diferencia_set2)
