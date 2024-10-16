#Diccionario dentro de una lista

productos = [{"nombre" : "jabon liquido", "precio" : 175, "cantidad en stock" : 35},
             {"nombre" : "shampo", "precio" : 190, "cantidad en stock" : 40},
             {"nombre" : "desodorante", "precio" : 45, "cantidad en stock" : 45},
             {"nombre" : "acondicionador", "precio" : 150, "cantidad en stock" : 20}
]

producto = productos[1]
nombre_producto = producto.get("nombre")
precio_producto = producto.get("precio")

print(f"El segundo producto de la lista es: {nombre_producto} y cuesta: ${precio_producto} MXN")
