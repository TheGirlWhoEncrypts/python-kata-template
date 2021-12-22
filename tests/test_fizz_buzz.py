import unittest
from src.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_return_fizz_if_multiple_of_three(self):
        self.assertEqual("Fizz", fizz_buzz(6))

    def test_fizz_buzz_return_fizz_if_multiple_of_five(self):
        self.assertEqual("Buzz", fizz_buzz(10))

    def test_fizz_buzz_return_fizzBuzz_if_multiple_of_both(self):
        self.assertEqual("FizzBuzz", fizz_buzz(30))

    def test_fizz_buzz_return_num_if_regular_num(self):
        self.assertEqual(98, fizz_buzz(98))
