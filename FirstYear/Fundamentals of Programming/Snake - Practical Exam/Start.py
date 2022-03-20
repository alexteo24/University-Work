from Board.Board import Board
from Game.Game import Game
from Console import Console

if __name__ == '__main__':
    settings_file = open("settings.txt", 'r+')
    contents = settings_file.read().split()
    dimension = int(contents[0])
    apple_count = int(contents[1])
    the_board = Board(dimension, apple_count)
    the_game = Game(the_board)
    the_console = Console(the_game)
    the_console.start_game()
