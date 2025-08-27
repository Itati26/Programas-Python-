print("🚗 VERIFICACIÓN PARA LICENCIA DE CONDUCIR")

try:
    edad = int(input("Ingresa tu edad: "))
    pais = input("¿En qué país resides? ").lower()
    
    if edad < 0:
        print("❌ Error: Edad inválida")
    elif pais == "méxico" or pais == "mexico":
        if edad >= 18:
            print("✅ Puedes sacar tu licencia de conducir")
        else:
            print("❌ Debes tener 18 años o más")
    elif pais == "estados unidos" or pais == "usa":
        if edad >= 16:
            print("✅ Puedes sacar tu licencia de conducir")
        else:
            print("❌ Debes tener 16 años o más")
    else:
        if edad >= 17:
            print("✅ Probablemente puedas sacar tu licencia (verifica leyes locales)")
        else:
            print("❌ Edad insuficiente para la mayoría de países")
            
except ValueError:
    print("❌ Ingresa una edad válida")
