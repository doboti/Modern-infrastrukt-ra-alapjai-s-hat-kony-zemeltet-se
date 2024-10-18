
import unittest
from main import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_add_subtract(self):
        calc = Calculator()
        result = calc.add(2, 3)
        final_result = calc.subtract(result, 1)
        self.assertEqual(final_result, 4)

if __name__ == '__main__':
    unittest.main()
