import random
from collections import Counter

def lanzar_moneda():
    return random.choice(['Cara', 'Cruz'])

def simulador_moneda():
    lanzamientos = int(input("Número de lanzamientos: "))
    resultados = [lanzar_moneda() for _ in range(lanzamientos)]
    conteo = Counter(resultados)
    
    print(f"\nResultados de {lanzamientos} lanzamientos:")
    for resultado, count in conteo.items():
        porcentaje = (count / lanzamientos) * 100
        print(f"{resultado}: {count} veces ({porcentaje:.1f}%)")
    
    # Secuencia más larga de caras/cruces
    secuencia_actual = 1
    secuencia_max = 1
    for i in range(1, len(resultados)):
        if resultados[i] == resultados[i-1]:
            secuencia_actual += 1
            secuencia_max = max(secuencia_max, secuencia_actual)
        else:
            secuencia_actual = 1
    
    print(f"Secuencia más larga: {secuencia_max}")

simulador_moneda()
