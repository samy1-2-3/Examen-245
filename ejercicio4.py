import networkx as nx
import matplotlib.pyplot as plt

familia = {
    'abuelos': ['abuelo1', 'abuela1', 'abuelo2', 'abuela2'],
    'padres': ['padre1', 'madre1', 'padre2', 'madre2'],
    'tios': ['tio1', 'tio2', 'tio3', 'tio4'],
    'primos': ['primo1', 'primo2', 'primo3', 'primo4'],
    'hijos': ['hijo1', 'hijo2']
}

G = nx.DiGraph()

# nodos
G.add_edge('abuelo1', 'padre1')
G.add_edge('abuela1', 'padre1')
G.add_edge('abuelo2', 'madre1')
G.add_edge('abuela2', 'madre1')
G.add_edge('padre1', 'hijo1')
G.add_edge('madre1', 'hijo1')
G.add_edge('padre1', 'hijo2')
G.add_edge('madre1', 'hijo2')
G.add_edge('abuelo1', 'tio1')
G.add_edge('abuela1', 'tio1')
G.add_edge('abuelo1', 'tio2')
G.add_edge('abuela1', 'tio2')
G.add_edge('abuelo2', 'tio3')
G.add_edge('abuela2', 'tio3')
G.add_edge('abuelo2', 'tio4')
G.add_edge('abuela2', 'tio4')
G.add_edge('tio1', 'primo1')
G.add_edge('tio1', 'primo2')
G.add_edge('tio3', 'primo3')
G.add_edge('tio3', 'primo4')

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)

plt.title("Árbol Genealógico")
plt.show()
