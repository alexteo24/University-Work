class Game:
    def __init__(self, board):
        self.__board = board
        self.__direction = 'up'

    def start_game(self):
        """
        This function is responsible for starting the game by placing both the snake and apples and marking them
        :return: -
        """
        self.__board.place_snake_initial()
        self.__board.mark_snake_on_board()
        self.__board.place_apples()

    def make_move(self, distance=1):
        """
        This function is responsible for moving the snake on the board in the direction stored in self.__direction and
        by a distance stored in "distance"
        :param distance: The distance we want to move the snake
        :return: The status of the game. If the snake hits itself or tries to go outside the board, it will return True
         = Game over otherwise returns False
        """
        new_apples_needed = 0
        game_over = False
        distance = int(distance)
        for i in range(0, distance):
            self.__board.clear_snake_location()
            snake_coords = self.__board.snake
            head_row, head_column = snake_coords[-1]
            # Head movements
            # if up, row index -1
            # if down, row index + 1
            # if left, column index - 1
            # if right column index + 1
            if self.__direction == 'up':
                new_head_location = [head_row - 1, head_column]
            elif self.__direction == 'right':
                new_head_location = [head_row, head_column + 1]
            elif self.__direction == 'down':
                new_head_location = [head_row + 1, head_column]
            elif self.__direction == 'left':
                new_head_location = [head_row, head_column - 1]
            row_new_head_location, column_new_head_location = new_head_location
            if not (0 <= row_new_head_location < self.__board.dimension) \
                    or not (0 <= column_new_head_location < self.__board.dimension):
                game_over = True
            elif new_head_location in self.__board.apples:
                new_apples_needed += 1
                self.apple_hit(new_head_location)
            elif new_head_location in self.__board.snake[1:]:
                game_over = True
            else:
                self.nothing_hit(new_head_location)
        self.__board.mark_snake_on_board()
        self.__board.apple_number(new_apples_needed)
        self.__board.place_apples()
        return game_over

    def apple_hit(self, new_head_location):
        """
        This function handles the case in which the snake goes to an apple
        :param new_head_location: The location of the snake in form of [row, column]
        :return: -
        """
        self.__board.apples.remove(new_head_location)
        self.__board.snake.append(new_head_location)

    def nothing_hit(self, new_head_location):
        """
        This function handles the case in which the snake doesn't hit anything (itself, apple or out of board)
        :param new_head_location: The location of the snake in form of [row, column]
        :return: -
        """
        self.__board.snake.append(new_head_location)
        self.__board.new_snake(self.__board.snake[1:])

    def check_if_game_over(self, game_status):
        """
        The function is responsible for checking if the game has ended either by hitting itself or out of board or the
        snake is occupying all the cells in the board
        :param game_status: The state of the game (if it it ended = True if not = False)
        :return: The message game over in case game_status is True = end of game
        """
        if game_status:
            return "Game Over"
        spaces_left, something_not_relevant = self.__board.get_empty_spaces_left()
        if spaces_left == 0:
            game_status = not game_status
            return "Game Over"

    def direction(self, direction):
        self.__direction = direction

    @property
    def board(self):
        return self.__board

    @property
    def what_direction(self):
        return self.__direction
