import os
import shutil

def organizar_archivos(directorio):
    if not os.path.exists(directorio):
        print("Directorio no existe")
        return
    
    for archivo in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, archivo)
        
        if os.path.isfile(ruta_completa):
            extension = archivo.split('.')[-1] if '.' in archivo else 'SinExtension'
            carpeta_destino = os.path.join(directorio, extension)
            
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            
            shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
            print(f"Movido: {archivo} -> {extension}/")

directorio = input("Ruta del directorio a organizar: ")
organizar_archivos(directorio)
print("Organización completada")
