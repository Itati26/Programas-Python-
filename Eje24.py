import random

def jugar():
    print("🎮 ¡Adivina el número entre 1 y 100!")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = input("👉 Ingresa tu número: ")
        
        try:
            intento = int(intento)
            intentos += 1

            if intento < numero_secreto:
                print("⬆️ Más alto")
            elif intento > numero_secreto:
                print("⬇️ Más bajo")
            else:
                print(f"🎉 ¡Correcto! Lo lograste en {intentos} intentos.")
                break

        except ValueError:
            print("❌ ¡Debes ingresar un número!")

if __name__ == "__main__":
    jugar()
