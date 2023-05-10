#Jonatan Sanchez Ibarra 
#20310417
#6E

import sys

def dijkstra_simulator(graph, n, source):
    # Se inicializan las distancias y los conjunto de nodos visitados
    dist = [sys.maxsize] * n
    dist[source] = 0
    visited = set()

    # Se muestra el estado inicial
    print("Estado inicial:")
    print_grid(graph, dist, visited)

    # Iterar hasta visitar todos los nodos
    while len(visited) != n:
        # Seleccionar el nodo con la distancia más corta
        u = min((dist[i], i) for i in range(n) if i not in visited)[1]
        # Marcar el nodo como visitado
        visited.add(u)

        # Actualizar las distancias de los nodos adyacentes
        for v in range(n):
            if graph[u][v] != 0:
                alt = dist[u] + graph[u][v]
                if alt < dist[v]:
                    dist[v] = alt

        # Mostrar el estado actual
        print("Paso:", len(visited))
        print_grid(graph, dist, visited)
    return dist

def print_grid(graph, dist, visited):
    #Se muestra el grid
    n = len(graph)
    for i in range(n):
        row = ""
        for j in range(n):
            if i == j:
                row += "-"
            elif graph[i][j] == 0:
                row += "X"
            elif j in visited:
                row += "V"
            elif dist[j] == sys.maxsize:
                row += "inf"
            else:
                row += str(dist[j])
            row += " "
        print(row)


#Se obtiene la entrada del usuario
n = int(input("Ingrese el número de nodos: "))
graph = []
for i in range(n):
    row = list(map(int, input("Ingrese la fila {} de la matriz de adyacencia: ".format(i+1)).split()))
    graph.append(row)
source = int(input("Ingrese el nodo de origen: "))

# Ejecutar el simulador del algoritmo de Dijkstra
dist = dijkstra_simulator(graph, n, source)

# Se muestra el resultado final
print("La distancia más corta desde el nodo de origen es:")
for i in range(n):
    if i == source:
        continue
    print("hasta el nodo", i, "es", dist[i])