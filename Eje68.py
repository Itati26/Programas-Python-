def contador_palabras_archivo():
    nombre_archivo = input("Nombre del archivo: ")
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            lineas = contenido.split('\n')
            
            print(f"Palabras: {len(palabras)}")
            print(f"Líneas: {len(lineas)}")
            print(f"Caracteres: {len(contenido)}")
            
    except FileNotFoundError:
        print("Archivo no encontrado")

contador_palabras_archivo()
