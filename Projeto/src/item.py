from currency import *

class Item:
    def __init__(self, name: str, desc:str, price: Currency):
        self.name = name
        self.desc = desc
        self.price = price

    