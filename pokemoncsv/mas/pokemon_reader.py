import csv
import matplotlib.pyplot as plt


# Leer el archivo CSV (hp de pokemon y nombre)
with open('pokemoncsv\pokemon.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

#Extraer los datos hp y nombre del csv:
vida_del_pokemon = [int(row['HP']) for row in data]
nombres = [row['Name'] for row in data]


#creamos la grafica 
plt.bar(nombres, vida_del_pokemon)
plt.xlabel('Pokemon Name')
plt.ylabel('Hp')
plt.title('Pokemon hp')


#Rotar los nombres de los pokemons para evitar supersitciones
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
