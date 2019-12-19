print("Ingrese dos numeros")
a=float(input("Ingrese el primer numero A:"))
b=float(input("Ingrese el Segundo numero B:"))
if a%2==0 and b%2==0 :
    print("A Y B es par")
elif a%2==0 and b%2!=0:
    print("A es par")
elif a%2!=0 and b%2==0:
    print("B es par")
else:
    print("Ningun numero es par")
