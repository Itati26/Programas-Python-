import random

def lanzar_dados(cantidad, caras):
    return [random.randint(1, caras) for _ in range(cantidad)]

def estadisticas(resultados):
    return {
        'total': sum(resultados),
        'promedio': sum(resultados) / len(resultados),
        'maximo': max(resultados),
        'minimo': min(resultados)
    }

while True:
    print("\n1. Lanzar dados\n2. Salir")
    opcion = input("Opción: ")
    if opcion == '2': break
    
    cantidad = int(input("Número de dados: "))
    caras = int(input("Número de caras: "))
    
    resultados = lanzar_dados(cantidad, caras)
    stats = estadisticas(resultados)
    
    print(f"Resultados: {resultados}")
    print(f"Total: {stats['total']}")
    print(f"Promedio: {stats['promedio']:.2f}")
    print(f"Máximo: {stats['maximo']}")
    print(f"Mínimo: {stats['minimo']}")
