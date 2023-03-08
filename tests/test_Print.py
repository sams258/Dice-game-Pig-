import unittest
from Print import Print
import io
import sys
import time
from unittest.mock import patch

class TestPrint(unittest.TestCase):

    def setUp(self):
        # This method is called before each test case, so we can use it to redirect stdout
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # This method is called after each test case, so we can use it to restore stdout
        sys.stdout = sys.__stdout__

    def test_print_sleep(self):
        Print.print_sleep("Test")
        time.sleep(1)  # Wait for the sleep to finish
        self.assertEqual(self.captured_output.getvalue(), "Test\n\n")
    def test_print_sleep(self):
        with patch('builtins.print') as mock_print:
            Print.print_sleep("Hello", "World", end='!')
        mock_print.assert_called_once_with("Hello", "World", end='!')
        
    @patch('time.sleep')
    def test_print_sleep_sleep_called(self, mock_sleep):
        Print.print_sleep("Hello", "World")
        mock_sleep.assert_called_once_with(1)
        
    @patch('builtins.print', side_effect=[None])
    def test_print_sleep_return_none(self, mock_print):
        result = Print.print_sleep("Hello", "World")
        self.assertIsNone(result)
        
    def test_print_sleep_no_args(self):
        with patch('builtins.print') as mock_print:
            Print.print_sleep()
        mock_print.assert_called_once_with()
        
    def test_print_sleep_kwargs(self):
        with patch('builtins.print') as mock_print:
            Print.print_sleep("Hello", "World", end='!', sep='***')
        mock_print.assert_called_once_with("Hello", "World", end='!', sep='***')
        
    @patch('builtins.print', side_effect=Exception("Mock Exception"))
    def test_print_sleep_exception(self, mock_print):
        with self.assertRaises(Exception):
            Print.print_sleep("Hello", "World")
            
    @patch('builtins.print', side_effect=KeyboardInterrupt)
    def test_print_sleep_keyboard_interrupt(self, mock_print):
        with self.assertRaises(KeyboardInterrupt):
            Print.print_sleep("Hello", "World")
            
    @patch('builtins.print')
    def test_print_sleep_contains_hello_world(self, mock_print):
        Print.print_sleep("Hello", "World")
        mock_print.assert_called_once()
        printed_output = mock_print.call_args[0][0]
        self.assertIn("Hello", printed_output)
        self.assertIn("World", printed_output)
        
    @patch('builtins.print', side_effect=[None])
    def test_print_sleep_called_with_tuple(self, mock_print):
        args = ("Hello", "World")
        Print.print_sleep(*args)
        mock_print.assert_called_once_with(*args)
if __name__ == '__main__':
    unittest.main()
