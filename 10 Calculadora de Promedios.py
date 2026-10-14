#10 Calculadora de Promedios
suma = 0
contador = 0

while True:
    nota = float(input("Ingrese una calificación (-1 para terminar): "))
    if nota == -1:
        break
    suma += nota
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"El promedio exacto de las {contador} notas es: {promedio}")
else:
    print("No se ingresaron calificaciones.")