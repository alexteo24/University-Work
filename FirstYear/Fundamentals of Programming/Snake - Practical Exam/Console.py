class DirectionException(Exception):
    def __init__(self, message):
        self._message = message


class Console:
    def __init__(self, game):
        self.__game = game

    def print_commands(self):
        """
        Function responsible for printing the commands at the start of the game
        :return: -
        """
        print("Available commands for the game:")
        print("move (n) : n optional parameter, if not given will move 1 position in the last direction it moved or "
              "n positions in that direction")
        print("up : will change the direction in which the snake moves to up and move the snake by 1 positions")
        print("right : will change the direction in which the snake moves to right and move the snake by 1 positions")
        print("down : will change the direction in which the snake moves to down and move the snake by 1 positions")
        print("left : will change the direction in which the snake moves to left and move the snake by 1 positions")

    def start_game(self):
        """
        Function responsible for playing the game and printing "Game over" when the game ends
        :return: -
        """
        self.print_commands()
        self.__game.start_game()
        game_over = False
        print(self.__game.board)
        while not game_over:
            try:
                user_command = input("command>")
                user_command.strip()
                if ' ' in user_command:
                    command, distance = user_command.strip().split(' ', 1)
                    if not distance.isnumeric():
                        raise TypeError("Invalid distance to move! The distance must be an integer greater than 0!")
                    elif distance == 0:
                        raise TypeError("Invalid distance to move! The distance must be an integer greater than 0!")
                else:
                    command = user_command
                    distance = None
                if command == 'move':
                    if distance is None:
                        distance = 1
                    game_over = self.__game.make_move(distance)
                    if not game_over:
                        print(self.__game.board)
                elif command == 'up':
                    if command != self.__game.what_direction:
                        if self.__game.what_direction == 'down':
                            raise DirectionException("The snake cannot do a 180 degrees turn!")
                        else:
                            self.__game.direction(command)
                            game_over = self.__game.make_move(1)
                            if not game_over:
                                print(self.__game.board)
                    else:
                        raise DirectionException("Nothing happened! Perhaps try using move!")
                elif command == 'down':
                    if command != self.__game.what_direction:
                        if self.__game.what_direction == 'up':
                            raise DirectionException("The snake cannot do a 180 degrees turn!")
                        else:
                            self.__game.direction(command)
                            game_over = self.__game.make_move(1)
                            if not game_over:
                                print(self.__game.board)
                    else:
                        raise DirectionException("Nothing happened! Perhaps try using move!")
                elif command == 'right':
                    if command != self.__game.what_direction:
                        if self.__game.what_direction == 'left':
                            raise DirectionException("The snake cannot do a 180 degrees turn!")
                        else:
                            self.__game.direction(command)
                            game_over = self.__game.make_move(1)
                            if not game_over:
                                print(self.__game.board)
                    else:
                        raise DirectionException("Nothing happened! Perhaps try using move!")
                elif command == 'left':
                    if command != self.__game.what_direction:
                        if self.__game.what_direction == 'right':
                            raise DirectionException("The snake cannot do a 180 degrees turn!")
                        else:
                            self.__game.direction(command)
                            game_over = self.__game.make_move(1)
                            if not game_over:
                                print(self.__game.board)
                    else:
                        raise DirectionException("Nothing happened! Perhaps try using move!")
                else:
                    raise DirectionException("Invalid command!")
            except Exception as ex:
                print(ex)
                print(self.__game.board)
            message = self.__game.check_if_game_over(game_over)
            if message == 'Game Over':
                print(message)
                break
