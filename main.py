from db import EdgeStore
from graph import Graph


if __name__ == '__main__':
    store = EdgeStore()

    edges = store.pickFromTo(0, 2)

    graph = Graph(edges)

    while graph.next():
        graph.draw()