import copy
import random
import time


class Graph:
    def __init__(self):
        self.__number_of_vertices = 0
        self.__number_of_edges = 0
        self.__vertices = []
        self.__dictionary_in = {}
        self.__dictionary_costs = {}

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
        else:
            raise Exception("The vertex does not belong to the graph!!!")

    def prim_algorithm_init(self):
        selected = [0 for _ in range(self.__number_of_vertices)]
        vertices_tree = 0
        selected[0] = 1
        print("Edge  :  Weight\n")
        while vertices_tree < self.__number_of_vertices - 1:
            minimum = 9999999
            x = 0
            y = 0
            for i in self.__vertices:
                if selected[i]:
                    for j in self.__dictionary_in[i]:
                        if not selected[j]:
                            # not in selected and there is an edge
                            if minimum > self.__dictionary_costs[tuple([i, j])]:
                                minimum = self.__dictionary_costs[tuple([i, j])]
                                x = i
                                y = j
            print(str(x) + " - " + str(y) + " : " + str(self.__dictionary_costs[tuple([x, y])]))
            selected[y] = 1
            vertices_tree += 1

    def prim_algorithm(self):
        connection = [9999999 for _ in range(self.__number_of_vertices)]
        edges = [-1 for _ in range(self.__number_of_vertices)]
        forest = []
        vertices = [1 for _ in range(self.__number_of_vertices)]
        sum = self.__number_of_vertices
        sum -= vertices[0]
        vertices[0] = 0
        minimum = 9999999
        best = -1
        for x in self.__dictionary_in[0]:
            if connection[x] > self.__dictionary_costs[tuple([x, 0])]:
                connection[x] = self.__dictionary_costs[tuple([x, 0])]
                edges[x] = 0
            if connection[x] < minimum:
                minimum = self.__dictionary_costs[tuple([x, 0])]
                best = x
        while sum != 0:
            forest.append(best)
            if edges[best] != -1:
                forest.append(edges[best])
                edges[best] = -1
                connection[best] = 999999
                sum -= 1
                vertices[best] = 0
            minimum = 9999999
            v = best
            for x in self.__dictionary_in[v]:
                if vertices[x] == 1:
                    if connection[x] > self.__dictionary_costs[tuple([x, v])]:
                        connection[x] = self.__dictionary_costs[tuple([x, v])]
                        edges[x] = v
            for i in range(0, self.__number_of_vertices):
                if minimum > connection[i]:
                    minimum = connection[i]
                    best = i
        print(forest)

# [1, 0, 2, 1, 3, 2, 4, 3, 5, 2]
#     def prim_algorithm(self):
#         connection = [9999999 for _ in range(self.__number_of_vertices)]
#         edges = [-1 for _ in range(self.__number_of_vertices)]
#         forest = []
#         vertices = [1 for _ in range(self.__number_of_vertices)]
#         sum = self.__number_of_vertices
#         sum -= vertices[0]
#         vertices[0] = 0
#         minimum = 9999999
#         best = -1
#         for x in self.__dictionary_in[0]:
#             if connection[x] > self.__dictionary_costs[tuple([x, 0])]:
#                 connection[x] = self.__dictionary_costs[tuple([x, 0])]
#                 edges[x] = 0
#             if connection[x] < minimum:
#                 minimum = self.__dictionary_costs[tuple([x, 0])]
#                 best = x
#         while sum != 0:
#             forest.append(best)
#             if edges[best] != -1:
#                 forest.append(edges[best])
#                 edges[best] = -1
#                 connection[best] = 999999
#                 sum -= 1
#                 vertices[best] = 0
#             minimum = 9999999
#             v = best
#             for x in self.__dictionary_in[v]:
#                 if vertices[x] == 1:
#                     if connection[x] > self.__dictionary_costs[tuple([x, v])]:
#                         connection[x] = self.__dictionary_costs[tuple([x, v])]
#                         edges[x] = v
#             for i in range(0, self.__number_of_vertices):
#                 if minimum > connection[i]:
#                     minimum = connection[i]
#                     best = i
#         print(forest)

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

    @property
    def dictionary_costs(self):
        return self.__dictionary_costs

    @dictionary_costs.setter
    def dictionary_costs(self, value):
        self.__dictionary_costs = value


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
        dictionary_costs = {}
        file = open(file_name, 'r')
        line = file.readline().strip()
        number_of_vertices, number_of_edges = line.split(' ')
        line = file.readline().strip()
        quantity = int(number_of_vertices)
        for i in range(0, quantity + 1):
            dictionary_in[i] = []
        while len(line) > 0:
            start_point, end_point, cost = line.split(' ')
            start_point = int(start_point)
            end_point = int(end_point)
            cost = int(cost)
            if start_point not in dictionary_in[end_point]:
                dictionary_in[end_point].append(start_point)
            if end_point not in dictionary_in[start_point]:
                dictionary_in[start_point].append(end_point)
            dictionary_costs[tuple([start_point, end_point])] = cost
            dictionary_costs[tuple([end_point, start_point])] = cost
            line = file.readline().strip()
        file.close()
        A_graph.number_vertices = int(number_of_vertices)
        A_graph.number_edges = int(number_of_edges)
        A_graph.dictionary_in = dictionary_in
        A_graph.dictionary_costs = dictionary_costs
    except Exception:
        raise Exception("There was an error while reading the graph!")
    A_graph.vertices = [x for x in range(0, quantity + 1) if (len(dictionary_in[x]) > 0)]
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
read_graph_from_file(graph, "another_input.txt")
graph.prim_algorithm()
# [1, 0, 2, 1, 8, 2, 5, 2, 6, 5, 7, 6, 3, 2, 4, 3] - more_input.txt - 37 v 37
# [3, 0, 5, 3, 1, 0, 4, 1, 2, 4, 6, 4] - some_input.txt - 39 v 39
# [1, 0, 2, 1, 4, 2, 3, 2, 5, 4] - some_txt_file.txt - 14 v 14
# [1, 0, 2, 0, 5, 2, 4, 5, 3, 4] - another_input.txt - 33 v 33
