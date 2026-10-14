#14 Serie de Fibonacci
n = int(input("Ingrese la cantidad de términos de Fibonacci que desea visualizar: "))

a = 0
b = 1
contador = 0

print("Serie de Fibonacci:")
while contador < n:
    print(a, end=" ")
    siguiente = a + b
    a = b
    b = siguiente
    contador += 1
print()  