import time
import datetime

def recordatorio_agua():
    print("Recordatorio de agua activado (8 horas)")
    inicio = datetime.datetime.now()
    
    for i in range(1, 9):
        time.sleep(1)  # En realidad sería 3600 segundos (1 hora)
        print(f"[{datetime.datetime.now().strftime('%H:%M')}] Recordatorio {i}/8: ¡Toma agua!")
    
    print("Jornada completada. ¡Bien hidratado!")

recordatorio_agua()
