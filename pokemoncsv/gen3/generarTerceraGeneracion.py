import csv

try:
    # Read the original CSV file
    with open('pokemoncsv/pokemon.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header
        rows = [row for row in reader]

    # Filter out the Pokémon from the third generation
    gen_three_pokemon = [row for row in rows if int(row[11]) == 6]


    filePath = "pokemoncsv/gen6/gen_six_pokemon.csv"
    # Write the filtered data to a new CSV file
    with open(filePath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Write the header
        writer.writerows(gen_three_pokemon)
        
    print("New CSV file created successfully.")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
