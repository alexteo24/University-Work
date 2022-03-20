from BattleShips.BattleShips import BattleShips
from BattleField.BattleField import BattleField, AttackException, PlacementException

import unittest


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.battleships = BattleShips(BattleField(), BattleField())

    def test_instance(self):
        self.assertIsInstance(self.battleships, BattleShips)

    def test_set_first_player_ships(self):
        self.battleships.set_first_player_ships(5, 1, 3, True)
        assert self.battleships.first_player.ocean_data[5][1] == 'S'
        self.battleships.set_second_player_ships(5, 1, 3, True)
        assert self.battleships.second_player.ocean_data[5][1] == 'S'

    def test_place_ships(self):
        self.battleships.check_place_ships(1, 1, 2, False)
        self.battleships.check_place_ships(1, 1, 2, True)
        self.battleships.check_place_ships(1, 1, 2)
        with self.assertRaises(PlacementException):
            self.battleships.check_place_ships(11, 1, 2, True)
        with self.assertRaises(PlacementException):
            self.battleships.check_place_ships(11, 1, 2, False)
        with self.assertRaises(PlacementException):
            self.battleships.check_place_ships(1, 11, 2, True)
        with self.assertRaises(PlacementException):
            self.battleships.check_place_ships(1, 11, 2, False)

    def test_first_player_attack(self):
        self.battleships.set_second_player_ships(5, 1, 3, False)
        self.battleships.set_second_player_ships(7, 1, 3, True)
        self.battleships.first_player_attack(5, 1)
        with self.assertRaises(AttackException):
            self.battleships.first_player_attack(5, 11)

    def test_second_player_attack(self):
        self.battleships.set_first_player_ships(5, 1, 3, False)
        self.battleships.set_first_player_ships(7, 1, 3, True)
        self.battleships.second_player_attack(5, 1)
        with self.assertRaises(AttackException):
            self.battleships.second_player_attack(5, 11)

    def test_anyone_won(self):
        assert self.battleships.check_if_anyone_won() == 2
        self.battleships.set_first_player_ships(5, 1, 2, True)
        assert self.battleships.check_if_anyone_won()
        self.battleships.set_second_player_ships(5, 1, 2, True)
        assert self.battleships.check_if_anyone_won() == -1
        self.battleships.second_player_attack(5, 1)
        self.battleships.second_player_attack(6, 1)
        assert not self.battleships.check_if_anyone_won()
