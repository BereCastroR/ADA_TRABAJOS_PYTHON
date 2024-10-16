# Anidación básica de diccionarios
persona = {
    "nombre" : "Berenice Castro",
    "edad" : 30,
    "direccion" : {
        "calle" : "Neptuno",
        "numero" : 106,
        "colonia" : "Villas del Sol II",
        "codigo postal" : 22842,
        "ciudad" : "Ensenada"
    }
}
print("La ciudad donde vive es: ",persona["direccion"]["ciudad"])
