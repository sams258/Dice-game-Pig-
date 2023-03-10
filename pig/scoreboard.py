"""This module contains the Scoreboard class."""
import json
import os


class Scoreboard:
    """This module contains the Scoreboard class."""

    def __init__(self):
        """Initialize a new instance of the Scoreboard class."""
        self.scores = {}
        self.load_scores()

    def add_score(self, name, score):
        """
        Add a score for the specified player.

        Args:
            name (str): The name of the player.
            score (int): The score to be added.
        """
        if name in self.scores:
            self.scores[name]["scores"].append(score)
            self.scores[name]["games_played"] += 1
        else:
            self.scores[name] = {"scores": [score], "games_played": 1}
        self.save_scores()

    def get_high_scores(self):
        """
        Return the high scores of all players.

        Returns:
            list: A list of tuples containing the player name,
            high score, and number of games played.
        """
        high_scores = []
        for name, data in self.scores.items():
            high_score = max(data["scores"])
            high_scores.append((name, high_score, data["games_played"]))
        high_scores.sort(key=lambda x: x[1], reverse=True)
        return high_scores

    def load_scores(self):
        """Load the scores from the scores.json file."""
        try:
            with open("pig/scores.json", "r", encoding='utf-8') as file:
                self.scores = json.load(file)
        except FileNotFoundError:
            self.scores = {}

    def save_scores(self):
        """Save the scores to the scores.json file."""
        # create the pig directory if it doesn't exist
        os.makedirs('pig', exist_ok=True)

        # open the scores.json file in write mode
        with open("pig/scores.json", "w", encoding='utf-8') as file:
            json.dump(self.scores, file)

    def get_player_score(self, name):
        """
        Return the total score of the specified player.

        Args:
            name (str): The name of the player.

        Returns:
            int: The total score of the player.
        """
        if name in self.scores:
            return sum(self.scores[name]["scores"])
        return 0

    def change_player_name(self, old_name, new_name):
        """
        Change the name of a player.

        Args:
            old_name (str): The current name of the player.
            new_name (str): The new name of the player.
        """
        if old_name in self.scores:
            self.scores[new_name] = self.scores.pop(old_name)
            self.save_scores()

    def clear(self):
        """Clear the scores."""
        self.scores = {}
        self.save_scores()
