#Jonatan Sanchez Ibarra 
#20310417
#6E

from collections import defaultdict

def prim(graph, start):
    # Inicializar la lista de nodos visitados y el árbol parcial mínimo
    visit = set([start])
    mst = []
    
    while len(visit) < len(graph):
        # Encontrar todas las aristas que conectan nodos visitados y no visitados
        candidates = []
        for v in visit:
            for w, weight in graph[v]:
                if w not in visit:
                    candidates.append((v, w, weight))
        
        # Seleccionar la arista con el peso mínimo
        min_edge = min(candidates, key=lambda x: x[2])
        
        # Agregar el nodo no visitado y la arista al árbol parcial mínimo
        visit.add(min_edge[1])
        mst.append(min_edge)
    
    return mst

if __name__ == '__main__':
    # Definir el grafo como un diccionario de listas de tuplas (nodo, peso)
    graph = defaultdict(list)
    graph[1] = [(2, 2), (3, 3), (4, 1)]
    graph[2] = [(1, 2), (3, 4), (5, 5)]
    graph[3] = [(1, 3), (2, 4), (4, 6), (5, 7)]
    graph[4] = [(1, 1), (3, 6), (5, 8)]
    graph[5] = [(2, 5), (3, 7), (4, 8)]
    
    # Ejecutar el algoritmo de Prim y mostrar el árbol parcial mínimo paso a paso
    start = 1
    visit = set([start])
    mst = []
    
    print("Paso 0: Árbol parcial mínimo vacío")
    print(mst)
    
    while len(visit) < len(graph):
        candidates = []
        for v in visit:
            for w, weight in graph[v]:
                if w not in visit:
                    candidates.append((v, w, weight))
        
        min_edge = min(candidates, key=lambda x: x[2])
        visit.add(min_edge[1])
        mst.append(min_edge)
         #Se Imprimen los pasos
        print(f"\nPaso {len(visit)-1}: Añadir arista ({min_edge[0]}, {min_edge[1]}) con peso {min_edge[2]}")
        print(mst)
