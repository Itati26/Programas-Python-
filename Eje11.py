def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Solicitar entrada al usuario
try:
    cantidad = int(input("¿Cuántos números de la serie Fibonacci deseas ver? "))
    if cantidad <= 0:
        print("Por favor ingresa un número entero positivo.")
    else:
        print(f"\nLos primeros {cantidad} números de la serie Fibonacci son:")
        fibonacci(cantidad)
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
