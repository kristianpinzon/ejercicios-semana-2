#13 Calculadora de Potencia sin Operador
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero positivo o cero): "))

resultado = 1
i = 0

while i < exponente:
    resultado *= base
    i += 1

print(f"El resultado de {base} elevado a {exponente} es: {resultado}")