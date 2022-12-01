import unittest

from mars import launch

class TestMars(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(launch(2030),'no','wrong answer')
    def test2_answer(self):
        self.assertEqual(launch(10000),'yes','wrong answer')
    def test3_answer(self):
        self.assertEqual(launch(9690),'yes','wrong answer')

        
if __name__ == "__main__":
    unittest.main(verbosity=2)