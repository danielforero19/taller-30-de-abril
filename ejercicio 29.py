n1 = float(input("ingrese el primer numero: "))
n2 = float(input("ingrese el segundo numero: "))
n3 = float(input("ingrese el tercer numero: "))

if n1 < n3 < n2:
    print(f"{n2} es el mayor y {n1} es el menor")
elif n2 < n1 < n3:
    print(f"{n1} es el mayor y {n3} es el menor")
elif n3 < n2 < n1:
    print(f"{n1} es el mayor y {n3} es el menor")
elif n1 < n2 < n3:
    print(f"{n3} es el mayor y {n1} es el menor")
elif n2 < n3 < n1:
    print(f"{n2} es el mayor y {n1} es el menor")
elif n3 < n1 < n2:
    print(f"{n2} es el mayor y {n3} es el menor")
else:
    print("ingreso un numero igual. vueva iniciar el programa")