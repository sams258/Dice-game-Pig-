"""This module contains the Scoreboard class."""
import json


class Scoreboard:
    """_summary_."""

    def __init__(self):
        """_summary_."""
        self.scores = {}
        self.load_scores()

    def add_score(self, name, score):
        """_summary_.

        Args:
            name (_type_): _description_
            score (_type_): _description_
        """
        if name in self.scores:
            self.scores[name]["scores"].append(score)
            self.scores[name]["games_played"] += 1
        else:
            self.scores[name] = {"scores": [score], "games_played": 1}
        self.save_scores()

    def get_high_scores(self):
        """_summary_.

        Returns:
            _type_: _description_
        """
        high_scores = []
        for name, data in self.scores.items():
            high_score = max(data["scores"])
            high_scores.append((name, high_score, data["games_played"]))
        high_scores.sort(key=lambda x: x[1], reverse=True)
        return high_scores

    def load_scores(self):
        """_summary_."""
        try:
<<<<<<< HEAD:pig/Scoreboard.py
            with open("scores.json", "r", encoding='utf-8') as file:
                self.scores = json.load(file)
=======
            with open("scores.json", "r") as f:
                self.scores = json.load(f)
>>>>>>> 1a3437d6689f64f9adbca65e4ffa5958ec163b0d:pig/scoreboard.py
        except FileNotFoundError:
            self.scores = {}

    def save_scores(self):
        """_summary_."""
        with open("scores.json", "w", encoding='utf-8') as file:
            json.dump(self.scores, file)

    def get_player_score(self, name):
        """_summary_.

        Args:
            name (_type_): _description_

        Returns:
            _type_: _description_
        """
        if name in self.scores:
            return sum(self.scores[name]["scores"])
        return 0

    def change_player_name(self, old_name, new_name):
        """_summary_.

        Args:
            old_name (_type_): _description_
            new_name (_type_): _description_
        """
        if old_name in self.scores:
            self.scores[new_name] = self.scores.pop(old_name)
            self.save_scores()

    def clear(self):
        """_summary_."""
        self.scores = {}
        self.save_scores()
