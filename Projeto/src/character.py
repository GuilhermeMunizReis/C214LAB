class Character:
    def __init__(self, name:str, character_class:str, level:int):
        self.name = name
        self.character_class = character_class
        self.level = level

    def level_up(self):
        self.level += 1

