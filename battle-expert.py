import csv
with open('pokemon.csv', 'rb') as f:
    reader = csv.reader(f)
    pokemon_list = list(reader)

print pokemon_list
