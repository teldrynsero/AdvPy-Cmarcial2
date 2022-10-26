import unittest

from howl import fenrir
from howl import response

class TestHowl(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(response("AAHOWO"), 'AAHOWOO', 'wrong answer')
    def test2_answer(self):
        self.assertEqual(response("AAAWOHO"), 'AAAWOHOO', 'wrong answer')
    def test3_answer(self):
        self.assertNotEqual(response("AAHOOW"), 'AAHOOW', 'wrong answer')
    def test4_answer(self):
        self.assertEqual(response("WAHOOO"), 'WAHOOOO', 'wrong answer')
    def test5_answer(self):
        self.assertEqual(response("HAWOO"), 'HAWOOO', 'wrong answer')
    def test6_answer(self):
        self.assertIn(response("AWHOOO"), 'AWHOOOO', 'wrong answer')

if __name__ == "__main__":
    unittest.main(verbosity=2)