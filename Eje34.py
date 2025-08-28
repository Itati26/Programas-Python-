print("💪 SISTEMA DE MEMBRESÍAS - GIMNASIO")

try:
    edad = int(input("Ingresa tu edad: "))
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad < 14:
        print("👶 Membresía infantil: $200/mes (con tutor)")
        print("⚠️  Requiere autorización de padres")
    elif edad <= 17:
        print("👦 Membresía juvenil: $300/mes")
        print("📝 Requiere firma de padres")
    elif edad <= 59:
        print("👨 Membresía adulta: $500/mes")
        print("✅ Acceso completo a instalaciones")
    else:
        print("👵 Membresía tercera edad: $250/mes")
        print("🎯 Clases especiales y horarios preferentes")
        
except ValueError:
    print("❌ Por favor, ingresa una edad válida")
