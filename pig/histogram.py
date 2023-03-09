"""This module contains the Histogram class."""

from print import Print


class Histogram:
    """_summary_."""

    rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    @classmethod
    def add_roll(cls, roll):
        """_summary_.

        Args:
            roll (_type_): _description_
        """
        cls.rolls[roll] += 1

    @classmethod
    def clear(cls):
        """_summary_."""
        cls.rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    @classmethod
    def display(cls):
        """_summary_."""
        Print.print_sleep("\nHistogram of Rolls:")
        for roll, count in cls.rolls.items():
            print(f"{roll}: {'*' * count}")

    @classmethod
    def set_cheat(cls):
        """_summary_."""
        cls.rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}
