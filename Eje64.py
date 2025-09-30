import os
import shutil

def organizar_archivos():
    directorio = input("Ruta del directorio: ")
    
    for archivo in os.listdir(directorio):
        if os.path.isfile(os.path.join(directorio, archivo)):
            extension = archivo.split('.')[-1].upper()
            carpeta_destino = os.path.join(directorio, extension)
            
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            
            shutil.move(
                os.path.join(directorio, archivo),
                os.path.join(carpeta_destino, archivo)
            )
            print(f"Movido: {archivo} -> {extension}/")

organizar_archivos()
