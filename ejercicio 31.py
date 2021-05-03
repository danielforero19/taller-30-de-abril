distancia = int(input("ingrese la distancia a recorrer en km: "))
estancia = int(input("ingrese el numero de dias de estancia: "))
precio = 5000 * distancia
if distancia > 1000 and estancia > 7:
    descuento = precio * 0.15
    precio_final = precio - descuento
    print(f"el precio del pasaje es {precio_final} pesos ")
else:
    print(f"el precio del pasaje es {precio} pesos ")