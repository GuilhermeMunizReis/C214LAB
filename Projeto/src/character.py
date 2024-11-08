from player_classes import *

class Character:
    def __init__(self, name:str, race:str, level:int):
        self.name = name
        self.race = race
        self.character_class = []
        self.character_multiclass = []
        self.level = level
        self.proficiencies = []
        self.feats = []
        self.saving_throws = []
        self.prof_weapon = ""
        self.prof_armor = ""
        self.prof_bonus = 0
        self.str_base = 1
        self.dex_base = 1
        self.con_base = 1
        self.int_base = 1
        self.wis_base = 1
        self.cha_base = 1
        self.str_value = 1
        self.dex_value = 1
        self.con_value = 1
        self.int_value = 1
        self.wis_value = 1
        self.cha_value = 1
        self.str_current = 1
        self.dex_current = 1
        self.con_current = 1
        self.int_current = 1
        self.wis_current = 1
        self.cha_current = 1    
        
    def get_character_level(self):
        level = 0
        
        level += self.character_class.level
        
        for c in self.character_multiclass:
            level += c.level

        self.level = level