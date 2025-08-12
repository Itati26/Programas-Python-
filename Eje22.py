# Programa simple: Calculadora básica
def calculadora():
    print("¡Calculadora Básica en Python!")
    print("Operaciones disponibles: +, -, *, /")
    
    try:
        num1 = float(input("Ingresa el primer número: "))
        operacion = input("Ingresa la operación: ")
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                raise ZeroDivisionError("¡No se puede dividir entre cero!")
            resultado = num1 / num2
        else:
            print("Operación no válida.")
            return
        
        print(f"Resultado: {resultado}")
    
    except ValueError:
        print("Error: Ingresa números válidos.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculadora()
