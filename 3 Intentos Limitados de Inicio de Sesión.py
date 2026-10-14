#3 Intentos Limitados de Inicio de Sesión

clavec = "1234"
intentos = 0

while True:
    clave = input("\nIngrese la contraseña: ")
    intentos += 1

    if clave == clavec:
        print("Acceso concedido.")
        break

    elif intentos == 3:
        print("Cuenta bloqueada.")
        break

    else:
        print("Contraseña incorrecta.")
