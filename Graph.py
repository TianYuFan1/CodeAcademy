class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding vertex: {VERTEX} to the graph...".format(VERTEX=vertex.get_value()))
        self.graph_dict[vertex.get_value()] = vertex

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        print("Adding edge from {fvertex} to {tvertex}".format(fvertex=from_vertex.get_value(), tvertex=to_vertex.get_value()))
        self.graph_dict[from_vertex.get_value()].add_edge(to_vertex, weight)
        if self.directed is False:
            print("Adding edge from {tvertex} to {fvertex}".format(fvertex=from_vertex.get_value(), tvertex=to_vertex.get_value()))
            self.graph_dict[to_vertex.get_value()].add_edge(from_vertex, weight)

    def find_path(self, start_vertex, end_vertex):
        print("Finding path between {start} and {end}".format(start=start_vertex.get_value(), end=end_vertex.get_value()))
        start = [start_vertex]
        seen = {}
        while start != []:
            current_vertex = start.pop()
            seen[current_vertex] = True
            if current_vertex is end_vertex:
                return True
            else:

                next_vertices = [vertex for vertex in current_vertex.get_edges() if vertex not in seen]
                start += next_vertices
            print("Visiting: {VERTEX}".format(VERTEX=current_vertex.get_value()))
        return False
