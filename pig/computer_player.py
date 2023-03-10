"""This module contains the ComputerPlayer class."""

import random
from player import Player
from print import Print
from histogram import Histogram


# pylint: disable=R0903
class ComputerPlayer(Player):
    """Represents a computer player in the game of Pig.

    This class extends the Player class and overrides the take_turn method
    to implement a computer-controlled player that makes decisions based on
    a specified difficulty level.

    Args:
        name (str): The name of the player.
        difficulty (str): The difficulty level of the computer player,
            either "easy" or "hard".
    """

    def __init__(self, name, difficulty):
        """Initialize a new instance of the ComputerPlayer class.

        Args:
            name (str): The name of the player.
            difficulty (str): The difficulty level of the computer player,
                either "easy" or "hard".
        """
        super().__init__(name)
        self.difficulty = difficulty

    def take_turn(self):
        """Simulate the computer player taking a turn.

        The computer player will roll a die until either a 1 is rolled or
        the turn score meets the threshold for the difficulty level.

        Returns:
            int: The score earned by the computer player during the turn.
        """
        turn_score = 0
        while True:
            roll = random.randint(1, 6)
            Print.print_sleep(f"{self.name} rolled a {[roll]}")

            Histogram.add_roll(roll)
            if roll == 1:
                Print.print_sleep(f"{self.name} lost their turn!")
                return 0

            turn_score += roll
            Print.print_sleep(f"{self.name}'s current turn score: "
                              f"{turn_score}")

            if self.difficulty == "easy":
                if turn_score >= 15:
                    self.total_score += turn_score
                    Print.print_sleep(f"{self.name}'s total score: "
                                      f"{self.total_score}")
                    return turn_score

            if self.difficulty == "hard":
                if turn_score >= (25 - len(str(self.total_score))):
                    self.total_score += turn_score
                    Print.print_sleep(f"{self.name}'s total score: "
                                      f"{self.total_score}")
                    return turn_score

            self.total_score += turn_score
            Print.print_sleep(f"{self.name}'s total score: {self.total_score}")
            return turn_score
