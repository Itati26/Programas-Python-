def calcular_calorias():
    edad = int(input("Edad: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (cm): "))
    genero = input("Género (M/F): ").upper()
    actividad = float(input("Nivel de actividad (1.2-1.9): "))
    
    if genero == 'M':
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    else:
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
    
    calorias = tmb * actividad
    
    print(f"\nCalorías diarias necesarias: {calorias:.0f}")
    print("Para mantener peso:", calorias)
    print("Para bajar peso:", calorias - 500)
    print("Para subir peso:", calorias + 500)

calcular_calorias()
