import unittest
from unittest.mock import patch
from io import StringIO
from pig.Game import Game
from pig.Player import Player
from pig.ComputerPlayer import ComputerPlayer


class TestGame(unittest.TestCase):
    @patch("builtins.input", side_effect=["2", "Test Player 1", "Test Player 2", "n"])
    def test_add_players_human(self, mock_input):
        game = Game()
        game.add_players()

        expected_players = ["Test Player 1", "Test Player 2"]
        actual_players = [player.name for player in game.players]

        self.assertEqual(expected_players, actual_players)

    @patch("builtins.input", side_effect=["1", "2", "Test Player", "n"])
    def test_add_players_computer(self, mock_input):
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

    def test_play_again_yes(self):
        game = Game()
        game.players = [Player("Test Player"), ComputerPlayer("Computer", "easy")]
        game.round = 1
        game.game_over = True

        with patch("builtins.input", return_value="y") as mock_input:
            with patch("sys.exit") as mock_exit:
                game.play_again()

                expected_players = []
                actual_players = game.players
                self.assertEqual(expected_players, actual_players)

                expected_round = 0
                actual_round = game.round
                self.assertEqual(expected_round, actual_round)

                expected_game_over = False
                actual_game_over = game.game_over
                self.assertEqual(expected_game_over, actual_game_over)

                mock_input.assert_called_once_with(
                    "\nDo you want to play again? (y/n) "
                )
                mock_exit.assert_not_called()

    def test_play_again_no(self):
        game = Game()
        game.players = [Player("Test Player"), ComputerPlayer("Computer", "easy")]
        game.round = 1
        game.game_over = True

        with patch("builtins.input", return_value="n") as mock_input:
            with patch("sys.exit") as mock_exit:
                game.play_again()

                expected_players = [
                    Player("Test Player"),
                    ComputerPlayer("Computer", "easy"),
                ]
                actual_players = game.players
                self.assertEqual(expected_players, actual_players)

                expected_round = 1
                actual_round = game.round
                self.assertEqual(expected_round, actual_round)

                expected_game_over = True
                actual_game_over = game.game_over
                self.assertEqual(expected_game_over, actual_game_over)

                mock_input.assert_called_once_with(
                    "\nDo you want to play again? (y/n) "
                )
                mock_exit.assert_called_once()

    @patch("sys.stdout", new_callable=StringIO)
    def test_end_game_winner(self, mock_stdout):
        game = Game()
        player1 = Player("Test Player 1")
        player2 = Player("Test Player 2")
        player1.total_score = 100
        player2.total_score = 99
        game.players = [player1, player2]

        game.end_game()

        expected_output = "\nTest Player 1 wins!"
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_end_game_no_winner(self, mock_stdout):
        game = Game()
        player1 = Player("Test Player 1")
        player2 = Player("Test Player 2")
        player1.total_score = 99
        player2.total_score = 98
        game.players = [player1, player2]

        game.end_game()

        expected_output = "\nNo one wins!"
        self.assertIn(expected_output, mock_stdout.getvalue())


def test_play_round_one_player(self):
    # Test the case when there is only one player in the game
    game = Game()
    game.players = [Player("Player1")]
    game.round = 1
    game.game_over = False
    game.play_round()
    assert game.game_over
    assert game.players[0].total_score >= 0


def test_play_round_cheat(self):
    # Test the case when a player cheats and wins the game
    game = Game()
    game.players = [Player("Player1"), ComputerPlayer("Computer", "easy")]
    game.round = 1
    game.game_over = False
    # Player1 cheats and wins the game
    game.players[0].take_turn = lambda: 0
    game.players[0].total_score = 99
    game.players[0].take_turn = lambda: 100
    game.play_round()
    assert game.game_over
    assert game.players[0].total_score == 100
    assert game.players[1].total_score < 100
