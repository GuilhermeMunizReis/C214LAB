from database import Database
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(db)

data = pokedex.getPokemonByName("Pikachu")
print(data)

data = pokedex.getPokemonByType("Dragon")
print(data)

data = pokedex.getPokemonByWeakness("Fire")
print(data)

data = pokedex.getPokemonByID(79)
print(data)

data = pokedex.getPokemonBySpawnTime("20:00")
print(data)

db.resetDatabase()