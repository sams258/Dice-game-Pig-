import sys

sys.path.append("pig")
import unittest
from unittest.mock import patch
from pig.player import Player


class TestPlayer(unittest.TestCase):
    def test_take_turn_hold(self):
        # Test that the player correctly holds their turn
        with patch("builtins.input", side_effect=["h"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertEqual(score, 0)
        self.assertEqual(player.total_score, 0)

    def test_take_turn_roll(self):
        # Test that the player correctly rolls and holds their turn
        with patch("builtins.input", side_effect=["r", "h"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 20)
        self.assertEqual(player.total_score, score)

    def test_take_turn_cheat(self):
        # Test that the player can cheat and win the game
        with patch("builtins.input", side_effect=["c"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertEqual(score, 100)
        self.assertEqual(player.total_score, 100)

    def test_take_turn_invalid_input(self):
        # Test that the player is prompted to enter valid input if they enter an invalid choice
        with patch("builtins.input", side_effect=["x", "h"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertEqual(score, 0)
        self.assertEqual(player.total_score, 0)

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
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 20)

    def test_player_can_hold_turn(self):
        # Test that the player can hold their turn
        with patch("builtins.input", side_effect=["h"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertEqual(score, 0)
        self.assertEqual(player.total_score, 0)

    def test_player_can_cheat(self):
        # Test that the player can cheat and win the game
        with patch("builtins.input", side_effect=["c"]):
            player = Player("Alice")
            score = player.take_turn()
        self.assertEqual(score, 100)
        self.assertEqual(player.total_score, 100)

    def test_player_can_take_multiple_turns(self):
        # Test that the player can take multiple turns and accumulate their total score
        with patch("builtins.input", side_effect=["r", "h", "r", "h"]):
            player = Player("Alice")
            score1 = player.take_turn()
            score2 = player.take_turn()
        self.assertGreater(score1, 0)
        self.assertLessEqual(score1, 20)
        self.assertGreater(score2, 0)
        self.assertLessEqual(score2, 20)
        self.assertEqual(player.total_score, score1 + score2)


if __name__ == "__main__":
    unittest.main()
