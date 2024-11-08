class Currency:
    def __init__(self, name:str, shortname:str, value:float = 0.0):
        self.name = name
        self.shortname = shortname 
        self.value = value

    def set_value(self, new_value:float):
        self.value = new_value