import re

def validar_email():
    email = input("Email a validar: ")
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(patron, email):
        print("Email válido")
        
        # Información adicional
        usuario, dominio = email.split('@')
        print(f"Usuario: {usuario}")
        print(f"Dominio: {dominio}")
    else:
        print("Email inválido")

validar_email()
