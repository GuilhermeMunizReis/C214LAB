from item import *

"""
TO DO 

 - Set location as a argument
"""
class Shop:
    def __init__(self, name:str, owner:str, itens:list[Item] = []):
        self.name = name
        self.owner = owner
        self.itens = itens

    def add_item(self, item:Item):
        self.itens.append(item)

    def print_item_list(self):
        """
        Shows every item on shop
        """
        for i in self.itens:
            s = f"{i.name} - {i.currency.price.value} {i.currency.price.shortname}"
            print(s)