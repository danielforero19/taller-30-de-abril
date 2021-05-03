i = 1
suma = 0
while i <= 3:
    numeros = int(input("ingresa tres numeros: "))
    suma = suma + numeros
    i+=1
else:
    resultado = suma / 3
    print("el promedio de los numeros ingresados es: ", resultado)