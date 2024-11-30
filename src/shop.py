from item import *

"""
TO DO 

 - Set location as a argument
"""
class Shop:
    def __init__(self, name:str, owner:str):
        self.name = name
        self.owner = owner
        self.itens = []

    def add_item(self, item:Item):
        self.itens.append(item)

    def print_item_list(self):
        """
        Shows every item on shop
        """
        if self.itens == []:
            print("No itens")

        for i in self.itens:
            s = f"{i.name} - {i.price.value} {i.price.shortname}"
            print(s)

    def clear_repeated_elements(self):
        item_names = set()
        not_repeated = []
        for item in self.itens:
            if item.name not in item_names:
                item_names.add(item.name)
                not_repeated.append(item)
        self.itens = not_repeated

    def __repr__(self):
        print(f"{self.name} - {self.owner}\t")
        self.print_item_list()

        return ""