import sys

sys.path.append("pig")
import unittest
from pig.histogram import Histogram
from unittest.mock import patch
from io import StringIO


class TestHistogram(unittest.TestCase):
    def setUp(self):
        Histogram.clear()

    @classmethod
    def setUpClass(cls):
        cls.rolls = {1: 2, 2: 4, 3: 6, 4: 4, 5: 2, 6: 2}

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        expected_output = "\nHistogram of Rolls:\n1: **\n2: ****\n3: " \
                          "******\n4: ****\n5: **\n6: **\n"
        self.assertEqual(mock_stdout.getvalue(), '')
        self.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    def test_add_roll(self):
        Histogram.add_roll(1)
        self.assertEqual(Histogram.rolls, {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})

    def test_clear(self):
        Histogram.add_roll(1)
        Histogram.clear()
        self.assertEqual(Histogram.rolls, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})

    def test_set_cheat(self):
        Histogram.set_cheat()
        self.assertEqual(Histogram.rolls, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1})

    def test_add_multiple_rolls(self):
        Histogram.add_roll(1)
        Histogram.add_roll(2)
        Histogram.add_roll(3)
        self.assertEqual(Histogram.rolls, {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0})

    def test_set_cheat_with_invalid_input(self):
        with self.assertRaises(TypeError):
            Histogram.set_cheat(1)

    def test_display(self):
        Histogram.add_roll(1)
        Histogram.add_roll(2)
        Histogram.add_roll(3)
        Histogram.add_roll(4)
        Histogram.add_roll(5)
        Histogram.add_roll(6)
        expected_output = "\nHistogram of Rolls:" + "\n1: *" + "\n2: *" + "\n3: *" + "\n4: *" + "\n5: *" + "\n6: *"

    def test_display_with_cheat(self):
        Histogram.set_cheat()
        expected_output = "\nHistogram of Rolls:" + "\n1: " + "\n2: " + "\n3: " + "\n4: " + "\n5: " + "\n6: *"

    def test_display_with_no_rolls(self):
        expected_output = "\nHistogram of Rolls:" + "\n1: " + "\n2: " + "\n3: " + "\n4: " + "\n5: " + "\n6: "

    def test_display_with_multiple_rolls(self):
        Histogram.add_roll(1)
        Histogram.add_roll(1)
        Histogram.add_roll(2)
        Histogram.add_roll(2)
        Histogram.add_roll(3)
        Histogram.add_roll(3)
        Histogram.add_roll(4)
        Histogram.add_roll(4)
        Histogram.add_roll(5)
        Histogram.add_roll(5)
        Histogram.add_roll(6)
        Histogram.add_roll(6)
        expected_output = "\nHistogram of Rolls:" + "\n1: **" + "\n2: **" + "\n3: **" + "\n4: **" + "\n5: **" + "\n6: **"

if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)
