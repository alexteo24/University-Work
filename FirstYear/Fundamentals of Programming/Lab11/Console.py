from BattleShips.BattleShips import BattleShips
from BattleField.BattleField import BattleField


class Console:
    def __init__(self):
        self._BattleShips = None

    def first_player_attack_ui(self):
        """
        Function responsible for getting the input for the attack and performing it once the input is valid
        :return: The status of the attack (hit or miss)
        """
        self._BattleShips.second_player.display(self._BattleShips.second_player.masked_ocean)
        good_location = False
        while not good_location:
            try:
                print(self._BattleShips.second_player)
                row_index = int(input("Please enter the row of your attack: "))
                column_index = int(input("Please enter the column of your attack: "))
                attack_status = self._BattleShips.first_player_attack(row_index, column_index)
                good_location = True
            except Exception as ex:
                print(ex)
        return attack_status

    def second_player_attack_ui(self):
        """
        Function responsible for getting the input for the attack and performing it once the input is valid
        :return: The status of the attack (hit or miss)
        """
        good_location = False
        self._BattleShips.first_player.display(self._BattleShips.first_player.masked_ocean)
        while not good_location:
            try:
                print(self._BattleShips.first_player)
                row_index = int(input("Please enter the row of your attack: "))
                column_index = int(input("Please enter the column of your attack: "))
                attack_status = self._BattleShips.second_player_attack(row_index, column_index)
                good_location = True
            except Exception as ex:
                print(ex)
        return attack_status

    def first_player_set_ships_ui(self):
        """
        Function responsible for getting the input for the ship deployments and placing the ships once the input is valid
        :return: -
        """
        self._BattleShips.first_player.display(self._BattleShips.first_player.ocean_data)
        dimension = 2
        number_three_ships = 2
        while dimension <= 5:
            try:
                print(self._BattleShips.first_player)
                print("The player will lay the ship having the dimension " + str(dimension) + " !")
                row_index = int(input("Please enter the row: "))
                column_index = int(input("Please enter the column: "))
                rotate = input(
                    "Please enter if you want your ship to be placed horizontally or vertically (H/V): ").upper()
                if rotate == "V":
                    rotate = True
                else:
                    rotate = False
                if dimension == 3:
                    if number_three_ships == 1:
                        self._BattleShips.set_first_player_ships(row_index, column_index, dimension, rotate)
                        number_three_ships -= 1
                        dimension += 1
                    elif number_three_ships > 0:
                        self._BattleShips.set_first_player_ships(row_index, column_index, dimension, rotate)
                        number_three_ships -= 1
                else:
                    self._BattleShips.set_first_player_ships(row_index, column_index, dimension, rotate)
                    dimension += 1
            except Exception as ex:
                print(ex)

    def second_player_set_ships_ui(self):
        """
        Function responsible for getting the input for the ship deployments and placing the ships once the input is valid
        :return: -
        """
        dimension = 2
        print("The second player will lay his ships!")
        self._BattleShips.second_player.display(self._BattleShips.second_player.ocean_data)
        number_three_ships = 2
        while dimension <= 5:
            try:
                print(self._BattleShips.second_player)
                print("The player will lay the ship having the dimension " + str(dimension) + " !")
                row_index = int(input("Please enter the row: "))
                column_index = int(input("Please enter the column: "))
                rotate = input(
                    "Please enter if you want your ship to be placed horizontally or vertically (H/V): ").upper()
                if rotate == "V":
                    rotate = True
                else:
                    rotate = False
                if dimension == 3:
                    if number_three_ships == 1:
                        self._BattleShips.set_second_player_ships(row_index, column_index, dimension, rotate)
                        number_three_ships -= 1
                        dimension += 1
                    elif number_three_ships > 0:
                        self._BattleShips.set_second_player_ships(row_index, column_index, dimension, rotate)
                        number_three_ships -= 1
                else:
                    self._BattleShips.set_second_player_ships(row_index, column_index, dimension, rotate)
                    dimension += 1
            except Exception as ex:
                print(ex)

    def start_new_game_ui(self, first_player_symbol=None, second_player_symbol=None):
        """
        This function is responsible for starting the game and playing the game (deploying ships -> attacks -> winner)
        :param first_player_symbol: Optional, there was an option for the user to pick the symbol he wanted for the ship
        :param second_player_symbol: Optional, there was an option for the user to pick the symbol he wanted for the ship
        :return: -
        """
        self._BattleShips = BattleShips(BattleField(first_player_symbol), BattleField(second_player_symbol))
        print("The first player will lay his ships!")
        self.first_player_set_ships_ui()
        self.second_player_set_ships_ui()
        who_won = self._BattleShips.check_if_anyone_won()
        turn_to_attack = 1
        while who_won == -1:
            if turn_to_attack % 2 == 1:
                try:
                    print("First player will attack!")
                    attack_status = self.first_player_attack_ui()
                    if attack_status:
                        print("The last attack was a hit!\n")
                    else:
                        print("The last attack was a miss!\n")
                    turn_to_attack += 1
                except Exception as ex:
                    print(ex)
            if turn_to_attack % 2 == 0:
                try:
                    print("Second player will attack!")
                    attack_status = self.second_player_attack_ui()
                    if attack_status:
                        print("The last attack was a hit!\n")
                    else:
                        print("The last attack was a miss!\n")
                    turn_to_attack += 1
                except Exception as ex:
                    print(ex)
            who_won = self._BattleShips.check_if_anyone_won()
        if who_won == 2:
            print("It's a draw!\n")
        elif who_won:
            print("First player won! Congratulations!\n")
        else:
            print("Second player won! Congratulations!\n")

    def start_program(self):
        are_we_done_yet = False
        print("Hello! Welcome to battleships!")
        while not are_we_done_yet:
            try:
                print("What do you want to do?\n1. Start new game\n0. Exit game")
                user_command = input("Please enter your command: ")
                if user_command == '1':
                    self.start_new_game_ui()
                elif user_command == '0':
                    are_we_done_yet = True
                    print("Good bye! ☺")
                else:
                    print("Invalid command!")
            except Exception as ex:
                print(ex)
