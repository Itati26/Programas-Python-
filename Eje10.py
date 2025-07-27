def generar_fibonacci(n):
    a, b = 0, 1
    serie = []
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

while True:
    entrada = input("¿Cuántos números de Fibonacci deseas generar? (o 'salir' para terminar): ")
    
    if entrada.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    try:
        cantidad = int(entrada)
        if cantidad <= 0:
            print("Por favor ingresa un número entero positivo.\n")
            continue
            
        resultado = generar_fibonacci(cantidad)
        print(f"\nSerie Fibonacci con {cantidad} elementos:")
        print(' '.join(map(str, resultado)) + '\n')
        
    except ValueError:
        print("Error: Ingresa un número entero válido o 'salir'.\n")
