from Graph import Graph, read_graph_from_file, write_graph_to_file, randomly_generate_graph


class Controller:

    def __init__(self):
        self.__graphs = []
        self.__current = None

    def add_default_graph(self, filename):
        if self.__current is None:
            self.__current = 0
        new_graph = Graph()
        read_graph_from_file(new_graph, filename)
        self.__graphs.append(new_graph)
        self.__current = len(self.__graphs) - 1

    def add_empty_graph(self):
        if self.__current is None:
            self.__current = 0
        new_graph = Graph()
        self.__graphs.append(new_graph)
        self.__current = len(self.__graphs) - 1

    def add_random_generated_graph(self, number_vertices, number_edges):
        if self.__current is None:
            self.__current = 0
        new_graph = randomly_generate_graph(number_vertices, number_edges)
        self.__graphs.append(new_graph)
        self.__current = len(self.__graphs) - 1

    def add_edge_current_graph(self, start_point, end_point, cost):
        self.__graphs[self.__current].add_edge(start_point, end_point, cost)

    def add_vertex_current_graph(self, vertex):
        self.__graphs[self.__current].add_vertex(vertex)

    def remove_vertex_current_graph(self, vertex):
        self.__graphs[self.__current].remove_vertex(vertex)

    def remove_edge_current_graph(self, start_point, end_point):
        self.__graphs[self.__current].remove_edge([start_point, end_point])

    def parseX_current(self):
        return self.__graphs[self.__current].parseX()

    def parseNIn_current(self, vertex):
        return self.__graphs[self.__current].parseNIn(vertex)

    def parseNOut_current(self, vertex):
        return self.__graphs[self.__current].parseNOut(vertex)

    def copy_current_graph(self):
        copy_graph = self.__graphs[self.__current].make_copy()
        self.__graphs.append(copy_graph)

    def get_degree_in_vertex_current(self, vertex):
        return self.__graphs[self.__current].degree_in(vertex)

    def get_degree_out_vertex_current(self, vertex):
        return self.__graphs[self.__current].degree_out(vertex)

    def modify_cost_edge_current(self, edge, new_cost):
        self.__graphs[self.__current].modify_cost(edge, new_cost)

    def check_for_edge_current(self, start_point, end_point):
        return self.__graphs[self.__current].check_if_edge(start_point, end_point)

    def write_current_graph_to_file(self):
        current_graph = self.__graphs[self.__current]
        output_file = "output" + str(self.__current) + ".txt"
        write_graph_to_file(current_graph, output_file)

    @property
    def graphs(self):
        return self.__graphs

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, value):
        self.__current = value

    @property
    def verticess(self):
        return self.__graphs[self.__current].vertices
