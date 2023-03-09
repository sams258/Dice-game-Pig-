import sys

sys.path.append("pig")
import unittest
from unittest.mock import patch
from pig.player import Player


class TestPlayer(unittest.TestCase):
    
    def test_take_turn_roll(self):
        # Test that the player correctly rolls and holds their turn
        with patch("builtins.input", side_effect=["r", "h"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertLessEqual(score, 20)
        self.assertEqual(player.total_score, score)

    # def test_take_turn_cheat(self):
    #     # Test that the player correctly cheats and wins the game
    #     with patch("builtins.input", side_effect=["c"]):
    #         player = Player("Alice")
    #         score = player.take_turn()
    #     self.assertEqual(player.total_score, 100)

    def test_player_has_name(self):
        # Test that the player has a name attribute
        player = Player("Alice")
        self.assertEqual(player.name, "Alice")

    def test_player_total_score_starts_at_zero(self):
        # Test that the player's total score starts at zero
        player = Player("Alice")
        self.assertEqual(player.total_score, 0)

    def test_player_can_roll_dice(self):
        # Test that the player can roll the dice
        with patch("builtins.input", side_effect=["h"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertLessEqual(score, 6)

    def test_player_can_cheat(self):
        # Test that the player can cheat and win the game
        with patch("builtins.input", side_effect=["c"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertEqual(score, 100)
        self.assertEqual(player.total_score, 100)

    def test_player_can_hold(self):
        # Test that the player can hold their turn
        with patch("builtins.input", side_effect=["h"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertLessEqual(score, 6)


if __name__ == "__main__":
    unittest.main()
