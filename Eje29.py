print("=== SISTEMA DE TARIFAS DE AUTOBÚS ===")
try:
    edad = int(input("Ingresa la edad del pasajero: "))
    
    if edad < 0:
        print("❌ Error: La edad no puede ser negativa")
    elif edad <= 5:
        print("💰 Tarifa: GRATIS (0-5 años)")
    elif edad <= 12:
        print("💰 Tarifa: $10.00 (6-12 años)")
    elif edad <= 60:
        print("💰 Tarifa: $20.00 (13-60 años)")
    else:
        print("💰 Tarifa: $15.00 (60+ años, tercera edad)")
        
except ValueError:
    print("❌ Por favor, ingresa una edad válida (número entero)")
