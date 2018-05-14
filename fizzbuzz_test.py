import unittest
from fizzbuzz import fizzbuzz

class Testfizzbuzz(unittest.TestCase):

    def test_should_return_normal_number(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_3_should_return_Fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_5_should_return_Buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_3_and_5_should_return_FizzBuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
