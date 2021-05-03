lado = int(input("ingresa el valor de un lado: "))
mitad = lado/2
apotema = (lado**2)-(mitad**2)
apotema=apotema*1.0
if apotema>=0:
    p=apotema
    i=0
    while i!=p:
        i=p
        p=(apotema/p+p)/2
perimetro= lado * 6
area = perimetro * p /2
print(area)