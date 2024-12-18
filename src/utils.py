from random import randint
import pandas as pd
from shop import *

import sys

sys.path.append('data')

#This class contains random value elements, therefore it is tested manually
class Utils:
    """
        Contains lots of usefull and common use stuff, like roll dice
    """

    @staticmethod
    def roll(d_side:int = 6, quantity: int = 1) -> int:
        """
        d_side (int) -> Defines how many sides have this dice
        quantity (int) -> Defines how many dice will be rolled. -1:Disadvantage, 1:Normal, 2:Advantage

        return (int) -> Returns roll value. -1:Invalid values
        """
        valid_d_number = [3, 4, 5, 6, 8, 10, 12, 20, 100]

        if d_side not in valid_d_number:
            return -1
        
        lower_bound = 1
        upper_bound = d_side

        values = []

        if quantity == 1:
            return randint(lower_bound, upper_bound)
        elif quantity == -1:
            values.append(randint(lower_bound, upper_bound))
            values.append(randint(lower_bound, upper_bound))
        
            return max(values)
        elif quantity == 2:
            values.append(randint(lower_bound, upper_bound))
            values.append(randint(lower_bound, upper_bound))
        
            return min(values)
        else:
            return -1
        
    @staticmethod
    def load_market(market_id):

        try:
            markets = pd.read_csv('data/markets.csv', delimiter=';')
            itens = pd.read_csv('data/itens.csv', delimiter=';')

            market = markets[markets['market_id'] == market_id]

            if market.empty:
                raise ValueError(f"Mercado com ID {market_id} não encontrado.")
            
            item_ids = market['itens'].iloc[0].strip(';').split('-')

            for i in range(len(item_ids)):
                item_ids[i] = int(item_ids[i])

            market_itens = itens[itens['item_id'].isin(item_ids)]

            shop = Shop(market['name'].iloc[0], market['owner'].iloc[0])

            for _, row in market_itens.iterrows():
                shop.add_item(Item(row['name'], row['damage'], row['props'], Currency("Ardin", "ards", row['price']/100)))

            shop.clear_repeated_elements()
            return shop

        except FileNotFoundError as e:
            print(f"Arquivo não encontrado: {e}")
        except pd.errors.EmptyDataError:
            print("O arquivo CSV está vazio ou faltando colunas necessárias.")
        return None

class GlobalItens:
    """
    This class contains all possible itens on the world
    """

    def __init__(self):
        self.all_itens = []
        self.market_ids = {}

        self.__load_itens_from_csv()
        self.__load_market_ids()

    def get_shop(self, shop_id: int) -> Shop:
        return Utils.load_market(shop_id)

    def __load_itens_from_csv(self):
        self.all_itens = pd.read_csv('data/itens.csv', delimiter=';')

    def __load_market_ids(self):
        try:
            markets = pd.read_csv('data/markets.csv', delimiter=';')

            # Obtém os IDs dos mercados
            self.market_ids = markets.set_index('market_id')["name"].to_dict()
        except Exception as e:
            print(f"Erro ao carregar os IDs dos mercados: {e}")

class Dice:
    """
    Represents a dice 
    """

    def __init__(self, sides:int):
        self.sides = sides

        self.__check_valid_instance()

    def __check_valid_instance(self):
        valid_sides = [3,4,5,6,8,10,12,20,100]

        if self.sides not in valid_sides:
            raise Exception

    def roll_dice(self):
        return randint(1, self.sides)

    def roll_advantage(self):
        return max([randint(1, self.sides), randint(1, self.sides)])

    def roll_disadvantage(self):
        return min([randint(1, self.sides), randint(1, self.sides)])

    def __repr__(self):
        return f"d{self.sides}"
    