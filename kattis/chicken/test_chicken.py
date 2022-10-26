import unittest

from chicken import start
from chicken import output
from chicken import calculate

class TestChicken(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(calculate(1000,0), 'Dr. Chaz needs 1000 more pieces of chicken!', 'wrong answer')
    def test2_answer(self):
        self.assertEqual(calculate(982,981), 'Dr. Chaz needs 1 more piece of chicken!', 'wrong answer')
    def test3_answer(self):
        self.assertEqual(calculate(134,135), 'Dr. Chaz will have 1 piece of chicken left over!', 'wrong answer')
    def test4_answer(self):
        self.assertEqual(calculate(500,560), 'Dr. Chaz will have 60 pieces of chicken left over!', 'wrong answer')
    def test4_answer(self):
        self.assertEqual(calculate(500,560), 'Dr. Chaz will have 60 pieces of chicken left over!', 'wrong answer')
    def test5_answer(self):
        self.assertEqual(output(-400,400), 'Dr. Chaz needs 400 more pieces of chicken!', 'wrong answer')
    def test6_answer(self):
        self.assertEqual(output(190,-190), 'Dr. Chaz will have 190 pieces of chicken left over!', 'wrong answer')


if __name__ == "__main__":
    unittest.main(verbosity=2)