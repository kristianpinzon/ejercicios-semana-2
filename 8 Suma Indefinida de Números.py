#8 Suma Indefinida de Números
suma = 0
while True:
    numero = float(input("Ingrese un número real (ingrese 0 para terminar): "))
    suma += numero
    if numero == 0:
        break

print(f"La suma total acumulada es: {suma}")