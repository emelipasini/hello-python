import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    # python -m unittest discover to run the tests

    def setUp(self):
        self.calculator = Calculator()

    def test_initial_value(self):
        self.assertEqual(self.calculator.value, 0)

    def test_add_method_works(self):
        self.calculator.add(1, 3)
        self.assertEqual(self.calculator.value, 4)

    def test_subtract_method_works(self):
        self.calculator.subtract(9, 6)
        self.assertEqual(self.calculator.value, 3)

    def test_multiply_method_works(self):
        self.calculator.multiply(4, 5)
        self.assertEqual(self.calculator.value, 20)

    def test_divide_method_works(self):
        self.calculator.divide(8, 2)
        self.assertEqual(self.calculator.value, 4)

    def test_divide_method_fails_with_zero(self):
        self.calculator.divide(8, 0)
        self.assertEqual(self.calculator.value, "No se puede dividir por cero")
