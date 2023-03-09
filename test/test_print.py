import unittest
import io
import sys
import time
from unittest.mock import patch
from pig.print import Print


class TestPrint(unittest.TestCase):
    """
    Test case for the Print class.
    """

    def setUp(self):
        """
        Prepare the test environment by redirecting stdout to a StringIO object.
        """
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """
        Restore stdout to its original value.
        """
        sys.stdout = sys.__stdout__

    def test_print_sleep_calls_print_once(self):
        """
        Test that the print_sleep method calls the print function exactly once.
        """
        with patch("builtins.print") as mock_print:
            Print.print_sleep("Hello", "World")
            mock_print.assert_called_once()

if __name__ == "__main__":
    unittest.main()
