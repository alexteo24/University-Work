from BattleField.BattleField import BattleField, PlacementException, AttackException
import unittest


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.battlefield1 = BattleField()
        self.battlefield = BattleField("K")

    def test_instance(self):
        self.assertIsInstance(self.battlefield1, BattleField)
        self.assertIsInstance(self.battlefield, BattleField)

    def test_check_surroundings(self):
        self.battlefield.check_surroundings(1, 2, 3, False)
        self.battlefield.check_surroundings(1, 2, 3, True)
        self.battlefield.ocean_data[2][3] = self.battlefield.ship_symbol
        with self.assertRaises(PlacementException):
            self.battlefield.check_surroundings(1, 2, 3, False)
        with self.assertRaises(PlacementException):
            self.battlefield.check_surroundings(1, 2, 3, True)

    def test_place_ship(self):
        self.battlefield.place_ship(5, 6, 2, False)
        self.battlefield.place_ship(5, 1, 3, True)

    def test_remove_ship_location(self):
        self.battlefield.place_ship(5, 1, 2, True)
        self.battlefield.remove_ship_location(5, 1)
        self.battlefield.remove_ship_location(6, 1)

    def test_attack(self):
        self.battlefield.place_ship(5, 1, 2, True)
        self.battlefield.attack(5, 1)
        with self.assertRaises(AttackException):
            self.battlefield.attack(5, 1)
        self.battlefield.attack(10, 1)

    def test_str(self):
        self.battlefield.place_ship(5, 6, 2, False)
        self.battlefield.place_ship(5, 1, 3, True)
        self.battlefield.display(self.battlefield.masked_ocean)
        string = str(self.battlefield)

    def test_properties(self):
        self.battlefield.place_ship(5, 6, 2, False)
        self.battlefield.place_ship(5, 1, 3, True)
        test_locations = self.battlefield.locations
        test_ocean_data = self.battlefield.ocean_data
        test_symbol = self.battlefield.ship_symbol
        test_masked_ocean = self.battlefield.masked_ocean
        test_copy_ships_location = self.battlefield.copy_ships_locations
        test_gui_ships_location = self.battlefield.gui_ships_locations
        test_ships_location = self.battlefield.ships_locations
