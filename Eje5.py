import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

class CPMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPM - Ruta Crítica con Diagrama")
        self.activities = []

        # Interfaz
        tk.Label(root, text="Actividad").grid(row=0, column=0)
        tk.Label(root, text="Duración").grid(row=0, column=1)
        tk.Label(root, text="Predecesores (separados por coma)").grid(row=0, column=2)

        self.activity_entry = tk.Entry(root)
        self.duration_entry = tk.Entry(root)
        self.predecessor_entry = tk.Entry(root)

        self.activity_entry.grid(row=1, column=0)
        self.duration_entry.grid(row=1, column=1)
        self.predecessor_entry.grid(row=1, column=2)

        tk.Button(root, text="Agregar Actividad", command=self.add_activity).grid(row=1, column=3)
        tk.Button(root, text="Calcular Ruta Crítica", command=self.calculate_cpm).grid(row=2, column=1, columnspan=2)

    def add_activity(self):
        act = self.activity_entry.get().strip()
        dur = self.duration_entry.get().strip()
        pred = self.predecessor_entry.get().strip()

        if not act or not dur.isdigit():
            messagebox.showerror("Error", "Datos inválidos.")
            return

        self.activities.append({
            'id': act,
            'duration': int(dur),
            'predecessors': [p.strip() for p in pred.split(',') if p.strip()]
        })

        self.activity_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.predecessor_entry.delete(0, tk.END)

    def calculate_cpm(self):
        G = nx.DiGraph()
        for act in self.activities:
            G.add_node(act['id'], duration=act['duration'])
            for pred in act['predecessors']:
                G.add_edge(pred, act['id'])

        # Forward pass
        es = {}
        ef = {}
        for node in nx.topological_sort(G):
            es[node] = max([ef.get(pred, 0) for pred in G.predecessors(node)], default=0)
            ef[node] = es[node] + G.nodes[node]['duration']

        # Backward pass
        max_time = max(ef.values())
        lf = {node: max_time for node in G.nodes()}
        ls = {}
        for node in reversed(list(nx.topological_sort(G))):
            for succ in G.successors(node):
                lf[node] = min(lf[node], ls[succ])
            ls[node] = lf[node] - G.nodes[node]['duration']

        # Holgura y ruta crítica
        slack = {node: ls[node] - es[node] for node in G.nodes()}
        critical_path = [node for node in G.nodes() if slack[node] == 0]

        # Dibujar grafo
        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 6))
        for node in G.nodes():
            label = f"{node}\nES:{es[node]} EF:{ef[node]}\nLS:{ls[node]} LF:{lf[node]}"
            color = 'red' if node in critical_path else 'lightblue'
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=color, node_size=2000)
            nx.draw_networkx_labels(G, pos, labels={node: label}, font_size=8)

        nx.draw_networkx_edges(G, pos, arrows=True)
        plt.title("Diagrama de Red - Método CPM")
        plt.axis('off')
        plt.show()

# Ejecutar la app
root = tk.Tk()
app = CPMApp(root)
root.mainloop()
