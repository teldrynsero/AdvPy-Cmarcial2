import unittest

from abcKattis import order

class TestOrder(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(order(['100','96','97'],['A','B','C']), "96 97 100", 'wrong order')
    def test2_answer(self):
        self.assertEqual(order(['69','30','1'],['C','A','B']), "69 1 30", 'wrong order')
    def test3_answer(self):
        self.assertEqual(order(['25','2','20'],['B','C','A']), "20 25 2", 'wrong order')

        
if __name__ == "__main__":
    unittest.main(verbosity=2)