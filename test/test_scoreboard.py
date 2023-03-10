import sys
sys.path.append("pig")
import unittest
from unittest.mock import patch
from pig.scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):
    def setUp(self):
        # This method is called before each test case, so we can use it to reset the scoreboard
        self.scoreboard = Scoreboard()
        self.scoreboard.clear()

    def tearDown(self):
        # This method is called after each test case, so we can use it to reset the scoreboard again
        self.scoreboard.clear()

    def test_add_score(self):
        self.scoreboard.add_score("Alice", 10)
        self.scoreboard.add_score("Bob", 20)
        self.assertEqual(
            self.scoreboard.scores,
            {
                "Alice": {"scores": [10], "games_played": 1},
                "Bob": {"scores": [20], "games_played": 1},
            },
        )

    def test_get_high_scores(self):
        self.scoreboard.add_score("Alice", 10)
        self.scoreboard.add_score("Bob", 20)
        self.scoreboard.add_score("Charlie", 30)
        high_scores = self.scoreboard.get_high_scores()
        self.assertEqual(
            high_scores, [("Charlie", 30, 1), ("Bob", 20, 1), ("Alice", 10, 1)]
        )

    def test_get_player_score(self):
        self.scoreboard.add_score("Alice", 10)
        self.scoreboard.add_score("Bob", 20)
        self.assertEqual(self.scoreboard.get_player_score("Alice"), 10)
        self.assertEqual(self.scoreboard.get_player_score("Bob"), 20)
        self.assertEqual(self.scoreboard.get_player_score("Charlie"), 0)

    def test_change_player_name(self):
        self.scoreboard.add_score("Alice", 10)
        self.scoreboard.change_player_name("Alice", "Alice2")
        self.assertEqual(
            self.scoreboard.scores, {"Alice2": {"scores": [10], "games_played": 1}}
        )

    def test_clear(self):
        self.scoreboard.add_score("Alice", 10)
        self.scoreboard.clear()
        self.assertEqual(self.scoreboard.scores, {})

    def test_add_score_multiple_games(self):
        self.scoreboard.add_score("Alice", 10)
        self.scoreboard.add_score("Alice", 20)
        self.scoreboard.add_score("Bob", 30)
        self.scoreboard.add_score("Bob", 40)
        self.assertEqual(
            self.scoreboard.scores,
            {
                "Alice": {"scores": [10, 20], "games_played": 2},
                "Bob": {"scores": [30, 40], "games_played": 2},
            },
        )

    def test_load_missing_scores_file(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            self.scoreboard.load_scores()
        self.assertEqual(self.scoreboard.scores, {})    

if __name__ == "__main__":
    unittest.main
