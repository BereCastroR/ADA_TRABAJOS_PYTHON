# Definimos distintas variables para usar en las compraciones
a = 10
b = 5
c = 15
d = 8

# Operador AND
# Ambas condiciones deben ser verdaderas para que el resultado sea TRUE
resultado_and = (a > b) and (c > d)
print(f"Resultado de (a > b) and (c > d): {resultado_and}")
# (a > b) es True porque 10 > 5
# (c > d) es True porque 15 > 8

# Operador OR
# Al menos una de las condiciones se debe cumplir para ser True
resultado_or = (a < b) or (c > d)
print(f"Resultado de (a < b) or (c > d): {resultado_or}")
# (a < b) es False porque 10 no es menor que 5
# (c > d) es True porque 15 > 8

# Operador NOT
# El operador not invierte el valor de la expresion
resultado_not = not (a < b)
print(f"Resultado de not (a < b): {resultado_not}")
# (a < b) es False porque 10 no es menor que 5
# not False resulta en True

# Combinación de los operadores lógicos and, or y not en una sola expresión
resultado_combinado = (a > b) and (not (c < d)) or (b < c)
print(f"Resultado combinado: {resultado_combinado}")