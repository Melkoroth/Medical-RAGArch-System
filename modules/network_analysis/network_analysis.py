
# Análisis de Redes y Conexiones con NetworkX

import networkx as nx
import matplotlib.pyplot as plt

# Creación del grafo
G = nx.Graph()
G.add_edges_from([
    ('Glucosa', 'Insulina'),
    ('Colesterol', 'Triglicéridos'),
    ('Presión Arterial', 'Sodio')
])

# Detección de Comunidades
communities = list(nx.community.label_propagation_communities(G))

# Visualización de Redes y Conexiones
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True)
plt.title("Análisis de Redes entre Biomarcadores")
plt.show()
