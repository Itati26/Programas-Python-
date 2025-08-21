# Verificador de acceso a atracciones
print("=== SISTEMA DE VERIFICACIÓN DE EDAD ===")

try:
    edad = int(input("¿Cuántos años tienes? "))
    
    if edad < 0:
        print("❌ Error: La edad no puede ser negativa")
    elif edad < 5:
        print("🚼 Necesitas ir con un adulto para subir")
    elif edad < 8:
        print("⚠️  Puedes subir pero con supervisión de un adulto")
    elif edad < 65:
        print("✅ ¡Puedes subir sin problemas!")
    else:
        print("👵👴 Por tu seguridad, consulta con el personal")
        
except ValueError:
    print("❌ Por favor, ingresa un número válido")
