ano = int(input("Introduce un año: "))
if ano % 4 != 0:
    print("No es bisiesto")
elif ano % 4 == 0 and ano % 100 != 0:
    print("Es bisiesto")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
    print("No es bisiesto")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print("Es bisiesto")
