
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Inicializamos las distancias de cada nodo a infinito
    distances = {node: float('inf') for node in graph}
    # La distancia del nodo de inicio a sí mismo es 0
    distances[start] = 0
    # Creamos un heap con la distancia del nodo de inicio a sí mismo
    heap = [(0, start)]
    # Creamos un grafo vacío
    G = nx.Graph()
    while heap:
        # Obtenemos el nodo con la menor distancia
        (current_distance, current_vertex) = heapq.heappop(heap)
        # Si la distancia actual es mayor que la almacenada en distances[current_vertex], ignoramos este nodo
        if current_distance > distances[current_vertex]:
            continue
        # Para cada vecino del nodo actual
        for neighbor, weight in graph[current_vertex].items():
            # Calculamos la distancia desde el nodo de inicio al vecino actual
            distance = current_distance + weight
            # Si la distancia calculada es menor que la almacenada en distances[neighbor], actualizamos distances[neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Agregamos el vecino actual al heap con su nueva distancia
                heapq.heappush(heap, (distance, neighbor))
                # Agregamos una arista al grafo entre el nodo actual y su vecino con peso weight
                G.add_edge(current_vertex, neighbor, weight=weight)
        # Imprimimos las distancias actuales en consola
        print(f"Distancias actuales: {distances}")
    return G

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 3},
    'C': {'A': 1, 'D': 2},
    'D': {'B': 3, 'C': 2}
}

G = dijkstra(graph, 'A')

# Dibujamos el grafo utilizando networkx y matplotlib
pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G),edge_labels=nx.get_edge_attributes(G,'weight'))
plt.show()


