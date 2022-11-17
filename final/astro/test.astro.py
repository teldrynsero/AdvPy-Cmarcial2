import unittest

from astro import sign

class TestAstro(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(sign("29 Feb"), 'Pisces', 'wrong star sign')
    def test2_answer(self):
        self.assertNotEqual(sign("20 Apr"), 'Taurus', 'wrong star sign')
    def test3_answer(self):
        self.assertEqual(sign("2 Sep"), 'Virgo', 'wrong star sign')
        
if __name__ == "__main__":
    unittest.main(verbosity=2)