print("DESCUENTOS EN CINE")
try:
    edad = int(input("Ingresa tu edad: "))
    precio_base = 100  # Precio normal del boleto
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad < 4:
        print(f"💰 Entrada: GRATIS (0-3 años)")
        print(f"💵 Precio normal: ${precio_base}")
    elif edad <= 12:
        descuento = precio_base * 0.5
        print(f"💰 Entrada: ${descuento:.2f} (50% descuento - 4-12 años)")
        print(f"💵 Precio normal: ${precio_base}")
    elif edad >= 60:
        descuento = precio_base * 0.4
        print(f"💰 Entrada: ${descuento:.2f} (40% descuento - 60+ años)")
        print(f"💵 Precio normal: ${precio_base}")
    else:
        print(f"💰 Entrada: ${precio_base:.2f} (Precio regular - 13-59 años)")
        
except ValueError:
    print("❌ Por favor, ingresa una edad válida")
