from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph  # Matriz de capacidades
        self.ROW = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[t]

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Matriz de capacidades
graph = [
    [0, 10, 5, 0],  # Nodo 1
    [0, 0, 15, 10], # Nodo 2
    [0, 0, 0, 10],  # Nodo 3
    [0, 0, 0, 0]    # Nodo 4
]

g = Graph(graph)

source = 0  # Nodo 1 (origen)
sink = 3    # Nodo 4 (destino)

print("El flujo máximo es:", g.ford_fulkerson(source, sink))
