"""This module contains a custom print function."""

import time


# pylint: disable=R0903
class Print:
    """This class contains a custom print function."""

    def __init__(self):
        """Initialize the function."""

    @staticmethod
    def print_sleep(*args, **kwargs):
        """Print the specified arguments.

        With an extra newline character and a one-second delay.
        Args:
            *args: Any number of positional arguments
            to be passed to the print function.
            **kwargs: Any keyword arguments
            to be passed to the print function.

        Returns:
            None.
        """
        print(*args, **kwargs)
        time.sleep(1)
