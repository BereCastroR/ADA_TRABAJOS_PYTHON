# Ejemplo basico de un generador
# Genrador que produce numeros del 1 al 5
# Definicion del generador (sintaxis)
def contador():
    # itera sobre los num del 1 al 5
    for i in range(1,6):
        yield i #produce el valor de i y pausa la ejecucuion
        
# crear una instancia para el generador
gen = contador() # gen es un objeto generador

#Iterar sobre os valores producidos por el mismo generador
for numero in gen:
    print(numero) #IMprimer cada uno de los numeros producidos por el generador
    print()

# Ejemplo de fibonacci
def fibonacci():
    a,b = 0,1 #inicializa los primeros dos numeros de la secuencia
    while True: #ciclo infinito para generar los numeros
        yield a #produce el valor de a y pausa la ejecucion
        a, b = b, a + b #actualiza a y b para la siguient iteracion        
gen = fibonacci() #gen es un objeto generador que produce numeros de fibonacci

# Obtener los primeros 10 numeros de fibonacci
for _ in range(10):
    print(next(gen)) #obtiene el siguiente numero en la secuencia y lo imprime
