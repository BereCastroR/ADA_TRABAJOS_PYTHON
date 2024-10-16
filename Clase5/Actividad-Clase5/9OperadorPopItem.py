# Crear un diccionario
persona = {
    "nombre" : "Emilia",
    "edad" : 33,
    "ciudad" : "CABA",
    "profesion" : "Veterinaria"
}

# Imprimir el diccionario origial
print("Diccionario original: ", persona)

# Usamos PopItem para eliminar y obtener el ultimo par clave-valor
ultimo_elemento = persona.popitem()

# Imprimimos el par clave-valor
print("Ultimo par clave-valor eliminado: ", ultimo_elemento)

# Imprimimos despues de usar popitem
print("Diccionario despues de usar popitem: ", persona)
