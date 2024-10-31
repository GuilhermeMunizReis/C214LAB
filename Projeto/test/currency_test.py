import unittest
import sys

sys.path.append('src')

from currency import *

class TestCurrency(unittest.TestCase):
    def testCurrencyInstance(self):
        c = Currency("Ardin", "ard", 11.4)

        self.assertEqual(c.name, "Ardin")
        self.assertEqual(c.shortname, "ard")
        self.assertEqual(c.value, 11.4)

    def testCurrencyInstanceError(self):
        c = Currency("Ardin", "ard", 11.4)

        self.assertEqual(c.name, "Ardin")
        self.assertEqual(c.shortname, "ard")
        self.assertNotEqual(c.value, 20)

if __name__ == '__main__':  
    unittest.main()