import networkx as nx
import matplotlib.pyplot as plt


class Dijkstra:
    def __init__(self):
        self.odleglosci = {}
        self.odwiedzone = []
        for i in GRAF.keys():
            self.odleglosci[i] = float('inf')

    def algorytm(self, graf, poczatek, koniec):
        # TODO: obsłużyć przypadek, w którym użytkownik podaje punkty końcowy oraz początkowy nie będącym w grafie
        #  spójnym
        print('\n', 10 * '=', poczatek, 10 * "=")

        if self.odleglosci[poczatek] == float('inf'):
            self.odleglosci[poczatek] = 0

        koszt = self.odleglosci[poczatek]
        minimalna_droga = float('inf')
        najblizszy_wierzcholek = ''
        for edge, dst in graf[poczatek].items():
            print(edge, dst, end=", ")
            if self.odleglosci[edge] > dst + koszt and edge not in self.odwiedzone:
                self.odleglosci[edge] = dst + koszt
            if dst + koszt < minimalna_droga and edge not in self.odwiedzone:
                minimalna_droga = dst + koszt
                najblizszy_wierzcholek = edge
        self.odwiedzone.append(poczatek)
        if poczatek == koniec:
            return self.odleglosci[koniec]
        return self.algorytm(graf, najblizszy_wierzcholek, koniec)


G = nx.Graph()

GRAF = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
    'D': {'B': 8, 'C': 2, 'F': 22, 'E': 11},
    'E': {'C': 5, 'D': 11, 'F': 1},
    'F': {'E': 1, 'D': 22}
    # ===
    # 'A': {'B': 1, 'C': 3},
    # 'B': {'A': 1, 'C': 2, 'D': 4},
    # 'C': {'A': 3, 'B': 2, 'D': 1},
    # 'D': {'B': 4, 'C': 1}
    # ===
    # 'A': {'B': 1, 'C': 3, 'D': 7},
    # 'B': {'A': 1, 'C': 2, 'E': 6, 'F': 2},
    # 'C': {'A': 3, 'B': 2, 'D': 1, 'E': 3},
    # 'D': {'A': 7, 'C': 1, 'G': 2},
    # 'E': {'B': 6, 'C': 3, 'F': 1, 'G': 5},
    # 'F': {'B': 2, 'E': 1, 'G': 4},
    # 'G': {'D': 2, 'E': 5, 'F': 4}
}

x = Dijkstra()
y = x.algorytm(GRAF, '_', 'F')
print('\n', x.odleglosci)
print("odłegłość z pkt A do G to:", y)

# Dodawanie wierzchołków i krawędzi do grafu
edges = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'C', 3),
    ('B', 'D', 8),
    ('C', 'E', 5),
    ('C', 'D', 2),
    ('D', 'F', 22),
    ('D', 'E', 11),
    ('E', 'F', 1),
]
G.add_weighted_edges_from(edges)

# Rysowanie grafu
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
