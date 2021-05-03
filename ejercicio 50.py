lista = []
cont = 0
n = 1
while n != 0:
    n = int(input("ingrese un numero: "))
    lista.append(n)
    cont += 1
if cont % 2 == 0:
    prom = sum(lista)/cont-1
    print(f"el promedio de los impares es {prom}")
if cont % 2 != 0:
    prom = sum(lista) / cont+1
    print(f"el promedio de los pares es {prom}")
