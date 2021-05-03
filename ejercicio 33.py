import math
a = float(input("ingrese el valor a = "))
b = float(input("ingrese el valor b = "))
c = float(input("ingrese el valor c = "))
x = (b**2)-(4*a*c)
x1 = (-b + math.sqrt(x))/(2*a)
x2 = (-b - math.sqrt(x))/(2*a)
print(f"({x1},{x2})")
