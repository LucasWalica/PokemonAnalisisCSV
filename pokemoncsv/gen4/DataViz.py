import csv 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import re 

with open('pokemoncsv\cuarta_gen\cuartaGeneracion_pokemon.csv', 'r', encoding='UTF-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = []
    patron = re.compile(r'.*?Mega')
    for row in csv_reader:
        if (str(row['Type 1']) == "Fighting" or str(row['Type 1']) == "Psychic" or str(row['Type 2']) == "Fighting" or str(row['Type 2'])== "Psychic") and not patron.search(str(row['Name'])):
            data.append(row)
        
Sp_attack = [float(row['Sp. Atk']) for row in data]
Name = [row['Name'] for row in data]
Hp = [float(row['HP']) for row in data]
Attack = [float(row['Attack']) for row in data]
Def = [float(row['Defense']) for row in data]
Spdef = [float(row['Sp. Def']) for row in data]
Speed = [float(row['Speed']) for row in data]
bar_width = 0.1  
index = np.arange(len(Name)) 


datos = pd.read_csv('pokemoncsv\cuarta_gen\cuartaGeneracion_pokemon.csv')
print(datos)

plt.bar(index , Sp_attack,width=bar_width ,color='blue')
plt.bar(index+bar_width, Def, width=bar_width, color='yellow')
plt.bar(index+2*bar_width, Hp, width=bar_width, color='green')
plt.bar(index+3*bar_width, Attack, width=bar_width, color='red')
plt.bar(index+4*bar_width, Spdef, width=bar_width, color='violet')
plt.bar(index+5*bar_width, Speed, width=bar_width, color='pink')
plt.xticks(index + 1.5 * bar_width, Name)  

plt.xlabel('Pokemon')
plt.ylabel('Values')
plt.title('Data visualization Pokemon')
plt.tight_layout()
plt.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=5 ,labels=['Sp_attack', 'Def', 'Hp', 'Attack', 'Spdef', 'Speed'])
plt.show()