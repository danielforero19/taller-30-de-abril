n = int(input("ingrese cuantos numeros desea mostrar: "))
c = 1
d = -1
while c < n:
    if c % 2 != 0:
        print(c)
        if d % 2 == 0:
            print(d)
        d -= 1
    c += 1

