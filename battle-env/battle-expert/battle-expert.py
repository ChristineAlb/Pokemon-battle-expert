import numpy
import pandas
import os

# Import pokemon data
dir = os.path.dirname(__file__)
pokemon_list = os.path.join(dir, 'datasheet/pokemon.csv')
pokemon_list = pandas.read_csv(pokemon_list)

print pokemon_list
