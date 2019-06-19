class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding vertex: {VERTEX} to the graph...".format(VERTEX=vertex.get_value()))
        self.graph_dict[vertex.get_value()] = vertex

    def add_edge(self, from_vertex, to_vertex):
        print("Adding edge from {fvertex} to {tvertex}".format(fvertex=from_vertex.get_value(), tvertex=to_vertex.get_value()))
        self.graph_dict[from_vertex.get_value()].add_edge(to_vertex)
        if self.directed is False:
            print("Adding edge from {tvertex} to {fvertex}".format(fvertex=from_vertex.get_value(), tvertex=to_vertex.get_value()))
            self.graph_dict[from_vertex.get_value()].add_edge(to_vertex.get_value())
