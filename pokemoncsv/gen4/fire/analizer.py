import csv 
import matplotlib.pyplot as plt 
import numpy as np 

with open('C:/Users/User/Desktop/Work/Programacion/Python/pokemoncsv/gen4/fire/fire4thGen.csv', 'r', encoding='UTF-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = []
    for row in csv_reader:
        data.append(row)

Sp_attack = [float(row['Sp. Atk']) for row in data]
Name = [row['Name'] for row in data]
Hp = [float(row['HP']) for row in data]
Attack = [float(row['Attack']) for row in data]
Speed = [float(row['Defense']) for row in data]

bar_width = 0.2  
index = np.arange(len(Name)) 

plt.bar(index , Sp_attack,width=bar_width ,color='blue')
plt.bar(index+bar_width, Speed, width=bar_width, color='yellow')
plt.bar(index+2*bar_width, Hp, width=bar_width, color='green')
plt.bar(index+3*bar_width, Attack, width=bar_width, color='red')
plt.xticks(index + 1.5 * bar_width, Name)  


plt.xlabel('Pokemon')
plt.ylabel('Values')
plt.title('Fire-type 4th Gen Pokemon')
plt.tight_layout()
plt.legend(loc='upper right', bbox_to_anchor=(1, 1), labels=['Sp_attack', 'Speed', 'Hp', 'Attack'])
plt.show()