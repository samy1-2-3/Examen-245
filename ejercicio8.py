import itertools
grafo = {
    'A': {'B': 2, 'C': 4, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'A': 4, 'B': 3, 'D': 3, 'E': 2},
    'D': {'A': 1, 'B': 2, 'C': 3, 'E': 2, 'F': 3},
    'E': {'C': 2, 'D': 2, 'F': 2, 'G': 4},
    'F': {'D': 3, 'E': 2, 'G': 3},
    'G': {'E': 4, 'F': 3}
}

def generaRcam(grafo):
    nodos = list(grafo.keys())
    caminos = itertools.permutations(nodos)
    return caminos

for camino in generaRcam(grafo):
    print(camino)
