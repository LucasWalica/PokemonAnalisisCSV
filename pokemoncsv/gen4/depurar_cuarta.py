import csv

with open('pokemoncsv\\cuarta_gen\\cuartaGeneracion_pokemon.csv', 'r', encoding='UTF-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = []
    for row in csv_reader:
        data.append(row)

Grass_pokemon_cuarta = []

for row in data:
    if row['#'] in {'387', '388', '389', '390', '391', '392', '393', '394', '395'}:
        Grass_pokemon_cuarta.append(row)

# Check if the list is not empty before accessing its first element
if Grass_pokemon_cuarta:
    valores = [list(fila.values()) for fila in Grass_pokemon_cuarta]
    indices = Grass_pokemon_cuarta[0].keys()

    with open('Water.csv', 'w', newline='') as csv_file:
        escritor_csv = csv.writer(csv_file)
        escritor_csv.writerow(indices)
        escritor_csv.writerows(valores)
else:
    print("No Grass-type Pokémon found with the specified Pokédex numbers.")
