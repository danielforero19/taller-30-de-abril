s = int(input("ingrese los segundos: "))
s1 = s//60
s2 = s % 60
m1 = s1//60
m2 = s1 % 60
h1 = m1//60
h2 = m1 % 60
print(h2,":",m2,":",s2 )