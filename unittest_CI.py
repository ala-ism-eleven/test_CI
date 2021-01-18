"""
Unit tests for the calculator library
"""

import test_Circle_CI
import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(5, test_Circle_CI.add(2, 2))

    def test_subtraction(self):
        self.assertEqual(120, test_Circle_CI.subtract(4, 2))


if __name__ == "__main__":
    unittest.main()
