print("🏛️  SISTEMA DE TARIFAS - MUSEO")

try:
    edad = int(input("Ingresa tu edad: "))
    es_estudiante = input("¿Eres estudiante? (si/no): ").lower() == "si"
    es_discapacitado = input("¿Tienes discapacidad? (si/no): ").lower() == "si"
    
    precio_base = 100
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad < 3:
        print("💰 Entrada: GRATIS (0-3 años)")
    elif edad <= 12:
        precio = precio_base * 0.4
        print(f"💰 Entrada: ${precio:.2f} (60% descuento - 4-12 años)")
    elif es_estudiante:
        precio = precio_base * 0.5
        print(f"💰 Entrada: ${precio:.2f} (50% descuento - Estudiante)")
    elif edad >= 60:
        precio = precio_base * 0.3
        print(f"💰 Entrada: ${precio:.2f} (70% descuento - Tercera edad)")
    elif es_discapacitado:
        precio = precio_base * 0.2
        print(f"💰 Entrada: ${precio:.2f} (80% descuento - Discapacidad)")
    else:
        print(f"💰 Entrada: ${precio_base:.2f} (Precio regular)")
        
except ValueError:
    print("❌ Ingresa una edad válida")
