import csv

with open('pokemoncsv\gen5\gen_five_pokemon.csv', 'r', encoding='UTF-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = []
    for row in csv_reader:
        data.append(row)

pokemon_tercera = [row for row in data if row['Type 1']=='Electric' or row['Type 2']=='Electric']

# Check if the list is not empty before accessing its first element
if pokemon_tercera:
    valores = [list(fila.values()) for fila in pokemon_tercera]
    indices = pokemon_tercera[0].keys()

    with open('pokemoncsv\gen5\electricos\electricsGen5.csv', 'w', newline='') as csv_file:
        escritor_csv = csv.writer(csv_file)
        escritor_csv.writerow(indices)
        escritor_csv.writerows(valores)
else:
    print("No Electric-type Pokémon found with the specified Pokédex numbers.")