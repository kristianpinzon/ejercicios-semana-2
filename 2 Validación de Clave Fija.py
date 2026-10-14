#2 Validación de Clave Fija

while True:
    clave = input("Ingrese la contraseña: ")

    if clave == "1234":
        print("¡Bienvenido al sistema!")
        break

    else:
        print("\nContraseña incorrecta. Intente nuevamente.")
