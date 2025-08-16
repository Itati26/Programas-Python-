cache = {0: 0, 1: 1}

def fibonacci_cache(n):
    if n not in cache:
        cache[n] = fibonacci_cache(n-1) + fibonacci_cache(n-2)
    return cache[n]

def main():
    try:
        n = int(input("¿Cuántos números Fibonacci quieres generar? "))
        if n < 1:
            print("Debe ser al menos 1")
            return
            
        print("Serie Fibonacci:")
        for i in range(n):
            print(fibonacci_cache(i), end=' ')
    except ValueError:
        print("Ingresa un número válido")

main()
