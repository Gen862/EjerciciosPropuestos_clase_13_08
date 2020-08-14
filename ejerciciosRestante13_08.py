#Realizar una calculadora
print("Bienvenidos a la calculadora de todos. \nrealiza las 4 operaciones básicas")
numero1 = float(input("\nDigite un numero: "))
numero2 = float(input("\nDigite otro numero: "))
operacion=input("Digite la operacion a ejecutar: s (suma), r (resta), m (multiplicación), d (división)").upper()
if operacion == 'S':
    suma=numero1+numero2
    print(f"\n El resultado es {suma}")
elif operacion == 'R':
    resta=numero1-numero2
    print(f"\n El resultado es {resta}")
elif operacion == 'M':
    multiplicacion=numero1*numero2
    print(f"\n El resultado es {multiplicacion}")
elif operacion == 'D':
    div=numero1/numero2
    print(f"\n El resultado es {div:.2f}")
else:
    print("Se equivoco de operación")


#Aplicación de un cajero automatico
print("\n Bienvenidos a tu Banco Liquidez\n")
saldo = 1000
print("\t.Menú:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero en la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion= int(input("\n Digíte una opción del menú: "))
print()
if opcion==1:
    extra=float(input("¿Cuando dinero desea ingresar?"))
    saldo = saldo + extra
    print(f"El dinero en la cuenta es: {saldo}")
elif opcion==2:
    retirar=float(input("¿Cuanto desea retirar?"))
    if retirar > saldo:

        print("Fondos insuficientes")
    else:
        saldo= (saldo-retirar)
        print(f"Su saldo restante es: {saldo:.1f}")
elif opcion==3:
    print(f"El dinero en la cuenta es: {saldo}")
elif opcion==4:
    print("Gracias por utilizar nuestros servicios")
else:
    print("Opcion invalida")

#listas
lista=["lunes, martes, miercoles, jueves, viernes"]
print(lista[0])

