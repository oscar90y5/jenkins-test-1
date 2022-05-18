import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        calculated_value = cal.add(3, 2)
        expected_value = 5
        self.assertEqual(calculated_value, expected_value)

if __name__ == '__main__':
    unittest.main()
