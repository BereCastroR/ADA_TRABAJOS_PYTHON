# Alcance global y local 

# Variable global
x = 20

def funcion_local():
    x = 10 # 'x' es una variable local
    print(f"Valor de x dentro de la funcion local: {x}")

def funcion_global():
    #para modificar una variable global, se usa la palbra clave 'global'
    global x
    x = 30
    print(f"Valor de x dentro dentro de la funcoin global: {x}")

# Llamada a las funciones
funcion_local() #Muestra el valor de x dentro de la funcoin local
#print(x) #Esto causara un error porque x esta definido en el alcance local de la funcion_local()

funcion_global() #Modifica el valor de x en el alcance global
print(f"Valor de x fuera de la funcion: {x}")
