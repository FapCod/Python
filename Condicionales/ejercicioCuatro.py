print("operaciones basicas")
print("Que desea hacer:")
print("S,s-Sumar\nR,r-Restar\nM,m-Multiplicar\nD,d-Dividir")
opcion = input("Ingrese su operacion:")
if opcion=='S' or opcion=='s':
    print("Sumara:")
    num1= float(input("Ingrese el numero1:"))
    num2= float(input("Ingrese el numero2:"))
    suma= num1+num2
    print("La suma es:",suma)
elif opcion=='R' or opcion=='r':
    print("Restara:")
    num1= float(input("Ingrese el numero1:"))
    num2= float(input("Ingrese el numero2:"))
    resta= num1-num2
    print("La suma es:",resta)
elif opcion=='M' or opcion=='m':
    print("Multiplicara:")
    num1= float(input("Ingrese el numero1:"))
    num2= float(input("Ingrese el numero2:"))
    mul= num1*num2
    print("La suma es:",mul)
elif opcion=='D' or opcion=='d':
    print("Dividira:")
    num1= float(input("Ingrese el numero1:"))
    num2= float(input("Ingrese el numero2:"))
    div= num1/num2
    print(f"La suma es:{div:.2f}")
