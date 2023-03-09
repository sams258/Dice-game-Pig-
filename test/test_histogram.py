import sys

sys.path.append("pig")
import unittest
from pig.histogram import Histogram
from unittest.mock import patch
from io import StringIO


class TestHistogram(unittest.TestCase):
    def setUp(self):
        Histogram.clear()

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


if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)
