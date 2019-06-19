
class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_value(self): # SELF ADDED
        return self.value

    def get_edges(self):
        return self.edges.keys()

    def add_edge(self, vertex):
        print("Adding edge {VERTEX} to {VERTEX1}".format(VERTEX=vertex.get_value(),VERTEX1=self.get_value()))
        self.edges[vertex.get_value()] = True

