import sys

sys.path.append('src')

from gamelib import *
from shop import *
from utils import *
from functools import partial

class App:
    def __init__(self):
        self.app = Game(resolution=(1200,700))
        self.global_itens = GlobalItens()
        self.shop = None
        self.screen = "menu"              #Screen will be stored here
        self.market_total_itens = None
     
    def start(self):
        self.set_screen()
        self.app.start()

    def set_market(self, market_id):
        if market_id == 0:
            self.screen = "menu"
        else:
            self.screen = "market"
            self.shop = self.global_itens.get_shop(market_id)
            self.market_total_itens = len(self.shop.itens)

        self.set_screen()

    def set_screen(self):
        screen = None
        if self.screen == "menu":
            screen = self.menu_screen()
        if self.screen == "market":
            screen = self.market_screen()

        self.app.set_screen(screen)

    def menu_screen(self):
        screen = Screen()

        options_lb = Label(text="Escolha uma das opções", x=400, y=200, height=30, width=400)
        screen.add(options_lb)

        cont = 0

        for i in self.global_itens.market_ids:
            cont += 1
            new_y = 300 + cont*40
            screen.add(Button(text=self.global_itens.market_ids[i], x=400, y=new_y, height=30, width=400, command=partial(self.set_market, i)))
        
        return screen

    def market_screen(self):
        screen = Screen()

        name_lb = Label(text=self.shop.name, x=50, y=30, height=30, width=200)
        screen.add(name_lb)

        owner_lb = Label(text=self.shop.owner, x=300, y=30, height=30, width=200)
        screen.add(owner_lb)

        back_bt = Button(text="Voltar", x=700, y=30, height=30, width=100, command=partial(self.set_market, 0))
        screen.add(back_bt)

        name_item = Label(text="Item", x=50, y=90, height=30, width=200)
        screen.add(name_item)

        dmg_item = Label(text="Damage", x=270, y=90, height=30, width=200)
        screen.add(dmg_item)

        props_item = Label(text="Props", x=490, y=90, height=30, width=400)
        screen.add(props_item)

        price_item = Label(text="Price", x=910, y=90, height=30, width=200)
        screen.add(price_item)

        lower_bound = 0
        upper_bound = min( 13, self.market_total_itens)

        cont = 1
        for i in range(lower_bound, upper_bound):
            new_y = 90 + cont*40
            item = self.shop.itens[i]

            name = Label(text=item.name, x=50, y=new_y, height=30, width=200)
            screen.add(name)

            dmg = Label(text=item.damage, x=270, y=new_y, height=30, width=200)
            screen.add(dmg)
         
            props = Label(text=item.props, x=490, y=new_y, height=30, width=400)
            screen.add(props)
            
            p_str = f"{item.price.value} {item.price.shortname}"
            price = Label(text=p_str, x=910, y=new_y, height=30, width=200)
            screen.add(price)

            cont += 1

        return screen