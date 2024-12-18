import unittest
import sys

sys.path.append('src')

from shop import *

class TestShop(unittest.TestCase):
    def setUp(self):
        self.c1 = Currency("Ardin", "ard", 30)
        self.c2 = Currency("Ardin", "ard", 40)
        self.c3 = Currency("Ardin", "ard", 50)
        
        self.i1 = Item("Sword", "1d6 damage", "Finesse", self.c1)
        self.i2 = Item("Axe", "1d8 damage", "Finesse", self.c2)
        self.i3 = Item("Mace", "1d6 damage", "Finesse", self.c3)

        self.shop_list = [] 
        self.shop_list.append(self.i1)
        self.shop_list.append(self.i2)

    def testShopInstance(self):
        s = Shop("Crippled Hunter", "Marquito")

        for i in self.shop_list:
            s.add_item(i)

        self.assertEqual(s.itens, self.shop_list)

    def testShopAddItem(self):
        s = Shop("Crippled Hunter", "Marquito")

        for i in self.shop_list:
            s.add_item(i)

        shop_list_test = self.shop_list.copy()

        s.add_item(self.i3)

        shop_list_test.append(self.i3)

        self.assertEqual(s.itens, shop_list_test)
    
    def testShopAddItemError(self):
        s = Shop("Crippled Hunter", "Marquito")

        for i in self.shop_list:
            s.add_item(i)

        shop_list_test = self.shop_list.copy()

        s.add_item(self.i3)

        shop_list_test.append(self.c1)

        self.assertNotEqual(s.itens, shop_list_test)

if __name__ == '__main__':  
    unittest.main()