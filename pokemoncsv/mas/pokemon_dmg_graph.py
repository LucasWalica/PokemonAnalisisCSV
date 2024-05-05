import csv
import matplotlib.pyplot as plt


# Leer el archivo CSV (hp de pokemon y nombre)
with open('pokemon_csv\pokemon.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)
#Extraer los datos hp y nombre del csv:
Daño_pokemon = [int(row['Sp. Atk']) for row in data]
nombres = [row['Name'] for row in data]
#creamos la grafica 
plt.bar(nombres, Daño_pokemon)
plt.xlabel('Pokemon Name')
plt.ylabel('Damage')
plt.title('Pokemon Sp. Atk')
#Rotar los nombres de los pokemons para evitar supersitciones
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()