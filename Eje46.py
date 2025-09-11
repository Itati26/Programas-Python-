# Sistema de préstamos de biblioteca por edad
print("📚 SISTEMA DE PRÉSTAMO BIBLIOTECARIO")

try:
    edad = int(input("Ingresa tu edad: "))
    tipo_material = input("¿Qué material quieres? (libro/revista/dvd): ").lower()
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad < 12:
        print("👦 Sección infantil:")
        print("   - Máximo 2 materiales")
        print("   - Préstamo por 7 días")
        print("   - Solo libros y revistas")
    elif edad < 18:
        print("👨 Sección juvenil:")
        print("   - Máximo 3 materiales")
        print("   - Préstamo por 14 días")
        print("   - Todos los materiales excepto DVD adultos")
    else:
        print("👨 Sección adultos:")
        print("   - Máximo 5 materiales")
        print("   - Préstamo por 21 días")
        print("   - Acceso a todo el material")
        
    if tipo_material == "dvd" and edad < 18:
        print("⚠️  Necesitas autorización parental para DVD")
        
except ValueError:
    print("❌ Ingresa una edad válida")
