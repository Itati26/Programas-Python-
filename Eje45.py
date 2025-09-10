def conversor_unidades():
    """
    Conversor simple de unidades de longitud, peso y temperatura
    """
    print("📏 Conversor de Unidades 📏")
    print("=" * 30)
    
    while True:
        print("\n¿Qué quieres convertir?")
        print("1. Longitud")
        print("2. Peso")
        print("3. Temperatura")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ").strip()
        
        if opcion == '4':
            print("👋 ¡Hasta luego!")
            break
        
        if opcion == '1':
            convertir_longitud()
        elif opcion == '2':
            convertir_peso()
        elif opcion == '3':
            convertir_temperatura()
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

def convertir_longitud():
    """Conversor de unidades de longitud"""
    print("\n📏 CONVERSOR DE LONGITUD")
    print("1. Centímetros a Pulgadas")
    print("2. Pulgadas a Centímetros")
    print("3. Metros a Pies")
    print("4. Pies a Metros")
    
    opcion = input("Elige una conversión (1-4): ").strip()
    
    try:
        valor = float(input("Ingresa el valor a convertir: "))
        
        if opcion == '1':
            resultado = valor * 0.393701
            print(f"✅ {valor} cm = {resultado:.2f} pulgadas")
        elif opcion == '2':
            resultado = valor * 2.54
            print(f"✅ {valor} pulgadas = {resultado:.2f} cm")
        elif opcion == '3':
            resultado = valor * 3.28084
            print(f"✅ {valor} m = {resultado:.2f} pies")
        elif opcion == '4':
            resultado = valor * 0.3048
            print(f"✅ {valor} pies = {resultado:.2f} m")
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor, ingresa un número válido")

def convertir_peso():
    """Conversor de unidades de peso"""
    print("\n⚖️ CONVERSOR DE PESO")
    print("1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    print("3. Gramos a Onzas")
    print("4. Onzas a Gramos")
    
    opcion = input("Elige una conversión (1-4): ").strip()
    
    try:
        valor = float(input("Ingresa el valor a convertir: "))
        
        if opcion == '1':
            resultado = valor * 2.20462
            print(f"✅ {valor} kg = {resultado:.2f} libras")
        elif opcion == '2':
            resultado = valor * 0.453592
            print(f"✅ {valor} libras = {resultado:.2f} kg")
        elif opcion == '3':
            resultado = valor * 0.035274
            print(f"✅ {valor} g = {resultado:.2f} onzas")
        elif opcion == '4':
            resultado = valor * 28.3495
            print(f"✅ {valor} onzas = {resultado:.2f} g")
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor, ingresa un número válido")

def convertir_temperatura():
    """Conversor de unidades de temperatura"""
    print("\n🌡️ CONVERSOR DE TEMPERATURA")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")
    
    opcion = input("Elige una conversión (1-4): ").strip()
    
    try:
        valor = float(input("Ingresa la temperatura: "))
        
        if opcion == '1':
            resultado = (valor * 9/5) + 32
            print(f"✅ {valor}°C = {resultado:.2f}°F")
        elif opcion == '2':
            resultado = (valor - 32) * 5/9
            print(f"✅ {valor}°F = {resultado:.2f}°C")
        elif opcion == '3':
            resultado = valor + 273.15
            print(f"✅ {valor}°C = {resultado:.2f} K")
        elif opcion == '4':
            resultado = valor - 273.15
            print(f"✅ {valor} K = {resultado:.2f}°C")
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor, ingresa un número válido")

if __name__ == "__main__":
    conversor_unidades()
