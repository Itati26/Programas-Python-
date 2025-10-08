import datetime

def generar_plan_estudios():
    materia = input("Materia a estudiar: ")
    horas_totales = int(input("Horas totales necesarias: "))
    fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
    
    fecha_limite = datetime.datetime.strptime(fecha_limite, "%Y-%m-%d")
    hoy = datetime.datetime.now()
    dias_disponibles = (fecha_limite - hoy).days
    
    if dias_disponibles <= 0:
        print("¡La fecha límite ya pasó!")
        return
    
    horas_por_dia = horas_totales / dias_disponibles
    
    print(f"\nPlan de estudio para: {materia}")
    print(f"Horas diarias necesarias: {horas_por_dia:.2f}")
    print(f"Sesión de estudio recomendada: {horas_por_dia * 60:.0f} minutos al día")

generar_plan_estudios()
