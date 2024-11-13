import unittest
import sys

sys.path.append('src')

from item import *

class TestCurrency(unittest.TestCase):
    def setUp(self):
        self.c = Currency("Ardin", "ard", 11.4)

    def testItemInstance(self):
        i = Item("Sword", "1d6 damage", self.c)
        
        self.assertEqual(i.name, "Sword")
        self.assertEqual(i.desc, "1d6 damage")
        self.assertEqual(i.price.value, 11.4)

    def testItemInstanceError(self):

        i = Item("Sword", "1d6 damage", self.c)
        
        self.assertEqual(i.name, "Sword")
        self.assertNotEqual(i.desc, "1d8 damage")
        self.assertEqual(i.price.value, 11.4)

if __name__ == '__main__':  
    unittest.main()