a = float(input("ingrese la aceleracion en m/s: "))
v = float(input("ingrese la velocidad en km/h: "))
t = float(input("ingrese el tiempo en segundos: "))
v2 = v * 1000/1 * 1/3600
d = v2 * t + 1/2 * a * t ** 2
print(d)