from player_classes import *

class Character:
    def __init__(self, name:str, character_class:Character_Class_ABC, character_multiclass:list[Character_Class_ABC], level:int):
        self.name = name
        self.character_class = character_class
        self.character_multiclass = character_multiclass
        self.level = level
        
    def get_character_level(self):
        level = 0
        
        level += self.character_class.level
        
        for c in self.character_multiclass:
            level += c.level

        self.level = level