# 1 Menú Principal de un Sistema

while True:
    print("\nMENU PRINCIPAL")
    print("1. Consultar")
    print("2. Registrar")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Ha seleccionado Consultar.")
    elif opcion == 2:
        print("Ha seleccionado Registrar.")
    elif opcion == 3:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")