print("🎓 SISTEMA DE BECAS EDUCATIVAS")

try:
    edad = int(input("Ingresa tu edad: "))
    promedio = float(input("Ingresa tu promedio (0-10): "))
    ingresos = float(input("Ingresos familiares mensuales: "))
    
    if edad < 0 or promedio < 0 or ingresos < 0:
        print("❌ Error: Valores inválidos")
    elif edad < 15:
        print("❌ Edad mínima: 15 años")
    elif edad > 30:
        print("❌ Edad máxima: 30 años")
    elif promedio < 8.5:
        print("❌ Promedio mínimo requerido: 8.5")
    elif ingresos > 10000:
        print("❌ Límite de ingresos excedido")
    else:
        print("✅ ¡FELICIDADES! Eres elegible para beca")
        print(f"📊 Tu puntuación: {(promedio * 10) + (30 - edad)}")
        print("🎯 Beca del 70% garantizada")
        
except ValueError:
    print("❌ Ingresa valores numéricos válidos")
