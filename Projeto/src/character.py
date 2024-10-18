# src/character.py

class Character:
    def __init__(self, name, character_class, level):
        self.name = name
        self.character_class = character_class
        self.level = level

    def level_up(self):
        self.level += 1

