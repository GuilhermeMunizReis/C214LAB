from abc import ABC, abstractmethod
from character import Character

class Feat(ABC):
    def __init__(self):
        self.feat = ""
        self.description = ""
        self.requirements = ""
    
    @abstractmethod
    def modify_character(self, character: Character):
        pass

class Defense(Feat):
    def __init__(self):
        super().__init__()
        self.feat = "Defense"
        self.description = "+1 AC when using a armor"
        self.requirements = "No requirements"

    def modify_character(self, character:Character):
        character.ac += 1