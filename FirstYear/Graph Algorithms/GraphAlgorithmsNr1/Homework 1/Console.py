from Graph import read_graph_from_file, Graph, write_graph_to_file


def print_menu():
    print("Available commands!\n"  # Done
          "1. Add new empty graph\n"  # Done
          "2. Add new graph with input from a file\n"  # Done
          "3. Add random generated graph\n"  # Done
          "4. Add a vertex to the current graph\n"  # Done
          "5. Add an edge to the current graph\n"  # Done
          "6. Modify the cost of an edge of the current graph\n"  # Done
          "7. Remove a vertex from the current graph\n"  # Done
          "8. Remove an edge from the current graph\n"  # Done
          "9. Get the in degree of a vertex of the current graph\n"  # Done
          "10. Get the out degree of a vertex of the current graph\n"  # Done
          "11. Check if there is an edge between two given vertices\n"  # Done
          "12. Parse the vertices of the current graph\n"  # Done
          "13. Parse the inbound vertices of a vertex\n"  # Done
          "14. Parse the outbound vertices of a vertex\n"  # Done
          "15. Copy current graph\n"  # Done
          "16. Write current graph to a file\n"  # Done
          "17. Switch graph\n"  # Done
          "18. Display current graph\n"  # Done
          "19. Small test thing\n"  # Done
          "0. Exit")


def test_small_thingie():
    graph = Graph()
    read_graph_from_file(graph, "small_input.txt")
    write_graph_to_file(graph, "output.txt")
    print(graph.check_if_edge(2, 7))  # should be true
    new_graph = graph.make_copy()
    print(new_graph.check_if_edge(2, 7))  # should be true
    new_graph.remove_vertex(2)
    print(new_graph.check_if_edge(2, 7))  # should be false
    print(graph.check_if_edge(2, 7))  # should be true
    print("stop")


