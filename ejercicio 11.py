#con math
import math
altura = int(input("ingrese la altura: "))
g = 9.81
t = math.sqrt(2*altura/9.81)
print("el tiempo que tarda en caer es:", t)
#sin math
n = int(input("ingrese la altura: "))
apotema = 2*n/9.81
if apotema>=0:
    p=apotema
    i=0
    while i!=p:
        i=p
        p=(apotema/p+p)/2
print("el tiempo que tarda en caer es:", p)