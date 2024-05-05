import csv


with open('pokemon_csv\pokemon.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)  # Read the entire CSV data into a list

    attack_column = [int(row['HP']) for row in data]
    name_column = [row['Name'] for row in data]
    indexes = [int(row['#']) for row in data]
      
for index, name, dmg in zip(indexes, name_column, attack_column):
    print(f"Index:{index} Nombre: {name} Daño:{dmg}")


