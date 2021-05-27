# Test Driven Developmeent (TDD)

Pytest and Unittest

Use pip to install the packages 

What is TDD?

Nothing is pushed or sent to production before it is tested 

Production means in front of clients (the users)

If the test fails, then we will again test 

**TDD:**
- Starts with RED where everything fails before writing functional code 
- Then we write the code to pass GREEN
- BLUE Refactoring - we improve our code, then start again 

Let's create a file to write out tests for our basic calculator class
Then we will create a file to add functionality to pass the tests 

Let's write our test:

```python
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
```
Command to run the tests `python -m unittest discover -v` and `python -m unittest`

Let's add the functionality to pass the tests:

```python
class SimpleCalc:

    def add(self, int1, int2):
        return int1 + int2

    def subtract(self, int1, int2):
        return int1 - int2

    def multiply(self, int1, int2):
        return int1 * int2

    def divide(self, int1, int2):
        return int1 / int2
```

Let's run the tests again now to ensure all 4 tests pass

So, run the command again `python -m unittest`





