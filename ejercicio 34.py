usuario = "daniel81"
contrasena = "clase19"
u = input("ingrese el usuario = ")
c = input("ingrese la contraseña = ")
if usuario == u:
    if contrasena == c:
        print(f"hola, bienvenido nuevamente {usuario}")
    else:
        print("usuario o contraseña incorrectos. intentelo de nuevo")