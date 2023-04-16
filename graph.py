from random import randint
import networkx as nx
from typing import List
import matplotlib.pyplot as plt

state_color_map = {
    'Prepared': '#42d4f4',
    'Committed': '#dcbeff',
    'NewRound': '#808000',
    'RoundChange': '#800000',
    'FinalCommitted': '#911eb4',
}

# the nodes will only send actions once they already in that state except RoundChange
# e.g. send NewRound 
action_color_map = {
    'PrePrepare': '#000075',
    'Prepare': '#42d4f4',
    'Commit': '#dcbeff',
    'NewRound': '#e6194B',
    'RoundChange': '#800000'
}

class Graph:
    def __init__(self, edges: List) -> None:
        plt.ion()
        self.edges = edges
        def sortByTimestamp(e):
            return e['ts']

        self.edges.sort(key=sortByTimestamp)

        self.pos = 0

        self.G = nx.MultiDiGraph()

        self.nodes = {}

        node_set = set()
        for edge in self.edges:
            node_set.add(edge['origin'])
            node_set.add(edge['target'])

        nodes_pos = {}
        
        for node in list(node_set):
            self.G.add_node(node)
            self.nodes[node] = {
                "state": "NewRound"            
            }

            nodes_pos[node] = [randint(0, 200), randint(0, 200)]
        
        self.layout = nx.layout.spring_layout(self.G, k=20, pos=nodes_pos, fixed=list(self.nodes))
    
    # add one edge to the graph
    def next(self):
        if self.pos >= len(self.edges):
            return False
        
        edge = self.edges[self.pos]

        print(edge)
        print(self.pos)

        self.pos += 1

        self.nodes[edge['target']]['state'] = edge['state']

        # if edge['action'] == 'PrePrepare' or edge['action'] == 'Prepare':
        #     self.nodes[edge['origin']]['state'] = 'Prepared'
        # elif edge['action'] == 'Commit':
        #     self.nodes[edge['origin']]['state'] = 'Committed'
        # elif edge['action'] == 'NewRound':
        #     self.nodes[edge['origin']]['state'] = 'NewRound'
        

        edges2remove = [[e[0], e[1]] for e in self.G.edges 
                        if [e[0], e[1]] == [edge['origin'], edge['target']] or [e[0], e[1]] == [edge['target'], edge['origin']] ]
        self.G.remove_edges_from(edges2remove)

        self.G.add_edge(edge['origin'], edge['target'], 1, color = action_color_map[edge['action']])

        return True

    def to_graph(self):
        pass
            
    def draw(self):
        node_colors = []

        for node in self.G.nodes:
            node_colors.append(state_color_map[self.nodes[node]['state']]) 
        
        edge_colors = []


        for (u,v,attrib_dict) in list(self.G.edges.data()):
            edge_colors.append(attrib_dict['color'])

        nx.draw(
            self.G, 
            pos=self.layout,
            with_labels=True,
            node_color=node_colors,
            edge_color=edge_colors,
            font_weight='bold',
            arrows=True,
            arrowstyle='->',
            arrowsize=10,
            width=2
        )

        plt.show()
        plt.pause(0.5)

