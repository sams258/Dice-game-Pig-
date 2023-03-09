import time

class Print:
    """
    A class for printing output with a one-second delay.
    """

    def __init__(self):
        """
        Initialize a new Print instance.
        """
        pass

    @staticmethod
    def print_sleep(*args, **kwargs):
        """
        Print the specified arguments with an extra newline character and a one-second delay.

        Args:
            *args: Any number of positional arguments to be passed to the print function.
            **kwargs: Any keyword arguments to be passed to the print function.

        Returns:
            None.
        """
        print(*args, **kwargs)
        time.sleep(1)
