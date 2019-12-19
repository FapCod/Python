import math
numero = int(input("Ingrese un numero:"))

while numero<0:
    print("Error ,debe ser positivo")
    numero = int(input("Ingrese un numero:"))

print(f"Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")
