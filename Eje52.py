contactos = {}

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    contactos[nombre] = {'telefono': telefono, 'email': email}
    print("Contacto agregado")

def buscar_contacto():
    nombre = input("Nombre a buscar: ")
    if nombre in contactos:
        print(f"Teléfono: {contactos[nombre]['telefono']}")
        print(f"Email: {contactos[nombre]['email']}")
    else:
        print("Contacto no encontrado")

while True:
    print("\n1. Agregar contacto\n2. Buscar contacto\n3. Salir")
    opcion = input("Opción: ")
    if opcion == '3': break
    if opcion == '1': agregar_contacto()
    if opcion == '2': buscar_contacto()
