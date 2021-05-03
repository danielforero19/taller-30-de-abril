lista = []
cont = 0
while cont < 10:
    n = int(input("ingrese un numero: "))
    lista.append(n)
    cont += 1
prom = sum(lista)/10
print(" la suma de los numeros es", sum(lista),"y su promedio es", prom)
