import sys
import unittest
sys.path.append("pig")
from unittest.mock import patch
from pig.computer_player import ComputerPlayer
from io import StringIO


class TestComputerPlayer(unittest.TestCase):
    def test_take_turn_easy(self):
        # Test that an easy computer player correctly holds their turn
        player = ComputerPlayer("Bob", "easy")
        player.total_score = 700
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertLessEqual(score, 20)
        self.assertGreaterEqual(player.total_score, 700)

    def test_take_turn_hard(self):
        # Test that a hard computer player correctly holds their turn
        player = ComputerPlayer("Bob", "hard")
        player.total_score = 700
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertLessEqual(score, 20)
        self.assertGreaterEqual(player.total_score, 700)

    def test_take_turn_cheat(self):
        # Test that a hard computer player correctly holds their turn
        player = ComputerPlayer("Bob", "hard")
        player.total_score = 700
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertIsNotNone(score, 0)
        self.assertLessEqual(score, 700)
        self.assertGreaterEqual(player.total_score, 700)

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
        self.assertLessEqual(score, 20)


    def test_player_can_take_multiple_turns(self):
        # Test that the computer player can take multiple turns
        player = ComputerPlayer("Bob", "easy")
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertLessEqual(score, 20)
        self.assertGreaterEqual(player.total_score, 0)

    def test_player_can_win(self):
        # Test that the computer player can win
        player = ComputerPlayer("Bob", "easy")
        player.total_score = 100
        with patch("builtins.input", side_effect=["h"]):
            score = player.take_turn()
        self.assertGreaterEqual(player.total_score, 100)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["yes"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_take_turn_loses_turn(self, mock_stdout, mock_input, mock_randint):
        player = ComputerPlayer("Test", "easy")
        expected_output = "Test rolled a [1]\nTest lost their turn!\n"
        self.assertEqual(player.take_turn(), 0)
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
