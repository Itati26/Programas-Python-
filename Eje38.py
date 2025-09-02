print("⚽ CATEGORÍAS DEPORTIVAS POR EDAD")

try:
    edad = int(input("Ingresa tu edad: "))
    deporte = input("¿Qué deporte practicas? ").lower()
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad < 6:
        print("👶 Categoría: Pre-infantil")
        print("   - Enfoque en desarrollo motor")
        print("   - Actividades lúdicas")
    elif edad <= 8:
        print("👦 Categoría: Infantil A")
        print("   - Iniciación deportiva")
        print("   - Juegos pre-deportivos")
    elif edad <= 10:
        print("👦 Categoría: Infantil B")
        print("   - Desarrollo de fundamentos")
    elif edad <= 12:
        print("👦 Categoría: Infantil C")
        print("   - Competición básica")
    elif edad <= 14:
        print("👦 Categoría: Juvenil A")
        print("   - Competición formal")
    elif edad <= 16:
        print("👦 Categoría: Juvenil B")
        print("   - Alto rendimiento")
    elif edad <= 18:
        print("👦 Categoría: Juvenil C")
        print("   - Nivel competitivo")
    else:
        print("👨 Categoría: Adultos")
        print("   - Liga mayor")
        print("   - Veteranos (35+ años)")
        
except ValueError:
    print("❌ Ingresa una edad válida")
