""".

Gotta catch em all

"""
import numpy
import pandas
import os
import sys

# ------ Import course toolbox ------
from tmgsimple import TmgSimple

# ------ Import pokemon data ------
dir = os.path.dirname(__file__)
pokemon_list = os.path.join(dir, 'datasheet/pokemon.csv')
pokemonCompleteList = pandas.read_csv(pokemon_list)
battle_list = os.path.join(dir, 'datasheet/combats.csv')
battle_list = pandas.read_csv(battle_list)

# ------ scope the sheet, by removing all other generations than 1 ------
pokemon_list = pokemonCompleteList[pokemonCompleteList.Generation == 1]
pokemon_list = pokemon_list[pokemon_list.Name.str.contains('Mega') == False]

# ------ Remove # row ------
# pokemon_list = pokemon_list.drop('#', axis=1)
# battle_list = battle_list + 1

# ------ Identify deleted pokemon id -----
irrelevantPokemon = pokemonCompleteList.index[
    ~pokemonCompleteList.index.isin(pokemon_list.index)] + 1

# ------ Remove unreleveant battles from combats ------
for i in range(0, len(irrelevantPokemon)):
    battle_list = battle_list[
        battle_list.First_pokemon != irrelevantPokemon[i]]
    battle_list = battle_list[
        battle_list.Second_pokemon != irrelevantPokemon[i]]
    battle_list = battle_list[battle_list.Winner != irrelevantPokemon[i]]

print(len(battle_list))
