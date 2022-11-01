import unittest

from vauvau import start
from vauvau import calculate

class TestTestDrive(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(calculate(52,52,40,32,5,60,100), 'both\nboth\nnone', 'wrong answer')
    def test2_answer(self):
        self.assertEqual(calculate(1009,5,999,4,500,600,999), 'one\none\nboth', 'wrong answer')
    def test3_answer(self):
        self.assertEqual(calculate(3,6,2,4,1,4,7), 'both\nboth\nboth', 'wrong answer')
    def test4_answer(self):
        self.assertEqual(calculate(100,100,50,50,49,52,100), 'both\nnone\nnone', 'wrong answer')
    def test5_answer(self):
        self.assertNotEqual(calculate(9,18,4,10,2,6,20), ' ', 'wrong answer')
    def test6_answer(self):
        self.assertEqual(calculate(40,30,30,20,21,31,51), 'one\none\none', 'wrong answer')


if __name__ == "__main__":
    unittest.main(verbosity=2)