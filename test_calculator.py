
import unittest

from calculator import add, divide, multiply, subtract


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(10, 0), 0)


if __name__ == "__main__":
    unittest.main()
