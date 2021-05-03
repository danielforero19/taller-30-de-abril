lista = []
m = int(input("ingrese la cantidad de numeros: "))
n = int(input("ingrese la cantdad de numeros: "))
h = m+n
c = 0
if m > n:
    while c < h:
        c += 1
        lista.append(c)
print(sum(lista))
