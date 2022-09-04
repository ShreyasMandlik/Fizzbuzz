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