import random
import string

def generar_password(longitud=12):
    """
    Genera una contraseña aleatoria segura.
    
    Args:
        longitud (int): Longitud de la contraseña (mínimo 8 caracteres)
    
    Returns:
        str: Contraseña generada
    """
    if longitud < 8:
        longitud = 8
    
    # Combinar diferentes tipos de caracteres
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generar contraseña aleatoria
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return password

def main():
    print("🔒 Generador de Contraseñas Seguras 🔒")
    print("=" * 40)
    
    try:
        longitud = int(input("Longitud de la contraseña (mínimo 8): "))
        cantidad = int(input("¿Cuántas contraseñas generar?: "))
        
        print("\nTus contraseñas seguras:")
        print("-" * 30)
        
        for i in range(cantidad):
            password = generar_password(longitud)
            print(f"{i+1}. {password}")
            
    except ValueError:
        print("❌ Error: Por favor ingresa números
