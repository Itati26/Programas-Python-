import heapq

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_arco(self, origen, destino, distancia):
        if origen not in self.nodos:
            self.nodos[origen] = []
        if destino not in self.nodos:
            self.nodos[destino] = []
        self.nodos[origen].append((destino, distancia))

    def dijkstra(self, inicio):
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[inicio] = 0
        predecesores = {nodo: None for nodo in self.nodos}
        cola = [(0, inicio)]

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)

            for vecino, peso in self.nodos[nodo_actual]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(cola, (nueva_distancia, vecino))

        return distancias, predecesores

    def ruta_mas_corta(self, inicio, fin):
        distancias, predecesores = self.dijkstra(inicio)
        ruta = []
        nodo = fin

        while nodo is not None:
            ruta.insert(0, nodo)
            nodo = predecesores[nodo]

        return ruta, distancias[fin]

# Interfaz de usuario
def main():
    grafo = Grafo()

    print("🔢 ¿Cuántos nodos tiene el grafo?")
    n = int(input("Número de nodos: "))
    nodos = []

    print("\n📍 Ingresa los nombres de los nodos:")
    for i in range(n):
        nombre = input(f"Nombre del nodo {i+1}: ")
        nodos.append(nombre)

    print("\n🔗 Ahora ingresa los arcos (conexiones entre nodos).")
    print("Escribe 'fin' cuando termines.")
    while True:
        entrada = input("Origen, Destino, Distancia (ej. A B 5): ")
        if entrada.lower() == 'fin':
            break
        try:
            origen, destino, distancia = entrada.split()
            distancia = float(distancia)
            grafo.agregar_arco(origen, destino, distancia)
        except:
            print("⚠️ Entrada inválida. Intenta de nuevo.")

    print("\n🎯 ¿Desde qué nodo quieres partir?")
    inicio = input("Nodo de inicio: ")

    print("🏁 ¿A qué nodo quieres llegar?")
    fin = input("Nodo de destino: ")

    if inicio not in grafo.nodos or fin not in grafo.nodos:
        print("❌ Uno de los nodos no existe en el grafo.")
        return

    ruta, distancia = grafo.ruta_mas_corta(inicio, fin)
    print(f"\n🛣️ Ruta más corta de {inicio} a {fin}: {' → '.join(ruta)}")
    print(f"📏 Distancia total: {distancia}")

if __name__ == "__main__":
    main()
