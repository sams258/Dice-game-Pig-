import sys
from unittest.mock import Mock
sys.path.append("pig")
import unittest
from unittest.mock import patch
from io import StringIO
from pig.game import Game
from pig.player import Player
from pig.computer_player import ComputerPlayer


import unittest.mock


class TestGame(unittest.TestCase):
    
    def test_init_players(self):
        game = Game()
        self.assertEqual(len(game.players), 0)
    
    def test_init_round(self):
        game = Game()
        self.assertEqual(game.round, 0)

    def test_init_game_over(self):
        game = Game()
        self.assertFalse(game.game_over)

    def test_add_players_human(self):
        with patch("builtins.input", side_effect=["2", "Test Player 1", "Test Player 2", "n"]), \
             patch('pig.game.Print.print_sleep'):
            game = Game()
            game.add_players()

            expected_players = ["Test Player 1", "Test Player 2"]
            actual_players = [player.name for player in game.players]

            self.assertEqual(expected_players, actual_players)

    def test_add_players_computer(self):
        with patch("builtins.input", side_effect=["1", "2", "Test Player", "n"]), \
             patch('pig.game.Print.print_sleep'):
            game = Game()
            game.add_players()

            expected_players = ["Test Player", "Computer"]
            actual_players = [player.name for player in game.players]

            self.assertEqual(expected_players, actual_players)

    def test_check_win_condition_true(self):
        game = Game()
        player = Player("Test Player")
        player.total_score = 100
        self.assertTrue(game.check_win_condition(player))

    def test_check_win_condition_false(self):
        game = Game()
        player = Player("Test Player")
        player.total_score = 50
        self.assertFalse(game.check_win_condition(player))

    def test_start_calls_end_game_when_game_over(self):
        # Arrange
        game = Game()
        game.game_over = True
        game.end_game = Mock()

        # Act
        game.start()

        # Assert
        game.end_game.assert_called_once()



