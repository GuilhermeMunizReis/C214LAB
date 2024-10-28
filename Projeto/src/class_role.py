from abc import ABC, abstractmethod

class ClassRole(ABC):
    def __init__(self, level: int, feats):
        self.level = level
        self.life_die = 0
        self.feats = []
        
    @abstractmethod
    def level_up(self):
        pass
    