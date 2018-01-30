import csv

with open('pokemon.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    pokemon_list = list(reader)

print pokemon_list
