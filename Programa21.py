import networkx as nx
import matplotlib.pyplot as plt

# Datos del ejercicio
actividades = {
    'a': {'predecesores': [], 'duracion': 3},
    'b': {'predecesores': ['a'], 'duracion': 2},
    'c': {'predecesores': [], 'duracion': 5},
    'd': {'predecesores': ['b', 'c'], 'duracion': 5},
    'e': {'predecesores': ['a'], 'duracion': 4},
    'f': {'predecesores': ['b', 'c'], 'duracion': 6},
    'g': {'predecesores': ['e', 'd'], 'duracion': 5}
}

# Crear grafo dirigido
G = nx.DiGraph()

# Agregar nodos y aristas
for act, datos in actividades.items():
    G.add_node(act, duracion=datos['duracion'])
    for pred in datos['predecesores']:
        G.add_edge(pred, act)

# Función para calcular tiempos tempranos y tardíos
def calcular_caminos(G):
    earliest_start = {}
    latest_start = {}
    top_order = list(nx.topological_sort(G))

    # Pase hacia adelante
    for node in top_order:
        preds = list(G.predecessors(node))
        if preds:
            earliest_start[node] = max(earliest_start[p] + G.nodes[p]['duracion'] for p in preds)
        else:
            earliest_start[node] = 0

    # Pase hacia atrás
    latest_start = {node: float('inf') for node in G.nodes}
    end_time = max(earliest_start[n] + G.nodes[n]['duracion'] for n in G.nodes)
    for node in reversed(top_order):
        succs = list(G.successors(node))
        if succs:
            latest_start[node] = min(latest_start[s] - G.nodes[node]['duracion'] for s in succs)
        else:
            latest_start[node] = end_time - G.nodes[node]['duracion']

    return earliest_start, latest_start, end_time

# Calcular rutas
earliest, latest, duracion_total = calcular_caminos(G)

# Identificar ruta crítica
ruta_critica = [n for n in G.nodes if earliest[n] == latest[n]]

# Mostrar resultados
print("Ruta crítica:", ' → '.join(ruta_critica))
print("Duración total del proyecto:", duracion_total, "días")

# Dibujar grafo
pos = nx.spring_layout(G, seed=42)
labels = {n: f"{n}\n({earliest[n]}/{latest[n]})" for n in G.nodes}
node_colors = ['red' if n in ruta_critica else 'lightblue' for n in G.nodes]

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors, node_size=2000, font_size=10, font_weight='bold', arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): '' for u, v in G.edges})
plt.title("Diagrama de Red con Ruta Crítica")
plt.axis('off')
plt.show()
