from database import Database
from WriteAJson import writeAJson

"""
db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()
"""

class Pokedex:
    def __init__(self, database: Database):
        self.db = database
    
    def getPokemonByName(self, pokemon_name: str):
        data = self.db.collection.find({"name": pokemon_name})
        print("D1")
        self._generate_json(data, pokemon_name)
        
        return data

    def getPokemonByType(self, pokemon_type: str):
        data = self.db.collection.find({"types": [pokemon_type]})
        print("D2")
        print(data)
        self._generate_json(data, pokemon_type)
      
        return data
 
    def getPokemonByWeakness(self, weakness: str):
        data = self.db.collection.find({"weaknesses": [weakness]})
        print("D3")
        self._generate_json(data, weakness)
        
        return data
 
    def getPokemonByID(self, id_: int):
        data = self.db.collection.find({"id": id_})
        print("D4")
        self._generate_json(data, id_)
        
        return data
 
    def getPokemonBySpawnTime(self, spawn_time: str):
        data = self.db.collection.find({"spawn_time": spawn_time})
        print("D5")
        self._generate_json(data, "all")
        
        return data

    def _generate_json(self, data, name):
        writeAJson(data, name)


