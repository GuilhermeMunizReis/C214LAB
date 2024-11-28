from currency import *

class Item:
    def __init__(self, name: str, damage:str, props:str, price: Currency):
        self.name = name
        self.damage = damage
        self.props = props
        self.price = price

    