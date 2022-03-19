import copy
import random
import time


class Graph:
    def __init__(self):
        self.__number_of_vertices = 0
        self.__number_of_edges = 0
        self.__vertices = []
        self.__dictionary_in = {}

    def degree_in(self, vertex):
        """
        Gets and returns the in degree of a vertex
        :param vertex: - the vertex whose in degree we want to find
        :return: - the in degree of the vertex
        """
        return len(self.__dictionary_in[vertex])

    def check_if_edge(self, first_vertex, second_vertex):
        """
        Checks if there is an edge between two vertices
        :param first_vertex: - the start of the edge
        :param second_vertex: - the edge of an edge
        :return: - the edge or false
        """
        try:
            if second_vertex in self.__dictionary_in[first_vertex]:
                return [first_vertex, second_vertex]
        except:
            pass
        return False

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
            self.__number_of_vertices += 1
            return True

    def add_edge(self, start_point, end_point):
        """
        Adds a new edge to the graph
        :param start_point: - the starting point of the edge
        :param end_point: - the ending point of the edge
        :return: - True if the addition was successful or false otherwise
        """
        if start_point not in self.__vertices or end_point not in self.__vertices:
            return False
        else:
            if start_point != end_point:
                if end_point not in self.__dictionary_in[start_point]:
                    self.__dictionary_in[start_point].append(end_point)
                    self.__dictionary_in[end_point].append(start_point)
                    self.__number_of_edges += 1
                    return True
                else:
                    return False
            else:
                return False

    def remove_edge(self, edge):
        """
        Removes an edge
        :param edge: - the edge to be removed
        :return: - raises an exception if the edge does not exist
        """
        start_point, end_point = edge
        if end_point in self.__dictionary_in[start_point]:
            self.__dictionary_in[start_point].remove(end_point)
            self.__dictionary_in[end_point].remove(start_point)
            self.__number_of_edges -= 1
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
                    self.__dictionary_in[start_point].remove(vertex)
                self.__dictionary_in.pop(vertex)
        else:
            raise Exception("The vertex does not belong to the graph!!!")

    def find_clique(self):
        min_vertex = -1
        nr_vertices = self.__number_of_vertices
        copy_dict_in = self.__dictionary_in
        while nr_vertices > 1:
            min = 999999
            for vertex in self.__vertices:
                if min > len(self.__dictionary_in[vertex]):
                    min = len(self.__dictionary_in[vertex])
                    min_vertex = vertex
            if min == nr_vertices - 1:
                print("The size of the maximal clique is " + str(min + 1))
                return
            self.remove_vertex(min_vertex)
            nr_vertices -= 1
        self.__dictionary_in = copy_dict_in
        print("There is no clique")

    # def maybe_better_find_clique(self):
    #     maximum_clique = []
    #     possible_new_clique = [1 for _ in range(0, self.__number_of_vertices)]
    #     available_vertices = self.__vertices
    #     vertex = 0
    #     if possible_new_clique[vertex] == 1:
    #         current_clique = [vertex]
    #         for adjacent in self.__dictionary_in[vertex]:
    #             good = True
    #             for member in current_clique:
    #                 if member not in self.__dictionary_in[adjacent]:
    #                     good = False
    #                     break
    #             if good:
    #                 current_clique.append(adjacent)
    #         # for member in current_clique:
    #         #     if len(self.__dictionary_in)
    #     print("End")

    def parseX(self):
        return VertexIterator(self.__vertices)

    def parseNIn(self, vertex):
        if vertex not in self.__dictionary_in:
            raise Exception("This vertex has no inbound edges!")
        return VertexIterator(self.__dictionary_in[vertex])

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


def read_graph_from_file(A_graph, file_name):
    start_time = time.time()
    try:
        dictionary_in = {}
        file = open(file_name, 'r')
        line = file.readline().strip()
        number_of_vertices, number_of_edges = line.split(' ')
        line = file.readline().strip()
        quantity = int(number_of_vertices)
        for i in range(0, quantity):
            dictionary_in[i] = []
        while len(line) > 0:
            start_point, end_point = line.split(' ')
            start_point = int(start_point)
            end_point = int(end_point)
            if start_point not in dictionary_in[end_point]:
                dictionary_in[end_point].append(start_point)
            if end_point not in dictionary_in[start_point]:
                dictionary_in[start_point].append(end_point)
            line = file.readline().strip()
        file.close()
        A_graph.number_vertices = int(number_of_vertices)
        A_graph.number_edges = int(number_of_edges)
        A_graph.dictionary_in = dictionary_in
    except Exception:
        raise Exception("There was an error while reading the graph!")
    A_graph.vertices = [x for x in range(0, quantity) if (len(dictionary_in[x]) > 0)]
    print(file_name)
    print(time.time()-start_time)


def write_graph_to_file(A_graph, file_name):
    try:
        visited = [0 for i in range(0, A_graph.number_vertices + 1)]
        file = open(file_name, "w")
        first_line = str(A_graph.number_vertices) + ' ' + str(A_graph.number_edges) + '\n'
        file.write(first_line)
        for starting_point in A_graph.dictionary_in:
            visited[starting_point] = 1
            if len(A_graph.dictionary_in[starting_point]) != 0:
                for ending_point in A_graph.dictionary_in[starting_point]:
                    if visited[ending_point] == 0:
                        new_line = str(starting_point) + ' ' + str(ending_point) + '\n'
                        file.write(new_line)
        file.close()
    except Exception:
        raise Exception("There was an error while writing the graph!")


def randomly_generate_graph(vertices, edges):
    if vertices * (vertices - 1) < edges:
        raise Exception("Invalid number of vertices and edges!!!")
    new_graph = Graph()
    new_graph.vertices = [i for i in range(0, vertices)]
    new_graph.number_vertices = vertices
    for i in range(0, vertices):
        new_graph.dictionary_in[i] = []
    current_edges = 0
    while current_edges < edges:
        start_point = random.randint(0, vertices - 1)
        end_point = random.randint(0, vertices - 1)
        if new_graph.add_edge(start_point, end_point):
            current_edges += 1
    return new_graph


graph = Graph()
read_graph_from_file(graph, "test.in")
graph.find_clique()
# graph.maybe_better_find_clique()
# 1. Given an undirected graph, find a clique of maximum size.
