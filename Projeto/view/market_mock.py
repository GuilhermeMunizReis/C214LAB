from shop import *

def get_shop_std():
    shop = Shop("Blacksmith", "Antonio")

    shop.add_item(Item("Long Sword", "1d8 dmg", Currency("Ardin", "ard", 20.0)))
    shop.add_item(Item("Short Sword", "1d6 dmg", Currency("Ardin", "ard", 12.0)))
    shop.add_item(Item("Dagger Sword", "1d4 dmg", Currency("Ardin", "ard", 5.0)))

    return shop