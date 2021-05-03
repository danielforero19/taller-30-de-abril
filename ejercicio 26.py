nota1 = float(input("ingrese la primera nota ="))
nota2 = float(input("ingrese la segunda nota ="))
nota3 = float(input("ingrese la tercera nota ="))
nota4 = float(input("ingrese la cuarta nota ="))
nota5 = float(input("ingrese la quinta nota ="))
p1 = 0.15
p2 = 0.20
p3 = 0.15
p4 = 0.3
p5 = 0.2
definitiva = nota1 * p1 + nota2 * p2 +nota3 * p3 +nota4 * p4 + nota5 * p5
if definitiva > 4.5:
    print (f"su nota fue {definitiva} felicitaciones saco mas de 4.5")
elif definitiva > 3:
    print(f"su nota fue {definitiva} por lo cual aprobo ")
elif definitiva < 2:
    print(f" su nota fue {definitiva} por lo que no aprobo y tampoco podra habilitar")
else:
    print (f"su nota fue {definitiva} por lo cual no aprobo pero podra habilitar")