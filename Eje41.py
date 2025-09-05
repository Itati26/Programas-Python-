print("🍎 PLAN NUTRICIONAL POR EDAD")

try:
    edad = int(input("Ingresa la edad en meses: "))
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad <= 6:
        print("🍼 Alimentación:")
        print("   - Lactancia materna exclusiva")
        print("   - 8-12 tomas al día")
        print("   - No agregar agua ni otros líquidos")
    elif edad <= 8:
        print("🥄 Alimentación:")
        print("   - Papillas de frutas")
        print("   - Cereales infantiles")
        print("   - Continuar con lactancia")
    elif edad <= 12:
        print("🍲 Alimentación:")
        print("   - Carnes molidas")
        print("   - Verduras cocidas")
        print("   - Frutas picadas")
    elif edad <= 24:
        print("🍴 Alimentación:")
        print("   - Dieta familiar adaptada")
        print("   - 4-5 comidas al día")
        print("   - Líquidos abundantes")
    else:
        print("🍽️  Alimentación:")
        print("   - Dieta balanceada completa")
        print("   - 3 comidas principales")
        print("   - 2 colaciones saludables")
        
except ValueError:
    print("❌ Ingresa una edad válida en meses")
