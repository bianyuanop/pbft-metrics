import networkx as nx
from typing import List
import matplotlib.pyplot as plt

state_color_map = {
    'Prepared': 'red',
    'Committed': 'blue',
    'NewRound': 'green',
}

action_color_map = {
    'PrePrepare': 'red',
    'Prepare': 'blue',
    'Commit': 'green',
}

class Graph:
    def __init__(self, edges: List) -> None:
        self.edges = edges
        def sortByTimestamp(e):
            return e['ts']

        self.edges.sort(key=sortByTimestamp)

        self.pos = 0

        self.G = nx.MultiGraph()

        self.nodes = {}

        node_set = set()
        for edge in self.edges:
            node_set.add(edge['origin'])
            node_set.add(edge['target'])
        
        for node in list(node_set):
            self.G.add_node(node)
            self.nodes[node] = {
                "state": "NewRound"            
            }
    
    # add one edge to the graph
    def next(self):
        if self.pos >= len(self.edges):
            return False
        
        edge = self.edges[self.pos]
        self.pos += 1

        self.nodes[edge['target']]['state'] = edge['state']

        self.G.add_edge(edge['origin'], edge['target'], 1, color = action_color_map[edge['action']])

        return True

    def to_graph(self):
        pass
            
    def draw(self):
        node_colors = []

        nodes = list(self.nodes.keys())
        nodes.sort()

        for node in nodes:
            node_colors.append(state_color_map[self.nodes[node]['state']])

        nx.draw(self.G, with_labels=True, node_color=node_colors,font_weight='bold', arrows=True, arrowstyle='->', arrowsize=10, width=2)
        plt.show()

