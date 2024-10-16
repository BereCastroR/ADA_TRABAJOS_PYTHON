# Ejemplo de diccionario
diccionario_vacio = {}
print("Ejemplo de un diccionario vacio: ", diccionario_vacio)

# Ejemplo bsaico de un diccionario
persona = {
    "nombre" : "Maria",
    "edad" : 30,
    "casada" : False,
    "hijos" : ["Ana", "Luis"],
    "direccion" : {
        "calle" : "La gran via" ,
        "ciudad" : "Madrid"
    }
}
print("Ejemplo de diccionario basico: ", persona)

# Ejemplo de diccionario con valores de distintos tipos
diccionario_mixto = {
    "nombre" : "Alejandra",
    1: [2, 3, 4], # Clave es un entero y valor es un string
    (2, 3): "Tupla como clave" # Clave es una tupla y valor es un st
}
print("Ejemplo de diccionario mixto: ", diccionario_mixto)
