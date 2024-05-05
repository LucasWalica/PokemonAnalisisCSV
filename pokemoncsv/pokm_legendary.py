import csv

# Leer el archivo CSV
with open('pokemoncsv\pokemon.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

Legendary_pokemon = 0
Non_legendary_pokemon = 0

Legendary_list = []
# Count the number of Legendary and Non-Legendary Pokémon
for row in data:
    if row['Legendary'].lower() == 'true':
        Legendary_pokemon += 1
        Legendary_list.append(row)

print("La cantidad de legendarios es ", Legendary_pokemon)
print("La cantidad de no legendarios es ", Non_legendary_pokemon)

for pokemon in Legendary_list:
    print("====>",pokemon['Name'],"<====")
    print("Type 1: ", pokemon['Type 1'] + "      Type 2: ", pokemon['Type 2'] + "\n" +
            "Stats ==> " + "HP:" +  pokemon['HP'] + "   Attack:" + pokemon['Attack'] + "  Sp attack:" + pokemon['Sp. Atk'] + "   Sp Defense:" + pokemon['Sp. Def'] + "  Speed:" + pokemon['Speed'] )
    print("")
    print()



