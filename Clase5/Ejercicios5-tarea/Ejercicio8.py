# Ejercicio 8: Modificar un valor en un diccionario anidado

nombre_tienda = {
    "nombre_tienda": "Librería Colibrí",
    "libros": [
        {"titulo": "El murmullo de las abejas", "precio": 450},
        {"titulo": "Romper el círculo", "precio": 390},
        {"titulo": "De animales a Dioses", "precio": 378}
    ]
}

# Cambio de precio 
nuevo_precio = 310
nombre_tienda["libros"][1]["precio"] = nuevo_precio

# Título y el precio del segundo libro modificado
segundo_libro = nombre_tienda["libros"][1]
print(f"El título del segundo libro es: {segundo_libro['titulo']}")
print(f"El nuevo precio es: ${segundo_libro['precio']}")
