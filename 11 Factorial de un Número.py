#11 Factorial de un Número
num = int(input("Ingrese un número entero positivo: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"El factorial de {num} es: {factorial}")