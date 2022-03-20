from texttable import Texttable
import random
import copy


class Board:
    def __init__(self, dimension, apple_count):
        self.__board = [[' ' for i in range(0, dimension)] for j in range(0, dimension)]
        self.__snake = []
        self.__apples = []
        self.__apple_count = apple_count
        self.__dimension = dimension
        self.__apple_number = apple_count

    def place_snake_initial(self):
        """
        This function will place the initial position of the snake to the board and save the location of its segments in
        self.__snake
        :return: -
        """
        tail = [self.__dimension // 2 + 1, self.__dimension // 2]
        body = [self.__dimension // 2, self.__dimension // 2]
        head = [self.__dimension // 2 - 1, self.__dimension // 2]
        self.__snake.append(tail)
        self.__snake.append(body)
        self.__snake.append(head)

    def mark_snake_on_board(self):
        """
        This function will mark the snake segments on the board by marking all the segments of the snake with + in the
        first place and then marking the head (the last element of the list self.__snake) with *
        :return: -
        """
        for a_segment in self.__snake:
            row, column = a_segment
            self.__board[row][column] = '+'
        head_row, head_column = self.__snake[-1]
        self.__board[head_row][head_column] = '*'

    def mark_apples(self):
        """
        This function marks the apples, with ".", stored in self.__apples on the board
        :return: -
        """
        for an_apple in self.__apples:
            row, column = an_apple
            self.__board[row][column] = '.'

    def get_empty_spaces_left(self):
        """
        This function will calculate the number of empty spaces and save their board coordinates
        :return: the number of empty spaces (empty_spaces_count) and the locations of the empty
        spaces(empty_spaces_locations)
        """
        empty_spaces_count = 0
        empty_spaces_locations = []
        for i in range(0, self.__dimension):
            for j in range(0, self.__dimension):
                if self.__board[i][j] == ' ':
                    empty_spaces_count += 1
                    empty_spaces_locations.append([i, j])
        return empty_spaces_count, empty_spaces_locations

    def check_apples_surroundings(self, apple_row, apple_column):
        """
        This functions checks is the location we chose for an apple is good (not on the snake, not close to another
        apple)
        :param apple_row: The row index of the apple
        :param apple_column: The column index of the apple
        :return: True if the location is suitable, False otherwise
        """
        if self.__board[apple_row][apple_column] in ['.', '+', '*']:
            return False
        for apple_location in self.__apples:
            row_index, column_index = apple_location
            if apple_row == row_index and abs(column_index - apple_column) == 1:
                return False
            if apple_column == column_index and abs(row_index - apple_row) == 1:
                return False
        return True

    def place_apples(self):
        """
        This functions is responsible for placing the apples (both initially and afterwards) based on
        self.__apple_number and the available spaces left, and marking the apples on the board
        :return: -
        """
        index = 0
        empty_spaces_count, empty_spaces_locations = self.get_empty_spaces_left()
        sw = 1
        while index < self.__apple_number and len(empty_spaces_locations) != 0 and sw == 1:
            sw = 0
            copy_empty_spaces_locations = copy.deepcopy(empty_spaces_locations)
            available = False
            location = random.choice(copy_empty_spaces_locations)
            apple_row, apple_column = location
            available = self.check_apples_surroundings(apple_row, apple_column)
            while not available:
                copy_empty_spaces_locations.remove(location)
                if len(copy_empty_spaces_locations) != 0:
                    location = random.choice(copy_empty_spaces_locations)
                    apple_row, apple_column = location
                    available = self.check_apples_surroundings(apple_row, apple_column)
                else:
                    break
            if available:
                index += 1
                empty_spaces_locations.remove(location)
                self.__apples.append(location)
                sw = 1
        self.mark_apples()

    def clear_snake_location(self):
        """
        This function clears the location of the snake, so that we won't misrepesent it on the print
        :return: -
        """
        for a_segment in self.__snake:
            row, column = a_segment
            self.__board[row][column] = ' '

    def __str__(self):
        """
        Transforms the matrix responsible for the board into a string(table) to be printed for the player
        :return: The matrix in form of a string(table)
        """
        table = Texttable()
        for row in range(0, self.__dimension):
            table_row = []
            for column in range(0, self.__dimension):
                table_row.append(self.__board[row][column])
            table.add_row(table_row)
        return table.draw()

    def apple_number(self, value):
        """
        Sets the apple number to value
        :param value: The numbers to which we want to set the apple_number
        :return: -
        """
        self.__apple_number = int(value)

    @property
    def board(self):
        return self.__board

    @property
    def snake(self):
        return self.__snake

    @property
    def apples(self):
        return self.__apples

    @property
    def dimension(self):
        return self.__dimension

    def new_snake(self, array):
        """
        Sets the snake positions to a new array (necessary for moving the snake)
        :param array:
        :return:
        """
        self.__snake = array
