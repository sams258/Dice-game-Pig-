import sys
import unittest
sys.path.append("pig")
from unittest.mock import patch
from pig.computer_player import ComputerPlayer


class TestComputerPlayer(unittest.TestCase):
    def test_take_turn_easy(self):
        # Test that an easy computer player correctly holds their turn
        player = ComputerPlayer("Bob", "easy")
        player.total_score = 80
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 20)
        self.assertGreaterEqual(player.total_score, 80)

    def test_take_turn_hard(self):
        # Test that a hard computer player correctly holds their turn
        player = ComputerPlayer("Bob", "hard")
        player.total_score = 700
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 20)
        self.assertGreaterEqual(player.total_score, 700)

    def test_take_turn_cheat(self):
        # Test that a computer player can cheat and win the game
        player = ComputerPlayer("Bob", "cheat")
        with patch("builtins.input", side_effect=["c"]):
            score = player.take_turn()
        self.assertEqual(score, 100)
        self.assertEqual(player.total_score, 100)

    def test_player_has_name(self):
        # Test that the computer player has a name attribute
        player = ComputerPlayer("Bob", "easy")
        self.assertEqual(player.name, "Bob")

    def test_player_total_score_starts_at_zero(self):
        # Test that the computer player's total score starts at zero
        player = ComputerPlayer("Bob", "easy")
        self.assertEqual(player.total_score, 0)

    def test_player_can_roll_dice(self):
        # Test that the computer player can roll the dice
        player = ComputerPlayer("Bob", "easy")
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 20)

    def test_player_can_hold_turn(self):
        # Test that the computer player can hold their turn
        player = ComputerPlayer("Bob", "easy")
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertEqual(score, 0)
        self.assertEqual(player.total_score, 0)

    def test_player_can_take_multiple_turns(self):
        # Test that the computer player can take multiple turns and accumulate their total score
        player = ComputerPlayer("Bob", "easy")
        with patch("builtins.input", side_effect=["r", "h", "r", "h"]):
            score1 = player.take_turn()
            score2 = player.take_turn()
        self.assertGreater(score1, 0)
        self.assertLessEqual(score1, 20)
        self.assertGreater(score2, 0)
        self.assertLessEqual(score2, 20)
        self.assertEqual(player.total_score, score1 + score2)


if __name__ == "__main__":
    unittest.main()
