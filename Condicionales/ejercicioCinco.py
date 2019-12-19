saldo=1000

print("\t\t'Menu'")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

opc = int (input("digite una opcion del menu:"))
print()
if opc==1:
    extra =float (input("cuanto dinero quiere ingresar--->"))
    saldo += extra
    print(f"Su saldo es de: {saldo} ")
elif opc==2:
    retiro=float(input("cuanto dinero desea retirar --->"))
    if retiro>saldo or saldo<=0:
         print("no puede realizar el retiro")
    else:
        saldo=saldo-retiro
        print(f"en su cuenta queda con un slado de {saldo}")
elif opc==3:
    print(f"su saldo es de {saldo}")
elif opc==4:
    print("gracias por venir")
    exit()
else:
    print(f"'esa {opc}'no esta programada ")
