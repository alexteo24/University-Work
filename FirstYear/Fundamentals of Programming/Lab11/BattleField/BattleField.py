from texttable import Texttable
import copy


class PlacementException(Exception):
    def __init__(self, message):
        self._message = message


class AttackException(Exception):
    def __init__(self, message):
        self._message = message


class BattleField:
    def __init__(self, symbol=None):
        self._rows = 12
        self._columns = 12
        self._ocean_data = [['■' for line in range(self._rows)] for column in range(self._columns)]
        self._masked_ocean = [['■' for line in range(self._rows)] for column in range(self._columns)]
        self._display_ocean = []
        if symbol is None:
            self._ship_symbol = 'S'
        else:
            self._ship_symbol = symbol
        self._ships_locations = []
        self._copy_ships_locations = []
        self._guy_ships_locations = []

    def check_surroundings(self, row_index, column_index, dimension, rotate=False):
        """
        This function checks if there is another ship in proximity (less < 1 tile in every direction) to the ship
         we want to place and raises and error if that is the case
        :param row_index: The start row of the ship we want to place
        :param column_index: The start column of the ship we want to place
        :param dimension: The dimension of the ship we want to place
        :param rotate: Determines if the ship is placed horizontally or vertically (false = h, true = v)
        :return: -  raises an error
        """
        row_surroundings = [-1, -1, 0, 1, 1, 1, 0, -1]
        column_surroundings = [0, 1, 1, 1, 0, -1, -1, -1]
        if not rotate:
            for index in range(column_index, column_index + dimension):
                for second_index in range(0, 8):
                    surrounding_row = row_index + row_surroundings[second_index]
                    surrounding_column = column_index + column_surroundings[second_index]
                    if self._ocean_data[surrounding_row][surrounding_column] == self._ship_symbol:
                        raise PlacementException("The ship is too close to another one!")
        else:
            for index in range(row_index, row_index + dimension):
                for second_index in range(0, 8):
                    surrounding_row = row_index + row_surroundings[second_index]
                    surrounding_column = column_index + column_surroundings[second_index]
                    if self._ocean_data[surrounding_row][surrounding_column] == self._ship_symbol:
                        raise PlacementException("The ship is too close to another one!")

    def place_ship(self, row_index, column_index, dimension, rotate):
        """
        This function places a new ship in the ocean and adds its locations in the form of [row, column] to a
         list of locations
        :param row_index: The start row of the ship we want to place
        :param column_index: The start column of the ship we want to place
        :param dimension: The dimension of the ship we want to place
        :param rotate: Determines if the ship is placed horizontally or vertically (false = h, true = v)
        :return: -
        """
        ship_location = []
        copy_ship_location = []
        guy_ships_location = []
        if not rotate:
            for index in range(column_index, column_index + dimension):
                self._ocean_data[row_index][index] = self._ship_symbol
                copy_ship_location.append([row_index, index])
                ship_location.append([row_index, index])
                guy_ships_location.append([row_index, index])

        else:
            for index in range(row_index, row_index + dimension):
                self._ocean_data[index][column_index] = self._ship_symbol
                copy_ship_location.append([row_index, index])
                ship_location.append([index, column_index])
                guy_ships_location.append([row_index, index])
        self._ships_locations.append(ship_location)
        self._copy_ships_locations.append(copy_ship_location)
        self._guy_ships_locations.append(guy_ships_location)

    def remove_ship_location(self, row_index, column_index):
        """
        This functions removes the [row, index] pair if it is a part of a ship and it was not hit yet, or the hole ship
        if the hit would be the last part of the ship
        :param row_index: The row of the attack
        :param column_index: The index of the attack
        :return: -
        """
        copy_index = -1
        index = 0
        while index < len(self._ships_locations):
            locations = self._ships_locations[index]
            second_index = 0
            while second_index < len(locations):
                row_column = locations[second_index]
                location_row = row_column[0]
                location_column = row_column[1]
                if location_row == row_index and location_column == column_index:
                    copy_index = index
                    locations.remove(row_column)
                else:
                    second_index += 1
                if len(locations) == 0:
                    self._ships_locations.remove(locations)
                    for location in self._copy_ships_locations[copy_index]:
                        location_row = location[0]
                        location_column = location[1]
                        self.mark_surroundings(location_row, location_column)
                    location = self._copy_ships_locations[copy_index]
                    self._copy_ships_locations.pop(copy_index)
                    break
                else:
                    index += 1

    def mark_surroundings(self, row_index, column_index):
        """
        This function is marking the surroundings of a sunken ship so that the player cannot attack there anymore since
        there cannot be two ships next to eachother
        :param row_index: The row of the attack
        :param column_index: The column of the attack
        :return: -
        """
        row_surroundings = [-1, -1, 0, 1, 1, 1, 0, -1]
        column_surroundings = [0, 1, 1, 1, 0, -1, -1, -1]
        for second_index in range(0, 8):
            surrounding_row = row_index + row_surroundings[second_index]
            surrounding_column = column_index + column_surroundings[second_index]
            if self._ocean_data[surrounding_row][surrounding_column] == '■':
                self._masked_ocean[surrounding_row][surrounding_column] = 'O'

    def attack(self, row_index, column_index):
        """
        This functions performs the attack action
        :param row_index: The row of the attack
        :param column_index: The column of the attack
        :return: The status of the attack (hit or miss)
        """
        if self._masked_ocean[row_index][column_index] == 'O' or self._masked_ocean[row_index][column_index] == 'X':
            raise AttackException("This location has already been hit!")
        if self._ocean_data[row_index][column_index] != self._ship_symbol:
            self._masked_ocean[row_index][column_index] = 'O'
            return False
        else:
            self._masked_ocean[row_index][column_index] = 'X'
            return True

    def __str__(self):
        """
        Transforms the matrix responsible for the board into a string(table) to be printed for the player
        :return: The matrix in form of a string(table)
        """
        table = Texttable()
        header = [' ', ' ']
        for index in range(1, self._columns - 1):
            header.append(index)
        table.header(header)
        table.add_row([' ' for index in range(self._columns)])
        for row in range(1, self._rows - 1):
            table_row = [' ']
            for element in self._display_ocean[row][1:-1]:
                table_row.append(element)
            table.add_row([str(row)] + table_row)
        return table.draw()

    def display(self, ocean):
        """
        This functions sets the board(matrix) ocean to be the one to be turned into a string for the print
        :param ocean: The ocean we want to turn into a string for the print
        :return: -
        """
        self._display_ocean = ocean.copy()

    @property
    def locations(self):
        return self._ships_locations

    @property
    def ocean_data(self):
        return self._ocean_data

    @property
    def ship_symbol(self):
        return self._ship_symbol

    @property
    def masked_ocean(self):
        return self._masked_ocean

    @property
    def copy_ships_locations(self):
        return self._copy_ships_locations

    @property
    def ships_locations(self):
        return self._ships_locations

    @property
    def gui_ships_locations(self):
        return self._guy_ships_locations
