import random

def juego_adivinanza():
    """
    Juego simple donde la computadora elige un número
    y el jugador debe adivinarlo en intentos limitados.
    """
    print("🎮 ¡Bienvenido al juego de adivinanza de números!")
    print("=" * 50)
    print("Estoy pensando en un número entre 1 y 100...")
    print("Tienes 7 intentos para adivinarlo. ¡Buena suerte!")
    
    # Generar número aleatorio
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 7
    
    while intentos < max_intentos:
        try:
            # Obtener intento del usuario
            intento = int(input(f"\nIntento {intentos + 1}/{max_intentos} - ¿Cuál es tu guess? "))
            
            # Verificar el intento
            if intento < numero_secreto:
                print("⬆️ ¡Más alto! El número es mayor.")
            elif intento > numero_secreto:
                print("⬇️ ¡Más bajo! El número es menor.")
            else:
                print(f"🎉 ¡Felicidades! ¡Adivinaste el número {numero_secreto} en {intentos + 1} intentos!")
                break
                
            intentos += 1
            
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
    
    else:
        print(f"\n😢 ¡Agotaste tus intentos! El número era {numero_secreto}.")
    
    # Preguntar si quiere jugar again
    jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_de_nuevo == 's':
        juego_adivinanza()
    else:
        print("¡Gracias por jugar! 👋")

if __name__ == "__main__":
    juego_adivinanza()
