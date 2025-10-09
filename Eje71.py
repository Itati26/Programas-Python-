def analizar_sueno():
    horas_sueno = []
    
    print("Registra tus horas de sueño (7 días):")
    for i in range(7):
        horas = float(input(f"Día {i+1} horas de sueño: "))
        horas_sueno.append(horas)
    
    promedio = sum(horas_sueno) / len(horas_sueno)
    max_sueno = max(horas_sueno)
    min_sueno = min(horas_sueno)
    
    print(f"\nAnálisis de sueño semanal:")
    print(f"Promedio: {promedio:.1f} horas")
    print(f"Máximo: {max_sueno} horas")
    print(f"Mínimo: {min_sueno} horas")
    
    if promedio >= 7:
        print("¡Excelentes hábitos de sueño!")
    elif promedio >= 6:
        print("Sueño adecuado, pero podrías mejorar")
    else:
        print("Necesitas dormir más horas")

analizar_sueno()