class Console:

    def __init__(self, controller):
        self.__controller = controller

    def add_new_empty_graph_UI(self):
        self.__controller.add_empty_graph()

    def add_new_default_graph_UI(self):
        filename = input("Please enter the filename! Either: small_input.txt graph1k.txt, graph10k.txt, graph100k.txt, "
                         "graph1m.txt although bigger graphs will take a while to load!\n")
        while filename not in ["small_input.txt", "graph1k.txt", "graph10k.txt", "graph100k.txt", "graph1m.txt"]:
            filename = input(
                "Please enter the filename! Either: small_input.txt graph1k.txt, graph10k.txt, graph100k.txt, "
                "graph1m.txt although bigger graphs will take a while to load!\n")
        self.__controller.add_default_graph(filename)

    def add_random_generated_graph_UI(self):
        number_vertices = input("Please enter the number of vertices for the graph you want to generate:")
        number_edges = input("Please enter the number of edges for the graph you want to generate:")
        while not number_edges.isdigit() or not number_vertices.isdigit():
            number_vertices = input("Please enter the number of vertices for the graph you want to generate:")
            number_edges = input("Please enter the number of edges for the graph you want to generate:")
        number_edges = int(number_edges)
        number_vertices = int(number_vertices)
        self.__controller.add_random_generated_graph(number_vertices, number_edges)

    def add_vertex_to_current_graph_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            vertex = input("Please enter the vertex you want to add:")
            while not vertex.isdigit() or (len(vertex) > 1 and vertex[0] == '0'):
                vertex = input("Please enter the vertex you want to add:")
            vertex = int(vertex)
            self.__controller.add_vertex_current_graph(vertex)

    def add_edge_to_current_graph_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            start_point = input("Please enter the first vertex:")
            end_point = input("Please enter the second vertex:")
            cost = input("Please enter the cost:")
            while not start_point.isdigit() \
                    or not end_point.isdigit() or not \
                    (cost.isdigit() or (cost[1:].isdigit()) and cost[0] == '-') or \
                    (len(start_point) > 1 and start_point[0] == '0') or (len(end_point) > 1 and end_point[0] == '0'):
                start_point = input("Please enter the first vertex:")
                end_point = input("Please enter the second vertex:")
                cost = input("Please enter the cost:")
            start_point = int(start_point)
            end_point = int(end_point)
            cost = int(cost)
            self.__controller.add_edge_current_graph(start_point, end_point, cost)

    def modify_cost_of_an_edge_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            start_point = input("Please enter the first vertex:")
            end_point = input("Please enter the second vertex:")
            cost = input("Please enter the cost:")
            while not start_point.isdigit() or not end_point.isdigit() or (cost[0] == '-' and not cost[1:].isdigit()):
                start_point = input("Please enter the first vertex:")
                end_point = input("Please enter the second vertex:")
                cost = input("Please enter the cost:")
            start_point = int(start_point)
            end_point = int(end_point)
            cost = int(cost)
            self.__controller.modify_cost_edge_current([start_point, end_point], cost)

    def remove_a_vertex_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            vertex = input("Please enter the vertex you want to remove:")
            while not vertex.isdigit():
                vertex = input("Please enter the vertex you want to remove:")
            vertex = int(vertex)
            self.__controller.remove_vertex_current_graph(vertex)

    def remove_an_edge_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            start_point = input("Please enter the first vertex:")
            end_point = input("Please enter the second vertex:")
            while not start_point.isdigit() or not end_point.isdigit() or \
                    (len(start_point) > 1 and start_point[0] == '0') or (len(end_point) > 1 and end_point[0] == '0'):
                start_point = input("Please enter the first vertex:")
                end_point = input("Please enter the second vertex:")
            start_point = int(start_point)
            end_point = int(end_point)
            self.__controller.remove_edge_current_graph(start_point, end_point)

    def get_in_degree_of_vertex_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            vertex = input("Please enter the vertex:")
            while not vertex.isdigit():
                vertex = input("Please enter the vertex:")
            vertex = int(vertex)
            print("The in degree of the vertex " + str(vertex) + " is " +
                  str(self.__controller.get_degree_in_vertex_current(vertex)))

    def get_out_degree_of_vertex_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            vertex = input("Please enter the vertex")
            while not vertex.isdigit():
                vertex = input("Please enter the vertex:")
            vertex = int(vertex)
            print("The out degree of the vertex " + str(vertex) + " is " +
                  str(self.__controller.get_degree_out_vertex_current(vertex)))

    def check_if_edge_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            start_point = input("Please enter the first vertex:")
            end_point = input("Please enter the second vertex:")
            while not start_point.isdigit() or not end_point.isdigit() or\
                    (len(start_point) > 1 and start_point[0] == '0') or (len(end_point) > 1 and end_point[0] == '0'):
                start_point = input("Please enter the first vertex:")
                end_point = input("Please enter the second vertex:")
            start_point = int(start_point)
            end_point = int(end_point)
            if self.__controller.check_for_edge_current(start_point, end_point):
                print("There is an edge going from " + str(start_point) + " to " + str(end_point))
            else:
                print("There is no edge going from " + str(start_point) + " to " + str(end_point))

    def parse_vertices_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There is no graph to be parsed!")
        else:
            it = self.__controller.parseX_current()
            line = ""
            while it.valid():
                line += str(next(it)) + " "
            print(line)

    def parseNIn_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There is no graph to be parsed!")
        else:
            vertex = input("Please enter a vertex:")
            while not vertex.isdigit() or int(vertex) not in self.__controller.verticess:
                vertex = input("Please enter a vertex:")
            vertex = int(vertex)
            it = self.__controller.parseNIn_current(vertex)
            line = ""
            while it.valid():
                line += str(next(it)) + " "
            print(line)

    def parseNOut_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There is no graph to be parsed!")
        else:
            vertex = input("Please enter a vertex:")
            while not vertex.isdigit() or int(vertex) not in self.__controller.verticess:
                vertex = input("Please enter a vertex:")
            vertex = int(vertex)
            it = self.__controller.parseNOut_current(vertex)
            line = ""
            while it.valid():
                line += str(next(it)) + " "
            print(line)

    def copy_current_graph_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There is no graph to copy!")
        else:
            self.__controller.copy_current_graph()

    def write_current_graph_to_file_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There is no graph to write!")
        else:
            self.__controller.write_current_graph_to_file()

    def switch_graph_UI(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs to switch to!")
        else:
            print("You are on the graph number: " + str(self.__controller.current))
            print("Available graphs: 0 - " + str(len(self.__controller.graphs) - 1))
            graph_number = input("Please enter the graph number you want to switch to: ")
            while not graph_number.isdigit() or not (0 <= int(graph_number) < len(self.__controller.graphs)):
                graph_number = input("Please enter the graph number you want to switch to: ")
            self.__controller.current = int(graph_number)

    def display_current_graph(self):
        if (len(self.__controller.graphs)) == 0:
            print("There are no graphs!")
        else:
            print("Currently you are working on graph number " + str(self.__controller.current))

    def start_program(self):
        print("Welcome!\n")
        are_we_done_yet = False
        command_dict = {"1": self.add_new_empty_graph_UI, "2": self.add_new_default_graph_UI,
                        "3": self.add_random_generated_graph_UI, "4": self.add_vertex_to_current_graph_UI,
                        "5": self.add_edge_to_current_graph_UI, "6": self.modify_cost_of_an_edge_UI,
                        "7": self.remove_a_vertex_UI, "8": self.remove_an_edge_UI, "9": self.get_in_degree_of_vertex_UI,
                        "10": self.get_out_degree_of_vertex_UI, "11": self.check_if_edge_UI,
                        "12": self.parse_vertices_UI, "13": self.parseNIn_UI, "14": self.parseNOut_UI,
                        "15": self.copy_current_graph_UI, "16": self.write_current_graph_to_file_UI,
                        "17": self.switch_graph_UI, "18": self.display_current_graph}
        while not are_we_done_yet:
            try:
                print_menu()
                user_command = input("Please enter your command: ")
                if user_command == "0":
                    are_we_done_yet = True
                    print("Goodbye!\n")
                elif user_command == "19":
                    test_small_thingie()
                elif user_command not in command_dict:
                    raise Exception("Invalid command!")
                else:
                    command_dict[user_command]()
            except Exception as ex:
                print(ex)
