
class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_value(self): # SELF ADDED
        return self.value

    def get_edges(self):
        return self.edges.keys()

    def add_edge(self, vertex, weight = 0):
        self.edges[vertex] = weight

