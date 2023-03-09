import sys
sys.path.append("pig")
import unittest
from unittest.mock import patch
from io import StringIO
from pig.main import Main
from pig.scoreboard import Scoreboard
from pig.game import Game
from pig.player import Player
from pig.computer_player import ComputerPlayer


class TestMain(unittest.TestCase):
    def test_main_init(self):
        main = Main()
        self.assertIsInstance(main.game, Game)
        self.assertEqual(main.player_name, "")
        self.assertIsInstance(main.scoreboard, Scoreboard)

    def test_display_menu(self):
        main = Main()
        expected_output = (
            "+"
            + "-" * 35
            + "+\n"
            + "|"
            + " " * 13
            + "PIG MENU"
            + " " * 14
            + "|\n"
            + "+"
            + "-" * 35
            + "+\n"
            + "|"
            + " " * 35
            + "|\n"
            + "|"
            + " " * 6
            + "1. Start Game"
            + " " * 16
            + "|\n"
            + "|"
            + " " * 6
            + "2. Show Rules"
            + " " * 16
            + "|\n"
            + "|"
            + " " * 6
            + "3. Show High Scores"
            + " " * 10
            + "|\n"
            + "|"
            + " " * 6
            + "4. Restart Game"
            + " " * 14
            + "|\n"
            + "|"
            + " " * 6
            + "5. Exit Game"
            + " " * 17
            + "|\n"
            + "|"
            + " " * 35
            + "|\n"
            + "+"
            + "-" * 35
            + "+\n"
        )
        with patch("sys.stdout", new=StringIO()) as fake_out:
            main.display_menu()
            self.assertEqual(fake_out.getvalue(), expected_output)

    # def test_start_with_choice_one(self):
    #     with patch("sys.stdin", StringIO("1\n")) as mock_input:
    #         main = Main()
    #         with patch.object(main, "start_game") as mock_start_game:
    #             main.start()
    #             mock_start_game.assert_called_once()

    # @patch("builtins.input", side_effect=[2])
    # def test_start_with_choice_two(self, mock_input):
    #     main = Main()
    #     with patch.object(main, "show_rules") as mock_show_rules:
    #         main.start()
    #         mock_show_rules.assert_called_once()

    # @patch("builtins.input", side_effect=[3])
    # def test_start_with_choice_three(self, mock_input):
    #     main = Main()
    #     with patch.object(main, "show_high_scores") as mock_show_high_scores:
    #         main.start()
    #         mock_show_high_scores.assert_called_once()

    # @patch("builtins.input", side_effect=[4])
    # def test_start_with_choice_four(self, mock_input):
    #     main = Main()
    #     with patch.object(main, "restart_game") as mock_restart_game:
    #         main.start()
    #         mock_restart_game.assert_called_once()

    # @patch("builtins.input", side_effect=[5])
    # def test_start_with_choice_five(self, mock_input):
    #     main = Main()
    #     with patch("sys.exit") as mock_exit:
    #         main.start()
    #         mock_exit.assert_called_once()

    # @patch("builtins.input", side_effect=[0, 6, "invalid", 1])
    # def test_start_with_invalid_choices(self, mock_input):
    #     main = Main()
    #     with patch.object(main, "display_menu") as mock_display_menu:
    #         with patch("sys.stdout", new=StringIO()) as fake_out:
    #             main.start()
    #             mock_display_menu.assert_called()
    #             expected_output = (
    #                 "\nInvalid input. Please enter a number between 1 and 5.\n" * 3
    #             )
    #             self.assertEqual(fake_out.getvalue(), expected_output)

    # @patch("builtins.input", side_effect=[1, 1, "invalid", 1])
    # def test_start_game_with_computer_easy(self, mock_input):
    #     main = Main()
    #     main.player_name = "test_player"
    #     main.start_game()
    #     self.assertEqual(len(main.game.players), 2)
    #     self.assertIsInstance(main.game.players[0], Player)
    #     self.assertEqual(main.game.players[0].name, "test_player")
    #     self.assertIsInstance(main.game.players[1], ComputerPlayer)
    #     self.assertEqual(main.game.players[1].name, "Computer")
    #     self.assertEqual(main.game.players[1].difficulty, "easy")

    # @patch("builtins.input", side_effect=[1, 2, "invalid", 1])
    # def test_start_game_with_computer_hard(self, mock_input):
    #     main = Main()
    #     main.player_name = "test_player"
    #     main.start_game()
    #     self.assertEqual(len(main.game.players), 2)
    #     self.assertIsInstance(main.game.players[0], Player)
    #     self.assertEqual(main.game.players[0].name, "test_player")
    #     self.assertIsInstance(main.game.players[1], ComputerPlayer)
    #     self.assertEqual(main.game.players[1].name, "Computer")
    #     self.assertEqual(main.game.players[1].difficulty, "hard")

    # @patch("builtins.input", side_effect=[2, "test_player", "player_1", "player_2"])
    # def test_start_game_with_human_players(self, mock_input):
    #     main = Main()
    #     main.start_game()
    #     self.assertEqual(len(main.game.players), 2)
    #     self.assertIsInstance(main.game.players[0], Player)
    #     self.assertEqual(main.game.players[0].name, "player_1")
    #     self.assertIsInstance(main.game.players[1], Player)
    #     self.assertEqual(main.game.players[1].name, "player_2")

    # @patch("builtins.input", side_effect=[0, 3, "invalid", 2])
    # def test_start_game_with_invalid_choices(self, mock_input):
    #     main = Main()
    #     with patch("sys.stdout", new=StringIO()) as fake_out:
    #         main.start_game()
    #         expected_output = "\nInvalid input. Please enter 1 or 2.\n" * 2
    #         self.assertEqual(fake_out.getvalue(), expected_output)

    # def test_start_game_with_no_player_name(self):
    #     main = Main()
    #     with patch("builtins.input", side_effect=[1, 1]):
    #         main.start_game()
    #         self.assertEqual(len(main.game.players), 2)
    #         self.assertEqual(main.game.players[0].name, "")
    #         self.assertEqual(main.game.players[1].name, "Computer")

    # def test_show_rules(self):
    #     main = Main()
    #     expected_output = (
    #         "+"
    #         + "-" * 64
    #         + "+\n"
    #         + "|"
    #         + " " * 29
    #         + "RULES"
    #         + " " * 30
    #         + "|\n"
    #         + "+"
    #         + "-" * 64
    #         + "+\n"
    #         + "|"
    #         + " " * 64
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "The objective of the game is to be the first player"
    #         + " " * 6
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "to reach 100 points."
    #         + " " * 37
    #         + "|\n"
    #         + "|"
    #         + " " * 64
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "On each turn, the player rolls a six-sided die. If"
    #         + " " * 7
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "the player rolls a 1, their turn ends and they"
    #         + " " * 11
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "receive no points."
    #         + " " * 39
    #         + "|\n"
    #         + "|"
    #         + " " * 64
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "If the player rolls any other number, they can"
    #         + " " * 11
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "choose to roll again or hold to keep score."
    #         + " " * 14
    #         + "|\n"
    #         + "|"
    #         + " " * 64
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "If a player chooses to hold their turn, "
    #         + " " * 17
    #         + "|\n"
    #         + "|"
    #         + " " * 7
    #         + "total is added to their score."
    #         + " " * 27
    #         + "|\n"
    #         + "|"
    #         + " " * 64
    #         + "|\n"
    #         + "+"
    #         + "-" * 64
    #         + "+\n"
    #     )
    #     with patch("sys.stdout", new=StringIO()) as fake_out:
    #         main.show_rules()
    #         self.assertEqual(fake_out.getvalue(), expected_output)

    # @patch("builtins.input", side_effect=[None])
    # @patch("sys.stdout", new_callable=StringIO)
    # def test_show_high_scores_with_no_scores(self, mock_stdout, mock_input):
    #     main = Main()
    #     main.show_high_scores()
    #     expected_output = "+-----------------------------------+\n|           HIGH SCORES             |\n+-----------------------------------+\n|         No high scores yet.       |\n+----------------------------------+"
    #     self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    # @patch("builtins.input", side_effect=[None])
    # @patch("sys.stdout", new_callable=StringIO)
    # def test_show_high_scores_with_scores(self, mock_stdout, mock_input):
    #     main = Main()
    #     main.scoreboard.add_score("player1", 100)
    #     main.scoreboard.add_score("player2", 200)
    #     main.show_high_scores()
    #     expected_output = "+-----------------------------------+\n|           HIGH SCORES             |\n+-----------------------------------+\n| 1. player2                        200 |\n| 2. player1                        100 |\n+----------------------------------+"
    #     self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_restart_game(self):
        main = Main()
        main.player_name = "test_player"
        main.restart_game()
        self.assertEqual(main.game.players, [])
        self.assertEqual(main.player_name, "")

    # @patch("sys.exit")
    # @patch("sys.stdout", new_callable=StringIO)
    # def test_exit_game(self, mock_stdout, mock_exit):
    #     main = Main()
    #     main.exit_game()
    #     expected_output = "\nThanks for playing!"
    #     self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    #     mock_exit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
