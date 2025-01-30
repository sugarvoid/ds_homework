from enum import Enum


class PokemonType(Enum):
    ELECTRIC = "Electric"
    FIRE = "Fire"
    WATER = "Water"
    GRASS = "Grass"
    PSYCHIC = "Psychic"
    ICE = "Ice"
    DRAGON = "Dragon"
    GHOST = "Ghost"
    BUG = "Bug"
    FAIRY = "Fairy"
    NORMAL = "Normal"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    ROCK = "Rock"
    STEEL = "Steel"
    DARK = "Dark"

class Pokemon:
    def __init__(self, dex_number: int):
        self.name = "name"
        self.dex_number = dex_number 
        self.poke_types = PokemonType.DRAGON

        self.base_stats = {
            'HP': 50,
            'Attack': 55,
            'Defense': 40,
            'Speed': 90,
            'Special_Attack': 50,
            'Special_Defense': 50
        }
    

    def take_damage(self, damage: int):
        self.stats['HP'] = clamp(0, self.stats['HP'] - damage, 100)
        print(f"{self.name} took {damage} damage! HP is now {self.stats['HP']}.")


    def __str__(self):
        types = ', '.join([poke_type.value for poke_type in self.poke_types])
        return f"{self.name} (Dex #{self.dex_number}, Type(s): {types})"



def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))