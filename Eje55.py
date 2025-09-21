def conversor_bases():
    numero = input("Número: ")
    base_origen = int(input("Base de origen (2-16): "))
    base_destino = int(input("Base de destino (2-16): "))
    
    # Convertir a decimal primero
    try:
        decimal = int(numero, base_origen)
    except ValueError:
        print("Número inválido para la base especificada")
        return
    
    # Convertir a base destino
    if base_destino == 10:
        resultado = str(decimal)
    else:
        digitos = "0123456789ABCDEF"
        resultado = ""
        temp = decimal
        while temp > 0:
            resultado = digitos[temp % base_destino] + resultado
            temp //= base_destino
    
    print(f"{numero} (base {base_origen}) = {resultado} (base {base_destino})")

conversor_bases()
