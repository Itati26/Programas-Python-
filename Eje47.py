tareas = []
while True:
    print("\n1. Agregar tarea  2. Ver tareas  3. Salir")
    opcion = input("Opción: ")
    if opcion == '3': break
    if opcion == '1': tareas.append(input("Tarea: "))
    if opcion == '2': [print(f"{i+1}. {t}") for i, t in enumerate(tareas)]
