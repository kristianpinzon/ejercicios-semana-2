#6 Selección de Tipo de Documento
while True:
    tipo = input("Ingrese su tipo de documento (CC, TI, CE): ").upper()
    
    if tipo in ["CC", "TI", "CE"]:
        print(f"Documento aceptado: {tipo}")
        break
    else:
        print("\nDocumento inválido. Debe ser CC, TI o CE. Intente nuevamente.")