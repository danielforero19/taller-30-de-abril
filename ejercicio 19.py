dinero = int(input("ingrese la cantidad de dinero: "))
if dinero >= 100000:
    restante = dinero // 100000
    print("existen " + str(restante) + " billetes de 100 mil pesos" )
    dinero = dinero % 100000
if dinero >= 50000:
    restante = dinero // 50000
    print("existen " + str(restante) + " billetes de 50 mil pesos" )
    dinero = dinero % 50000
if dinero >= 20000:
    restante = dinero // 20000
    print("existen " + str(restante) + " billetes de 20 mil pesos" )
    dinero = dinero % 20000
if dinero >= 10000:
    restante = dinero // 10000
    print("existen " + str(restante) + " billetes de 10 mil pesos" )
    dinero = dinero % 10000
if dinero >= 5000:
    restante = dinero // 5000
    print("existen " + str(restante) + " billetes de 5 mil pesos" )
    dinero = dinero % 5000
if dinero >= 2000:
    restante = dinero // 2000
    print("existen " + str(restante) + " billetes de 2 mil pesos" )
    dinero = dinero % 2000
if dinero >= 1000:
    restante = dinero // 1000
    print("existen " + str(restante) + " billetes de 1 mil pesos" )
    dinero = dinero % 1000
