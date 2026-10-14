#4 Validación de Nota Positiva

nota = float(input("\nIngrese una nota entre 0.0 y 5.0: "))

while nota < 0 or nota > 5:
    print("Nota inválida. Debe estar entre 0.0 y 5.0.")
    nota = float(input("\nIngrese nuevamente la nota: "))

print("Nota registrada:", nota)
