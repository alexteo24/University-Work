from BattleField.BattleField import PlacementException, AttackException


class BattleShips:
    def __init__(self, first_player_ocean, second_player_ocean):
        self._first_player_ocean = first_player_ocean
        self._second_player_ocean = second_player_ocean

    def set_first_player_ships(self, row_index, column_index, dimension, rotate):
        """
        This functions is responsible for the checking of the coordinates to make sure they are valid ( 1<= coord <=10)
        checks if there are no ships nearby and places the ship if possible
        :param row_index: The start row of the ship we want to place
        :param column_index: The start column of the ship we want to place
        :param dimension: The dimension of the ship we want to place
        :param rotate: The rotation of the ship (false = horizontally, true = vertically)
        :return: -
        """
        self.check_place_ships(row_index, column_index, dimension, rotate)
        self._first_player_ocean.check_surroundings(row_index, column_index, dimension, rotate)
        self._first_player_ocean.place_ship(row_index, column_index, dimension, rotate)

    def set_second_player_ships(self, row_index, column_index, dimension, rotate):
        """
        This functions is responsible for the checking of the coordinates to make sure they are valid ( 1<= coord <=10)
        checks if there are no ships nearby and places the ship if possible
        :param row_index: The start row of the ship we want to place
        :param column_index: The start column of the ship we want to place
        :param dimension: The dimension of the ship we want to place
        :param rotate: The rotation of the ship (false = horizontally, true = vertically)
        :return: -
        """
        self.check_place_ships(row_index, column_index, dimension, rotate)
        self._second_player_ocean.check_surroundings(row_index, column_index, dimension, rotate)
        self._second_player_ocean.place_ship(row_index, column_index, dimension, rotate)

    @staticmethod
    def check_place_ships(row_index, column_index, dimension, rotate=None):
        """
        This function is responsible for checking if the desired location is suitable for the current ship placement
        :param row_index: The start row of the ship we want to place
        :param column_index: The start column of the ship we want to place
        :param dimension: The dimension of the ship we want to place
        :param rotate: The rotation of the ship (false = horizontally, true = vertically)
        :return: -  raises an error if the placement is not valid
        """
        if rotate is None:
            rotate = False
        if not rotate:
            if not (1 <= row_index <= 10):
                raise PlacementException("Invalid placement!")
            if not (1 <= column_index <= 11 - dimension):
                raise PlacementException("Invalid placement!")
        else:
            if not (1 <= row_index <= 11 - dimension):
                raise PlacementException("Invalid placement!")
            if not (1 <= column_index <= 10):
                raise PlacementException("Invalid placement!")

    def first_player_attack(self, row_index, column_index):
        """
        This function is responsible for the attack of the first player and raises an error if the attack is outside
        the playing board
        :param row_index: The row of the attack
        :param column_index: The column of the attack
        :return: The status of the attack (hit or miss)
        """
        if not (0 <= row_index <= 10) or not (0 <= column_index <= 10):
            raise AttackException("Invalid location to attack!")
        attack_status = self._second_player_ocean.attack(row_index, column_index)
        if attack_status:
            self._second_player_ocean.remove_ship_location(row_index, column_index)
        return attack_status

    def second_player_attack(self, row_index, column_index):
        """
        This function is responsible for the attack of the second player and raises an error if the attack is outside
        the playing board
        :param row_index: The row of the attack
        :param column_index: The column of the attack
        :return: The status of the attack (hit or miss)
        """
        if not (0 <= row_index <= 10) or not (0 <= column_index <= 10):
            raise AttackException("Invalid location to attack!")
        attack_status = self._first_player_ocean.attack(row_index, column_index)
        if attack_status:
            self._first_player_ocean.remove_ship_location(row_index, column_index)
        return attack_status

    def check_if_anyone_won(self):
        """
        This function is responsible for checking which player won
        :return: 2 if it is a draw, False if player one has lost, True if player one has won and - 1 if the game
        hasn't ended yet
        """
        if len(self._first_player_ocean.locations) == 0 and len(self._second_player_ocean.locations) == 0:
            return 2
        if len(self._first_player_ocean.locations) == 0:
            return False
        if len(self._second_player_ocean.locations) == 0:
            return True
        return -1

    @property
    def first_player(self):
        return self._first_player_ocean

    @property
    def second_player(self):
        return self._second_player_ocean
