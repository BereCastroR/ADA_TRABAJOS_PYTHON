# Anidación compleja de diccionarios y listas
escuela = {"nombre" : "Mariano Sanches No.9",
           "año de fundación" : 1450,
           "lista de clases" : [{"clase1" : "matemáticas", 
                                 "estudiantes" : [{"nombre": "Jose María", "edad" : 15},
                                                  {"nombre": "María", "edad" : 16},
                                                  {"nombre": "Pablo", "edad" : 15}]},
                                {"clase2" : "español",
                                  "estudiantes" : [{"nombre": "Jessica", "edad" : 15},
                                                   {"nombre": "Erik", "edad" : 16},
                                                   {"nombre": "Paola", "edad" : 17}]},
                                {"clase3" : "química",
                                  "estudiantes" : [{"nombre": "Omar", "edad" : 14},
                                                   {"nombre": "Kevin", "edad" : 16},
                                                   {"nombre": "Erika", "edad" : 16}]}]
}

#Acceder al primer estudiante de la primera clase

clase1_primer_estudiante = escuela["lista de clases"][0]["estudiantes"][0]
print("Nombre del primer estudiante de la clase1:", clase1_primer_estudiante["nombre"])
