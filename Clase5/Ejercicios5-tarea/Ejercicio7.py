# Contar ocurrencias de elementos en un diccionario anidado

clubes = {
    "Club A1": [
        {"nombre": "Juan", "edad": 25},
        {"nombre": "Ana", "edad": 22},
        {"nombre": "Pedro", "edad": 28}
    ],
    "Club A2": [
        {"nombre": "María", "edad": 21},
        {"nombre": "Luis", "edad": 26}
    ],
    "Club A3": [
        {"nombre": "Sofía", "edad": 23},
        {"nombre": "David", "edad": 24},
        {"nombre": "Laura", "edad": 25},
        {"nombre": "Luia", "edad": 22}
    ]
}

# Conteo de los jugadores 
for club, jugadores in clubes.items():
    jugadores = len(jugadores)
    print(f"El {club} tiene {jugadores} jugadores en total")
