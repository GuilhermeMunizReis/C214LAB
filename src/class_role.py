from abc import ABC, abstractmethod

from utils import Dice
from character import Character

class ClassRole(ABC):
    def __init__(self, character:Character, hp: int):
        self.character = character
        self.total_hp = hp
        self.life_die = 0
        self.feats = []
        self.proficiencies = []
        
    @abstractmethod
    def level_up(self):
        pass
    
class FighterClass(ClassRole):
    def __init__(self, character:Character, hp:int, level:int = 0):
        super().__init__(character, hp)
        self.level = level
        self.life_die = Dice(10)

    def level_up(self, proficiencies: list, feats: str):
        match self.level:
            case 0:
                self.character.prof_bonus = 2
                self.character.proficiencies = ["Athletics", "Intimidation"]
                self.feats.extended("Fighting style - Archer", "Retake Breath")