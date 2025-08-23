print("=== TARIFAS ===")

TARIFA_NIÑO = 10
TARIFA_ADULTO = 20
TARIFA_TERCERA_EDAD = 15

total = 0
pasajeros = int(input("¿Cuántos pasajeros son? "))

for i in range(pasajeros):
    try:
        edad = int(input(f"Edad del pasajero {i+1}: "))
        
        if edad < 0:
            print("❌ Edad inválida, se omitirá este pasajero")
            continue
            
        if edad <= 5:
            tarifa = 0
            print("💰 Gratis (0-5 años)")
        elif edad <= 12:
            tarifa = TARIFA_NIÑO
            print(f"💰 ${TARIFA_NIÑO}.00 (6-12 años)")
        elif edad <= 60:
            tarifa = TARIFA_ADULTO
            print(f"💰 ${TARIFA_ADULTO}.00 (13-60 años)")
        else:
            tarifa = TARIFA_TERCERA_EDAD
            print(f"💰 ${TARIFA_TERCERA_EDAD}.00 (60+ años)")
            
        total += tarifa
        
    except ValueError:
        print("❌ Edad inválida, se omitirá este pasajero")

print(f"\n💵 TOTAL A PAGAR: ${total}.00")
