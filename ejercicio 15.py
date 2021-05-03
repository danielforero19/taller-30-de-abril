x1 = float(input("ingrese x1: "))
y1 = float(input("ingrese y1: "))
x2 = float(input("ingrese x2: "))
y2 = float(input("ingrese y2: "))
d = (x2-x1)**2+(y2-y1)**2
if d>=0:
    p=d
    i=0
    while i!=p:
        i=p
        p=(d/p+p)/2
print("la distancia es de:", p," unidades")
