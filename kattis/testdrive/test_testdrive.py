import unittest

from testdrive import start
from testdrive import calculate

class TestTestDrive(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(calculate(-500,-500), 'cruised', 'wrong answer')
    def test2_answer(self):
        self.assertEqual(calculate(-99,59), 'turned', 'wrong answer')
    def test3_answer(self):
        self.assertEqual(calculate(160,300), 'accelerated', 'wrong answer')
    def test4_answer(self):
        self.assertEqual(calculate(100,1), 'braked', 'wrong answer')
    def test5_answer(self):
        self.assertNotEqual(calculate(-99,59), 'braked', 'wrong answer')
    def test6_answer(self):
        self.assertNotEqual(calculate(-8,18), 'braked', 'wrong answer')

if __name__ == "__main__":
    unittest.main(verbosity=2)