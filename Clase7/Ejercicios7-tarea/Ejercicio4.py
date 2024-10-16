#Ejercicio 4 while con Condiciones y Contadores

#1. Use un bucle while para generar números de la serie de Fibonacci.
def generar_fibonacci(limite):
    
    a, b = 0, 1
    fibonacci_list = []
    while b < limite:
        fibonacci_list.append(b)
        a, b = b, a + b
    return fibonacci_list

#2. Continúe generando números hasta que el número actual sea mayor o igual a 100.
resultado = generar_fibonacci(100)

#3. Imprima la serie de Fibonacci generada.
print("Serie de Fibonacci: ")
print(resultado)
