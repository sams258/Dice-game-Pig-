"""This module contains the ComputerPlayer class."""
import random
from player import Player
from print import Print
from histogram import Histogram


# pylint: disable=R0903
class ComputerPlayer(Player):
    """_summary_.

    Args:
        Player (_type_): _description_
    """

    def __init__(self, name, difficulty):
        """_summary_.

        Args:
            name (_type_): _description_
            difficulty (_type_): _description_
        """
        super().__init__(name)
        self.difficulty = difficulty

    def take_turn(self):
        """_summary_.

        Returns:
            _type_: _description_
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
