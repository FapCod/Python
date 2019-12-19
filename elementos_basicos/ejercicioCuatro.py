import math
print("Bienvenido al programa \nQue te ayudara a encontrar el \nArea y Longitud de un circulo")
radio=float(input("Ingregese el radio del circulo:"))
area= math.pi*radio**2
longitud=2*math.pi*radio
print(f"El area es {area:.2f}, y su longitud es {longitud:.2f}")
