import unittest
from unittest import result
import FizBuz
class Test(unittest.TestCase):
    

    def test_Print_the_number_itself(self):
        result=FizBuz.fizzBuzz(1)
        self.assertEqual(result,[1])

        result1=FizBuz.fizzBuzz(2)
        self.assertEqual(result1,[1,2])
    

    def test_Print_Multiple_of_3(self):
        result=FizBuz.fizzBuzz(3)
        self.assertEqual(result,[1,2,"Fizz"])

        result1=FizBuz.fizzBuzz(9)
        self.assertEqual(result1,[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz'])


    def test_Print_Multiple_of_5(self):
        result=FizBuz.fizzBuzz(5)
        self.assertEqual(result,[1, 2, 'Fizz', 4, 'Buzz'])

        result1=FizBuz.fizzBuzz(10)
        self.assertEqual(result1,[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz'])

    def test_Print_Multiple_of_3_and_5_both(self):
        result=FizBuz.fizzBuzz(15)
        self.assertEqual(result,[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'])

        result1=FizBuz.fizzBuzz(30)
        self.assertEqual(result1,[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz'])



