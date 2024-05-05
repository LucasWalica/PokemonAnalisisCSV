import csv 
import pandas as pd
import matplotlib.pyplot as plt  
import numpy as np 

with open('pokemoncsv\cuarta_gen\cuartaGeneracion_pokemon.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

#datos
Name = [row['Name'] for row in data]
Hp = [float(row['HP']) for row in data]
Attack = [float(row['Attack']) for row in data]
Def = [float(row['Defense']) for row in data]
Sp_attack = [float(row['Sp. Atk']) for row in data]
Spdef = [float(row['Sp. Def']) for row in data]
Speed = [float(row['Speed']) for row in data]

#medias
medianHp = sum(Hp)/len(Hp)
medianAttack = sum(Attack)/len(Attack)
medianDef = sum(Def)/len(Def)
medianSpAttack = sum(Sp_attack)/len(Sp_attack)
medianSpDef = sum(Spdef)/len(Spdef)
medianSpeed = sum(Speed)/len(Speed)


df = pd.read_csv('pokemoncsv\cuarta_gen\cuartaGeneracion_pokemon.csv')

print("\n Good tanks => ")
Tanks_df = df[(df['HP'] > medianHp) & (df['Defense']>medianDef) & (df['Sp. Def'] >medianSpDef) & (df['Legendary']==False)]
print(Tanks_df)

print("\n Phisical DMG => ")
phisicalDmg_df = df[(df['Attack'] > medianAttack*1.5) & (df['Speed'] > medianSpeed) & (df['Legendary']==False)]
print(phisicalDmg_df)