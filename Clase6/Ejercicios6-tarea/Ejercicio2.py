#Ejercicio de while y for

def calcular_suma():

  print("¡Bienvenido al programa de suma! ")
  print("Por favor ingresa los valores que deseas sumar y presiona '0' para finalizar la suma \n")  
  numeros = []
  numero = 1  

  while numero != 0:
    numero = int(input("Ingrese el valor que desea sumar: "))
    if numero != 0:
      numeros.append(numero)

  suma = 0
  for num in numeros:
    suma += num

  print("El resultado de tu suma es: ", suma)
  
calcular_suma()
