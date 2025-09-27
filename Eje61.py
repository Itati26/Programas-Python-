def organizador_compras():
    lista = {}
    
    while True:
        print("\n1. Agregar item\n2. Ver lista\n3. Marcar comprado\n4. Salir")
        opcion = input("Opción: ")
        
        if opcion == '4':
            break
        elif opcion == '1':
            item = input("Item: ")
            cantidad = input("Cantidad: ")
            lista[item] = {'cantidad': cantidad, 'comprado': False}
        elif opcion == '2':
            print("\nLista de compras:")
            for i, (item, datos) in enumerate(lista.items(), 1):
                estado = "✓" if datos['comprado'] else "✗"
                print(f"{i}. [{estado}] {item} - {datos['cantidad']}")
        elif opcion == '3':
            item = input("Item comprado: ")
            if item in lista:
                lista[item]['comprado'] = True
                print(f"{item} marcado como comprado")

organizador_compras()
