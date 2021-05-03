a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercer numero: "))
if a == b or a == c or b == c or a == b == c:
    print("al menos dos numeros son iguales")
else:
    print("no hay numeros iguales")