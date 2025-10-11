def ajustar_receta():
    print("Ajustador de recetas")
    
    ingredientes = {}
    print("Ingresa los ingredientes (deja vacío para terminar):")
    
    while True:
        ingrediente = input("Ingrediente: ")
        if not ingrediente:
            break
        cantidad = float(input("Cantidad: "))
        unidad = input("Unidad: ")
        ingredientes[ingrediente] = {'cantidad': cantidad, 'unidad': unidad}
    
    factor = float(input("\nFactor de ajuste (ej: 0.5 para mitad, 2 para doble): "))
    
    print("\nReceta ajustada:")
    for ingrediente, datos in ingredientes.items():
        nueva_cantidad = datos['cantidad'] * factor
        print(f"{ingrediente}: {nueva_cantidad} {datos['unidad']}")

ajustar_receta()
