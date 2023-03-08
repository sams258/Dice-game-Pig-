import unittest
from pig.Scoreboard import Scoreboard


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

    def test_load_scores(self):
        # This test case verifies that we can load scores from a file and that they are stored correctly
        # We'll need to use the add_score method to make sure the scores are stored correctly
        with open("scores.json", "w") as f:
            f.write(
                '{"Alice": {"scores": [10, 20], "games_played": 2}, "Bob": {"scores": [30], "games_played": 1}}'
            )
        self.scoreboard.load_scores()
        self.scoreboard.add_score("Alice", 30)
        self.assertEqual(
            self.scoreboard.scores,
            {
                "Alice": {"scores": [10, 20, 30], "games_played": 3},
                "Bob": {"scores": [30], "games_played": 1},
            },
        )

    def test_save_scores(self):
        self.scoreboard.add_score("Alice", 10)
        self.scoreboard.add_score("Bob", 20)
        self.scoreboard.add_score("Charlie", 30)
        self.scoreboard.save_scores()
        with open("scores.json", "r") as f:
            self.assertEqual(
                f.read(),
                '{"Alice": {"scores": [10], "games_played": 1}, "Bob": {"scores": [20], "games_played": 1}, "Charlie": {"scores": [30], "games_played": 1}}',
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

    # def test_get_player_stats(self):
    #     self.scoreboard.add_score("Alice", 10)
    #     self.scoreboard.add_score("Alice", 20)
    #     self.scoreboard.add_score("Bob", 30)
    #     self.scoreboard.add_score("Bob", 40)
    #     self.assertEqual(
    #         self.scoreboard.get_player_score("Alice"),
    #         {
    #             "name": "Alice",
    #             "scores": [10, 20],
    #             "games_played": 2,
    #             "average_score": 15,
    #         },
    #     )
    #     self.assertEqual(
    #         self.scoreboard.get_player_score("Bob"),
    #         {"name": "Bob", "scores": [30, 40], "games_played": 2, "average_score": 35},
    #     )
    #     self.assertEqual(
    #         self.scoreboard.get_player_score("Charlie"),
    #         {"name": "Charlie", "scores": [], "games_played": 0, "average_score": 0},
    #     )


if __name__ == "__main__":
    unittest.main
