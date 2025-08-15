def fibonacci_limite():
    while True:
        try:
            limite = int(input("Ingresa el número máximo para la serie Fibonacci: "))
            if limite < 0:
                print("Debe ser un número positivo")
                continue
                
            a, b = 0, 1
            print(f"Serie Fibonacci hasta {limite}:")
            while a <= limite:
                print(a, end=' ')
                a, b = b, a + b
            break
        except ValueError:
            print("¡Error! Ingresa un número válido")

fibonacci_limite()
