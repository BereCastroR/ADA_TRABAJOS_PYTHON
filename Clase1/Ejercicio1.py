# 1. Declaración de Variables y Constantes
edad = 25                # Número
nombre = "Ana"           # Cadena de texto (string)
esta_estudiando = True   # BooLeano 

# Declaración de constantes
PI = 3.14                # Número
PAIS = "Argentina"       # Cadena de texto (String)

# 2. Leer Valores por teclado
edad = int(input("Introduce tu edad: "))   #Leer un número entero
nombre = input("Introduce tu nombre: ")    #Leer una cadena de texto
esta_estudiando = input("¿Estás estudiando? (si/no): ").lower() == "sí"  # leer y convertir a booleano

# 3. Tipo de datos
cantidad_de_libros = 10
titulo_libro = "El Principito"
es_interesante = True
temas = ["Aventura", "Fantasia", "Filosofía"]  #Lista (Array)
autor = { 
    "nombre", "Antonie de Saint-Exupéry",
     "nacionalidad", "Francesa"
}   

# Convertir tipos de datos
edad_str = str(edad)
cantidad_de_libros_float = float(cantidad_de_libros)

# 4. Imprimir Resultados en la consola
print("Nombre: ",nombre)
print("Edad: ", edad)
print("¿Está estudiando?", esta_estudiando)
print("Constante PI", PI)
print("Constante País: ", PAIS)
print("Cantidad de libros: ", cantidad_de_libros)
print("Título del libro: ", titulo_libro)
print("¿Es interesante?", es_interesante)
print("Temas de libro: ", temas)
print("Autor del libro: ", autor)
print("Edad (como cadena de texto): ", edad_str)
print("Cantidad de libros (como float): ", cantidad_de_libros_float)

