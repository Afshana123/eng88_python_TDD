# Test Driven Development (TDD)

---

- _Pytest and Unittest_

- _Use pip to install the packages_

## What is TDD?

Test Driven Development (TDD) is a software development approach in which test cases are developed to specify and validate what the code will do. In simple terms, test cases for each functionality are created and tested first and if the test fails then the new code is written in order to pass the test and making code simple and bug-free.

- Nothing is pushed or sent to production before it is tested.
- Production means when it is in front of clients to view (the users).
- If the test fails, then it will have to be tested again.
- The reason for TDD is that the program is error free or bug free.
###

<center> <img src="https://www.qaiglobalinstitute.com/wp-content/uploads/2018/02/tdd.jpg" width="250" height="250"> </center>

**TDD:**
- RED  is where everything fails before writing functional code.
- Then we write the code to pass (GREEN).
- BLUE Refactoring is when we improve our code then start again.

## Exercise

1. Let's create a file to write our tests for our basic calculator class.
2. Then we will create a file to add functionality to pass the tests.

Begin by writing a command on the terminal `pip install pytest` to install pytest.

Now, let's write our test:

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
Command to run the tests `python -m unittest discover -v` (which gives more information) and `python -m unittest`. 

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

Let's run the tests again now to ensure all 4 tests pass.

So, run the command again `python -m unittest`. 

- [x] All four tests passed.





