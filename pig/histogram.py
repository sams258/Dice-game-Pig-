"""This module contains the Histogram class."""

from print import Print


class Histogram:
    """Represents a histogram of rolls in the game of Pig.

    This class provides methods for adding rolls to the histogram,
    clearing the histogram, displaying the histogram, and setting a cheat
    mode where the histogram is fixed to always roll a 6.

    Attributes:
        rolls (dict): A dictionary mapping each possible roll (1-6) to the
            number of times it has been rolled.
    """

    rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    @classmethod
    def add_roll(cls, roll):
        """Add a roll to the histogram.

        Args:
            roll (int): The roll value to add to the histogram.
        """
        cls.rolls[roll] += 1

    @classmethod
    def clear(cls):
        """Clear the histogram."""
        cls.rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    @classmethod
    def display(cls):
        """Display the histogram."""
        Print.print_sleep("\nHistogram of Rolls:")
        for roll, count in cls.rolls.items():
            print(f"{roll}: {'*' * count}")

    @classmethod
    def set_cheat(cls):
        """Set the histogram to cheat mode, always rolling a 6."""
        cls.rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}
