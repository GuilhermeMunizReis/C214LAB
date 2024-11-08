from utils import *

from abc import ABC

class Character_Class_ABC(ABC):
    def __init__(self, level: int, name: str):
        self.name = name
        self.level = level
        self.life_dice = None

class No_Class(Character_Class_ABC):
    def __init__(self, level, name):
        super().__init__(level, name)
        self.life_dice = Dice(3)