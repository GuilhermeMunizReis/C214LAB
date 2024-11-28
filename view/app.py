import sys

sys.path.append('src')

from gamelib import *
from shop import *
from market_mock import *

class App:
    def __init__(self):
        self.app = Game(resolution=(1200,700))
        self.shop = get_shop_std()
        self.screen = "market"              #Screen will be stored here
     
    def start(self):
        self.set_screen()
        self.app.start()

    def set_screen(self):

        if self.screen == "menu":
            pass
        if self.screen == "market":
            self.market_screen()
    
    def market_screen(self):
        screen = Screen()

        name_lb = Label(text=self.shop.name, x=50, y=30, height=30, width=200)
        screen.add(name_lb)

        owner_lb = Label(text=self.shop.owner, x=300, y=30, height=30, width=200)
        screen.add(owner_lb)

        name_item = Label(text="Item", x=50, y=90, height=30, width=200)
        screen.add(name_item)

        dmg_item = Label(text="Description", x=270, y=90, height=30, width=400)
        screen.add(dmg_item)

        price_item = Label(text="Price", x=690, y=90, height=30, width=200)
        screen.add(price_item)


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