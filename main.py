import sys
import os
from db import EdgeStore
from graph import Graph


if __name__ == '__main__':
    store = EdgeStore()

    argv = sys.argv

    if len(argv) < 2:
        print("please provide the number of messages you want to display")
        os._exit(1)
    
    count = int(argv[1])

    edges = store.pickByNumMessages(count)

    graph = Graph(edges)

    while graph.next():
        graph.draw()