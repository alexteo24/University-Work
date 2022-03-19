import copy
import random


class Graph:
    def __init__(self):
        self.__number_of_vertices = 0
        self.__number_of_edges = 0
        self.__vertices = []
        self.__dictionary_in = {}
        self.__dictionary_out = {}
        self.__dictionary_costs = {}

    def degree_in(self, vertex):
        """
        Gets and returns the in degree of a vertex
        :param vertex: - the vertex whose in degree we want to find
        :return: - the in degree of the vertex
        """
        return len(self.__dictionary_in[vertex])

    def degree_out(self, vertex):
        """
        Gets and returns the out degree of a vertex
        :param vertex: - the vertex whose out degree we want to find
        :return: - the in degree of the vertex
        """
        return len(self.__dictionary_out[vertex])

    def check_if_edge(self, first_vertex, second_vertex):
        """
        Checks if there is an edge between two vertices
        :param first_vertex: - the start of the edge
        :param second_vertex: - the edge of an edge
        :return: - the edge or false
        """
        try:
            if second_vertex in self.__dictionary_out[first_vertex]:
                return [first_vertex, second_vertex]
        except:
            pass
        return False

    def modify_cost(self, edge, new_cost):
        """
        Modifies the cost of an edge
        :param edge: - the edge
        :param new_cost: - new cost
        :return: -
        """
        tuple_edge = tuple(edge)
        self.__dictionary_costs[tuple_edge] = new_cost

    def add_vertex(self, vertex):
        """
        Adds a new vertex to the graph
        :param vertex: - the vertex to be added
        :return: - True if the addition was successful or false otherwise
        """
        if vertex in self.__vertices:
            return False
        else:
            self.__vertices.append(vertex)
            self.__dictionary_in[vertex] = []
            self.__dictionary_out[vertex] = []
            self.__number_of_vertices += 1
            return True

    def add_edge(self, start_point, end_point, cost):
        """
        Adds a new edge to the graph
        :param start_point: - the starting point of the edge
        :param end_point: - the ending point of the edge
        :param cost: - the cost of the edge
        :return: - True if the addition was successful or false otherwise
        """
        if start_point not in self.__vertices or end_point not in self.__vertices:
            return False
        else:
            self.__dictionary_in[end_point].append(start_point)
            self.__dictionary_out[start_point].append(end_point)
            edge = tuple([start_point, end_point])
            self.__dictionary_costs[edge] = cost
            self.__number_of_edges += 1
            return True

    def remove_edge(self, edge):
        """
        Removes an edge
        :param edge: - the edge to be removed
        :return: - raises an exception if the edge does not exist
        """
        edge_tuple = tuple(edge)
        if edge_tuple in self.__dictionary_costs:
            try:
                self.__number_of_edges -= 1
                start_point, end_point = edge
                self.__dictionary_in[end_point].remove(start_point)
                self.__dictionary_out[start_point].remove(end_point)
                del self.__dictionary_costs[edge_tuple]
                if len(self.__dictionary_in[end_point]) == 0:
                    del self.__dictionary_in[end_point]
                if len(self.__dictionary_in[start_point]) == 0:
                    del self.__dictionary_in[start_point]
            except:
                pass
        else:
            raise Exception("The edge does not belong to the graph!!!")

    def remove_vertex(self, vertex):
        """
        Removes a vertex
        :param vertex:  - the vertex to be removed
        :return: - raises exception if the vertex does not belong to the graph
        """
        if vertex in self.__vertices:
            self.__vertices.remove(vertex)
            self.__number_of_vertices -= 1
            if vertex in self.__dictionary_in:
                for start_point in self.__dictionary_in[vertex]:
                    self.__number_of_edges -= 1
                    edge = tuple([start_point, vertex])
                    self.__dictionary_out[start_point].remove(vertex)
                    del self.__dictionary_costs[edge]
                del self.__dictionary_in[vertex]
            if vertex in self.__dictionary_out:
                for end_point in self.__dictionary_out[vertex]:
                    self.__number_of_edges -= 1
                    edge = tuple([vertex, end_point])
                    self.__dictionary_in[end_point].remove(vertex)
                    del self.__dictionary_costs[edge]
                del self.__dictionary_out[vertex]
        else:
            raise Exception("The vertex does not belong to the graph!!!")

    def parseX(self):
        return VertexIterator(self.__vertices)

    def parseNIn(self, vertex):
        if vertex not in self.__dictionary_in:
            raise Exception("This vertex has no inbound edges!")
        return VertexIterator(self.__dictionary_in[vertex])

    def parseNOut(self, vertex):
        if vertex not in self.__dictionary_out:
            raise Exception("This vertex has no outbound edges!")
        return VertexIterator(self.__dictionary_out[vertex])

    def make_copy(self):
        """
        Makes a copy of the graph
        :return: - returns the copy of the graph
        """
        return copy.deepcopy(self)

    @property
    def number_vertices(self):
        return self.__number_of_vertices

    @number_vertices.setter
    def number_vertices(self, value):
        self.__number_of_vertices = value

    @property
    def number_edges(self):
        return self.__number_of_edges

    @number_edges.setter
    def number_edges(self, value):
        self.__number_of_edges = value

    @property
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self, value):
        self.__vertices = value

    @property
    def dictionary_in(self):
        return self.__dictionary_in

    @dictionary_in.setter
    def dictionary_in(self, value):
        self.__dictionary_in = copy.deepcopy(value)

    @property
    def dictionary_out(self):
        return self.__dictionary_out

    @dictionary_out.setter
    def dictionary_out(self, value):
        self.__dictionary_out = copy.deepcopy(value)

    @property
    def dictionary_costs(self):
        return self.__dictionary_costs

    @dictionary_costs.setter
    def dictionary_costs(self, value):
        self.__dictionary_costs = copy.deepcopy(value)


