import sys

sys.path.append('src')

from gamelib import *
from shop import *
from market_mock import *

class App:
    def __init__(self):
        self.app = Game(resolution=(1200,700))
        self.shop = get_shop_std()
     
    def start(self):
        self.set_screen()
        self.app.start()

    def set_screen(self):
        screen = Screen()

        name_lb = Label(text=self.shop.name, x=50, y=50, height=30, width=200)
        screen.add(name_lb)

        owner_lb = Label(text=self.shop.owner, x=300, y=50, height=30, width=200)
        screen.add(owner_lb)

        cont = 1
        for item in self.shop.itens:
            new_y = 90 + cont*40
            
            name = Label(text=item.name, x=50, y=new_y, height=30, width=200)
            screen.add(name)

            desc = Label(text=item.desc, x=300, y=new_y, height=30, width=400)
            screen.add(desc)

            p_str = f"{item.price.value} {item.price.shortname}"
            price = Label(text=p_str, x=750, y=new_y, height=30, width=200)
            screen.add(price)

            cont += 1

        self.app.set_screen(screen)