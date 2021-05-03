valor = int(input("ingrese el valor de la venta: "))
precio_iva = valor+(valor*0.19)
if valor > 150000:
    descuento = precio_iva * 0.05
    precio_final = valor-descuento
    print(precio_final)
else:
    print(precio_iva)