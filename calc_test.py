import pytest
import unittest

from SimpleCalc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()
# this will run first (should pass)
    def test_add(self): # naming convention is essential as 'test' is the word we need to use naming tests
        self.assertEqual(self.calc.add(2, 4), 6) # it will add them and check if it is 6

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

# make sure you make the python file called name_test, not name_tests