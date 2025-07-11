import pandas as pd
from collections import defaultdict

class ProyectoPERTCPM:
    def __init__(self):
        self.actividades = {}
        self.precedencias = defaultdict(list)
        self.ruta_critica = []
        self.tiempo_total = 0
        self.unidad_tiempo = "días"  # Valor por defecto, se cambiará según elección del usuario
        
    def seleccionar_unidad_tiempo(self):
        print("\n=== CONFIGURACIÓN DE UNIDADES DE TIEMPO ===")
        while True:
            unidad = input("¿Qué unidad de tiempo usará? (días/semanas): ").lower()
            if unidad in ["días", "dias", "dia", "día"]:
                self.unidad_tiempo = "días"
                break
            elif unidad in ["semanas", "semana", "sem"]:
                self.unidad_tiempo = "semanas"
                break
            else:
                print("Opción no válida. Por favor ingrese 'días' o 'semanas'")
    
    def capturar_datos(self):
        print(f"\n=== CAPTURA DE DATOS (en {self.unidad_tiempo}) ===")
        print("Ingrese las actividades y sus relaciones. Deje el nombre vacío para terminar.\n")
        
        while True:
            nombre = input("Nombre de la actividad (ej. A, B): ").upper().strip()
            if not nombre:
                break
                
            if nombre in self.actividades:
                print(f"¡Error! La actividad {nombre} ya existe.")
                continue
                
            # Capturar duración
            while True:
                try:
                    duracion = float(input(f"Duración de '{nombre}' (en {self.unidad_tiempo}): "))
                    if duracion <= 0:
                        print(f"La duración debe ser mayor que 0 {self.unidad_tiempo}")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un número válido")
            
            # Capturar precedentes
            while True:
                precedentes = input(f"Precedentes de '{nombre}' (separar por comas, dejar vacío si no tiene): ").upper()
                precedentes = [p.strip() for p in precedentes.split(",")] if precedentes else []
                
                # Validar precedentes
                invalidos = [p for p in precedentes if p not in self.actividades]
                if invalidos:
                    print(f"Actividades precedentes no existentes: {', '.join(invalidos)}")
                    print(f"Actividades existentes: {', '.join(self.actividades.keys()) or 'Ninguna'}")
                    continue
                break
            
            # Guardar actividad
            self.actividades[nombre] = {
                'nombre': nombre,
                'duracion': duracion,
                'precedentes': precedentes,
                'IP': 0, 'TP': 0, 'IL': 0, 'TL': 0, 'holgura': 0
            }
            
            # Registrar relaciones
            for p in precedentes:
                self.precedencias[p].append(nombre)
    
    def calcular_ruta_critica(self):
        if not self.actividades:
            return False
            
        # Verificar si hay ciclos
        try:
            orden_topologico = list(nx.topological_sort(nx.DiGraph(
                (pre, act) for act in self.actividades for pre in self.actividades[act]['precedentes']
            )))
        except nx.NetworkXUnfeasible:
            print("\n¡Error! Existe un ciclo en las dependencias (una actividad depende de sí misma directa o indirectamente)")
            return False
        
        # Pase hacia adelante
        for actividad in orden_topologico:
            datos = self.actividades[actividad]
            
            if not datos['precedentes']:
                datos['IP'] = 0
                datos['TP'] = datos['duracion']
            else:
                max_tp = max(self.actividades[p]['TP'] for p in datos['precedentes'])
                datos['IP'] = max_tp
                datos['TP'] = max_tp + datos['duracion']
        
        self.tiempo_total = max(act['TP'] for act in self.actividades.values())
        
        # Pase hacia atrás
        for actividad in reversed(orden_topologico):
            datos = self.actividades[actividad]
            
            if actividad not in self.precedencias or not self.precedencias[actividad]:
                datos['TL'] = self.tiempo_total
                datos['IL'] = self.tiempo_total - datos['duracion']
            else:
                min_il = min(self.actividades[s]['IL'] for s in self.precedencias[actividad])
                datos['TL'] = min_il
                datos['IL'] = min_il - datos['duracion']
            
            datos['holgura'] = datos['IL'] - datos['IP']
        
        # Identificar ruta crítica
        self.ruta_critica = [act for act in self.actividades if abs(self.actividades[act]['holgura']) < 1e-9]
        self.ruta_critica.sort(key=lambda x: self.actividades[x]['IP'])
        
        return True
    
    def mostrar_resultados(self):
        if not self.actividades:
            print("\nNo se ingresaron actividades")
            return
            
        print(f"\n=== RESULTADOS DEL PROYECTO (en {self.unidad_tiempo}) ===")
        
        # Tabla de actividades
        print("\nTABLA DE ACTIVIDADES")
        print("="*110)
        headers = [
            'Actividad', f'Duración ({self.unidad_tiempo})',
            f'Inicio Temprano ({self.unidad_tiempo})', f'Fin Temprano ({self.unidad_tiempo})',
            f'Inicio Tardío ({self.unidad_tiempo})', f'Fin Tardío ({self.unidad_tiempo})',
            f'Holgura ({self.unidad_tiempo})'
        ]
        print("{:<10} {:<12} {:<18} {:<18} {:<18} {:<18} {:<12}".format(*headers))
        print("-"*110)
        
        for nombre in sorted(self.actividades.keys()):
            act = self.actividades[nombre]
            print(
                f"{nombre:<10} {act['duracion']:<12.1f} "
                f"{act['IP']:<18.1f} {act['TP']:<18.1f} "
                f"{act['IL']:<18.1f} {act['TL']:<18.1f} "
                f"{act['holgura']:<12.1f}"
            )
        
        print("="*110)
        
        # Ruta crítica
        if self.ruta_critica:
            print(f"\nRUTA CRÍTICA: {' → '.join(self.ruta_critica)}")
            print(f"DURACIÓN TOTAL: {self.tiempo_total} {self.unidad_tiempo}")
            
            print("\nCRONOGRAMA RUTA CRÍTICA:")
            for i, act in enumerate(self.ruta_critica, 1):
                datos = self.actividades[act]
                print(
                    f"{i}. {act}: {datos['IP']:.1f}-{datos['TP']:.1f} {self.unidad_tiempo} "
                    f"(Duración: {datos['duracion']} {self.unidad_tiempo})"
                )
        else:
            print("\nNo se pudo determinar una ruta crítica")

def main():
    print("ANÁLISIS DE RUTA CRÍTICA (PERT/CPM)")
    print("===================================")
    
    proyecto = ProyectoPERTCPM()
    proyecto.seleccionar_unidad_tiempo()
    proyecto.capturar_datos()
    
    if proyecto.actividades:
        if proyecto.calcular_ruta_critica():
            proyecto.mostrar_resultados()

if __name__ == "__main__":
    import networkx as nx  # Solo necesario para detección de ciclos
    main()
