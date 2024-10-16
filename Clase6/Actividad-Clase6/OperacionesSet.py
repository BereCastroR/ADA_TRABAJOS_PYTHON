# Crear conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
conjunto_c = {7, 8, 9}

# Subconjunto
es_subconj = conjunto_a.issubset(conjunto_b)
print(f"Es conjunto_a un subconjunto de conjunto_b?: {es_subconj}")  # da False

# SuperConjunto
es_superconj = conjunto_b.issuperset(conjunto_a)
print(f"Es conjunto_b un superconjunto de conjunto_a?: {es_superconj}") # da False

# Disconjuntos
son_disconj = conjunto_a.isdisjoint(conjunto_c)
print(f"Son conjunto_a y conjunto_c disjuntos?: {son_disconj}") # da True

# Simetria
simetria = conjunto_a.symmetric_difference(conjunto_b)
print(f"Diferencia simetrica entre conjunto_a y conjunto_b: {simetria}") # sale {1, 2, 5, 6}

# Union update
conjunto_a.update(conjunto_b)
print(f"Conjunto_a despues de la union con conjunto_b: {conjunto_a}") # sale {1, 2, 3, 4, 5, 6}

# Interseccion update
conjunto_a.intersection_update(conjunto_b)
print(f"Conjunto_a despues de la interseccion con conjunto_b: {conjunto_a}") # sale {3, 4, 5, 6}

# Difference update
conjunto_b.difference_update(conjunto_c)
print(f"Conjunto_a despues de la diferencia con conjunto_b: {conjunto_b}")

#Symmetric difference
conjunto_a.symmetric_difference_update(conjunto_b)
print(f"Conjunto_a_ despues de la diferencia simetrica con conjunto_b: {conjunto_b}")
