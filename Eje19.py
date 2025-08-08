def calcular_costo_boleto(edad):
    if edad < 0:
        return "Edad inválida"
    elif edad <= 3:
        return "Gratis 🎉"
    elif edad <= 12:
        return "$10 - Tarifa infantil 🧒"
    elif edad <= 64:
        return "$20 - Tarifa estándar 🧍"
    else:
        return "$12 - Tarifa para adultos mayores 👵👴"

# Ejemplo de uso
try:
    edad = int(input("Ingresa la edad del pasajero: "))
    costo = calcular_costo_boleto(edad)
    print(f"Costo del boleto: {costo}")
except ValueError:
    print("Por favor, ingresa un número válido.")
