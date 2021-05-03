lista = []
va = 0.19
iva = 0.19
a = True
while a == True:
    seleccion = int(input("ingrese 1 para agregar producto y 2 para ver la lista: "))
    if seleccion == 1:
        valor_neto = int(input("ingrese el valor o valores de la venta: "))
        lista.append(valor_neto)
        h = int(input("ingrese el valor o valores de la venta: "))
        lista.append(h)
        va = 0.19
        valor_iva = iva * sum(lista) / sum(lista)
        valor_coniva = iva * sum(lista)

    if seleccion == 2:
        break
print(sum(lista))

