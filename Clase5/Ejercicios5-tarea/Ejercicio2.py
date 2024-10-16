# Modificar y eliminar elementos de un diccionario
libro = {
    "titulo" : "El Principito",
    "autor" : "Antoine de Saint-Exupéry",
    "año" : 1943,
    "genero" : "Literatura infantil"
}

# Imprimimos el diccionario original
print("Diccionario orignial: ", libro)

#Actualización del año de publicación
libro["año"]=1968
print("Diccionario con el año actualizado: ", libro)

# Usamos pop para eliminar "genero"
valor_eliminado = libro.pop("genero")
print("Diccionario despues de eliminar 'genero': ", libro)
