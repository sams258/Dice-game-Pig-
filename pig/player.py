"""This module contains the Player class."""

import random
from print import Print
from histogram import Histogram


# pylint: disable=R0903
class Player:
    """_summary_."""

    def __init__(self, name):
        """_summary_.

        Args:
            name (_type_): _description_
        """
        self.name = name
        self.total_score = 0

    def take_turn(self):
        """_summary_.

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        turn_score = 0
        while True:
            roll = random.randint(1, 6)
            Print.print_sleep(f"{self.name} rolled a {[roll]}")

            Histogram().add_roll(roll)
            if roll == 1:
                Print.print_sleep(f"{self.name} lost their turn!")

                return 0
            else:
                turn_score += roll
                Print.print_sleep(f"{self.name}'s current "
                                  f"turn score: {turn_score}")

                while True:
                    try:
                        choice = input("Do you want to Roll or Hold?"
                                       "(r/h) ")

                        if choice.lower() not in ["r", "h", "c"]:
                            raise ValueError
                        break
                    except ValueError:
                        Print.print_sleep(
                            "Invalid input. Please enter 'r', 'h', or 'c'."
                        )

                if choice.lower() == "h":
                    self.total_score += turn_score
                    Print.print_sleep(f"{self.name}'s total score: "
                                      f"{self.total_score}")

                    return turn_score
                elif choice.lower() == "c":
                    self.total_score += 100
                    Print.print_sleep(f"{self.name} cheated and won the game!")

                    return 100
