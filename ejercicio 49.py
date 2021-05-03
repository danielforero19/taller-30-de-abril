lista = []
cont = 0
n = 1
while n != 0:
    n = int(input("ingrese un numero: "))
    lista.append(n)
    cont += 1
prom = sum(lista)/cont
print(" la suma de los numeros es", sum(lista),"y su promedio es", prom)