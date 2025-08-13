import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Carga las tareas desde el archivo JSON."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Guarda las tareas en el archivo JSON."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Añade una nueva tarea."""
    task = input("📝 Ingresa la nueva tarea: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("✅ Tarea añadida.")

def show_tasks(tasks):
    """Muestra todas las tareas."""
    if not tasks:
        print("No hay tareas pendientes. ¡Buen trabajo! 🎉")
        return
    
    print("\n📋 Lista de tareas:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

def complete_task(tasks):
    """Marca una tarea como completada."""
    show_tasks(tasks)
    try:
        index = int(input("\n🔢 Número de tarea completada: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("✅ Tarea completada.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Ingresa un número válido.")

def delete_task(tasks):
    """Elimina una tarea."""
    show_tasks(tasks)
    try:
        index = int(input("\n🔢 Número de tarea a eliminar: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Tarea eliminada: '{deleted_task['task']}'")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Ingresa un número válido.")

def main():
    """Menú principal."""
    tasks = load_tasks()
    
    while True:
        print("\n📌 To-Do List - Menú:")
        print("1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        choice = input("👉 Selecciona una opción: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
