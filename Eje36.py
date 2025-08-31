print("📱 PLANES DE TELEFONÍA POR EDAD")

try:
    edad = int(input("Ingresa tu edad: "))
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad < 18:
        print("👶 Plan Junior: $100/mes")
        print("   - 5GB de datos")
        print("   - Llamadas ilimitadas")
        print("   - Control parental incluido")
    elif edad <= 25:
        print("🎓 Plan Universitario: $150/mes")
        print("   - 10GB de datos")
        print("   - Redes sociales ilimitadas")
        print("   - Spotify Premium incluido")
    elif edad <= 60:
        print("💼 Plan Adulto: $300/mes")
        print("   - Ilimitado en todo")
        print("   - Hotspot incluido")
        print("   - Servicio corporativo")
    else:
        print("👵 Plan Tercera Edad: $120/mes")
        print("   - 3GB de datos")
        print("   - Llamadas ilimitadas")
        print("   - Botón de emergencia")
        
except ValueError:
    print("❌ Ingresa una edad válida")
