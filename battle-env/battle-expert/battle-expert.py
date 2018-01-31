"""
Gotta catch em all!
"""
import numpy
import pandas
import os

# Import pokemon data
dir = os.path.dirname(__file__)
pokemon_list = os.path.join(dir, 'datasheet/pokemon.csv')
pokemon_list = pandas.read_csv(pokemon_list)
battle_list = os.path.join(dir, 'datasheet/combats.csv')
battle_list = pandas.read_csv(battle_list)

# scope the sheet, by removing all other generations than 1
# pokemon_list = pokemon_list.drop('#', axis=1)
pokemon_list = pokemon_list[pokemon_list.Generation == 1]
pokemon_list = pokemon_list[pokemon_list.Name.str.contains('Mega') == False]

battle_list = battle_list + 1
battle_list = battle_list[battle_list.First_pokemon <= 166]
battle_list = battle_list[battle_list.Second_pokemon <= 166]

print(pokemon_list)
