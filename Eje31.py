print("=== SISTEMA DE TARIFAS DE AUTOBÚS ===")

# Definir precios (puedes modificarlos)
TARIFA_NIÑO = 10
TARIFA_ADULTO = 20
TARIFA_TERCERA_EDAD = 15

try:
    edad = int(input("Ingresa la edad del pasajero: "))
    
    if edad < 0:
        print("❌ Error: La edad no puede ser negativa")
    elif edad <= 5:
        print(f"💰 Tarifa: GRATIS (0-5 años)")
    elif edad <= 12:
        print(f"💰 Tarifa: ${TARIFA_NIÑO}.00 (6-12 años)")
    elif edad <= 60:
        print(f"💰 Tarifa: ${TARIFA_ADULTO}.00 (13-60 años)")
    else:
        print(f"💰 Tarifa: ${TARIFA_TERCERA_EDAD}.00 (60+ años)")
        
except ValueError:
    print("❌ Por favor, ingresa una edad válida")