class VertexIterator:

    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.valid():
            self.__index += 1
            vertex = self.__data[self.__index]
            return vertex

    def valid(self):
        if self.__index == len(self.__data) - 1:
            return False
        return True


# class InboundOutboundIterator:
#
#     def __init__(self, data):
#         self.__data = data
#         self.__current = -1
#         self.__index = 0
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.valid():
#             if self.__current < len(self.__data[self.__index]):
#                 while self.__index not in self.__data:
#                     self.__index += 1
#                     self.__current = 0
#                 self.__current += 1
#                 return self.__current - 1
#             self.__index += 1
#             self.__current = 0
#
#     def valid(self):
#         if self.__index == len(self.__data) - 1:
#             return False
#         return True


def read_graph_from_file(A_graph, file_name):
    try:
        dictionary_in = {}
        dictionary_out = {}
        dictionary_costs = {}
        file = open(file_name, 'r')
        line = file.readline().strip()
        number_of_vertices, number_of_edges = line.split(' ')
        line = file.readline().strip()
        while len(line) > 0:
            start_point, end_point, cost = line.split(' ')
            start_point = int(start_point)
            end_point = int(end_point)
            cost = int(cost)
            if start_point not in A_graph.vertices:
                A_graph.vertices.append(start_point)
            if end_point not in A_graph.vertices:
                A_graph.vertices.append(end_point)
            if end_point in dictionary_in:
                dictionary_in[end_point].append(start_point)
            else:
                dictionary_in[end_point] = [start_point]
            if start_point in dictionary_out:
                dictionary_out[start_point].append(end_point)
            else:
                dictionary_out[start_point] = [end_point]
            dictionary_costs[(start_point, end_point)] = cost
            line = file.readline().strip()
        file.close()
        A_graph.number_vertices = int(number_of_vertices)
        A_graph.number_edges = int(number_of_edges)
        A_graph.dictionary_in = dictionary_in
        A_graph.dictionary_out = dictionary_out
        A_graph.dictionary_costs = dictionary_costs
    except Exception:
        raise Exception("There was an error while reading the graph!")


def write_graph_to_file(A_graph, file_name):
    try:
        file = open(file_name, "w")
        first_line = str(A_graph.number_vertices) + ' ' + str(A_graph.number_edges) + '\n'
        file.write(first_line)
        for starting_point in A_graph.dictionary_out:
            if len(A_graph.dictionary_out[starting_point]) == 0:
                new_line = str(starting_point) + '\n'
                file.write(new_line)
            else:
                for ending_point in A_graph.dictionary_out[starting_point]:
                    edge = tuple([starting_point, ending_point])
                    new_line = str(starting_point) + ' ' + str(ending_point) + ' ' +\
                               str(A_graph.dictionary_costs[edge]) + '\n'
                    file.write(new_line)
        file.close()
    except Exception:
        raise Exception("There was an error while writing the graph!")


def randomly_generate_graph(vertices, edges):
    if vertices * (vertices - 1) / 2 < edges:
        raise Exception("Invalid number of vertices and edges!!!")
    new_graph = Graph()
    new_graph.vertices = [i for i in range(0, vertices)]
    new_graph.number_vertices = vertices
    for i in range(0, vertices):
        new_graph.dictionary_out[i] = []
        new_graph.dictionary_in[i] = []
    current_edges = 0
    while current_edges < edges:
        start_point = random.randint(0, vertices - 1)
        end_point = random.randint(0, vertices - 1)
        cost = random.randint(0, 100)
        if new_graph.add_edge(start_point, end_point, cost):
            current_edges += 1
    return new_graph
