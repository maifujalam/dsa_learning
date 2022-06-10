import calculator as cal
import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = cal.add(5, 3)
        self.assertEqual(result, 8)
        self.assertEqual(cal.add(-5, 2), -3)
        self.assertEqual(cal.add(5, -2), 3)
        self.assertEqual(cal.add(-5, -2), -7)
        self.assertEqual(cal.add(0, 3), 3)
        self.assertEqual(cal.add(0, -3), -3)

    def test_subtract(self):
        self.assertEqual(cal.subtract(5, 3), 2)
        self.assertEqual(cal.subtract(-5, 2), -7)
        self.assertEqual(cal.subtract(5, -2), 7)
        self.assertEqual(cal.subtract(-5, -2), -3)
        self.assertEqual(cal.subtract(0, 3), -3)
        self.assertEqual(cal.subtract(0, -3), 3)

    def test_multiply(self):
        self.assertEqual(cal.multiply(5, 3), 15)
        self.assertEqual(cal.multiply(-5, 2), -10)
        self.assertEqual(cal.multiply(5, -2), -10)
        self.assertEqual(cal.multiply(-5, -2), 10)
        self.assertEqual(cal.multiply(0, 3), 0)
        self.assertEqual(cal.multiply(0, -3), 0)

    def test_divide(self):
        self.assertEqual(cal.divide(5, 3), 1)
        self.assertEqual(cal.divide(-5, 2), -3)
        self.assertEqual(cal.divide(5, -2), -3)
        self.assertEqual(cal.divide(-5, -2), 2)
        self.assertEqual(cal.divide(0, 3), 0)
        self.assertEqual(cal.divide(0, -3), 0)
        self.assertRaises(ValueError, cal.divide, 10, 0)  # P1: Type of Error,P2: Calling method,{P4..: Method args)
        with self.assertRaises(ValueError):
            cal.divide(20, 0)


if __name__ == '__main__':
    unittest.main()
