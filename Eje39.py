print("🎮 RECOMENDADOR DE VIDEOJUEGOS")

try:
    edad = int(input("Ingresa tu edad: "))
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif edad < 7:
        print("🟢 Clasificación: E (Everyone)")
        print("🎮 Recomendados:")
        print("   - Minecraft")
        print("   - Super Mario")
        print("   - Animal Crossing")
    elif edad < 13:
        print("🟡 Clasificación: E10+ (Everyone 10+)")
        print("🎮 Recomendados:")
        print("   - Lego Games")
        print("   - Pokémon")
        print("   - Zelda")
    elif edad < 18:
        print("🟠 Clasificación: T (Teen)")
        print("🎮 Recomendados:")
        print("   - Fortnite")
        print("   - FIFA")
        print("   - Overwatch")
    else:
        print("🔴 Clasificación: M (Mature)")
        print("🎮 Recomendados:")
        print("   - Call of Duty")
        print("   - GTA")
        print("   - The Witcher")
        
except ValueError:
    print("❌ Ingresa una edad válida")
