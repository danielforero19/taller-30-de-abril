a = float(input("ingrese el numero: "))
if a > 0 and a % 2 == 0:
    print("el numero es positivo y par")
if a < 0 and a % 2 == 0:
    print("el numero es negativo e par")
elif a == 0:
    print("el numero es 0")
elif a > 0 and a % 2 != 0:
    print("el numero es positivo y impar")
elif a < 0 and a % 2 != 0:
    print("el numero es negativo y impar")