import csv 

with open('pokemoncsv\pokemon.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

#Extraer datos numericos  (Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed)
Name = [str(row['Name']) for row in data]
Total = [int(row['Total']) for row in data]
HP = [int(row['HP']) for row in data]
Attack = [int(row['Attack']) for row in data]
Defense = [int(row['Defense']) for row in data]
sp_Attack = [int(row['Sp. Atk']) for row in data]
sp_Defense =[int(row['Sp. Def']) for row in data]
Speed = [int(row['Speed']) for row in data]


#Calcular los valores medios de cara parámetro
Total_media = sum(Total) / len(Total)
HP_media = sum(HP) / len(HP)
Attack_media = sum(Attack) / len(Attack)
Defense_media = sum(Defense) / len(Defense)
sp_attack_media = sum(sp_Attack) / len(sp_Attack)
sp_defense_media = sum(sp_Defense) / len(sp_Defense)
speed_media = sum(Speed) / len(Speed)

#Devolver la media de cara parametro
print("------------------------------")
print("La media de las estadisticas son ==>\n" +
        "------------------------------" +
        f"\nMedia total: {Total_media}" +
        f"\nMedia de HP: {HP_media}" +
        f"\nAttack Media: {Attack_media}" +  
        f"\nDefense Media: {Defense_media}" +
        f"\nSP_Attack Media:{sp_attack_media}" + 
        f"\nSP_Defense Media: {sp_defense_media}" +  
        f"\nSpeed Media: {speed_media}")
print("------------------------------")

# Se quiere ver los mejores pokemons que esten por 
# encima de la media, pudiendo asi decidir que equipo pokemon seria el mas optimo
Total_media_int = int(Total_media)
count = 0
below_average = 0
#Inicializamos una lista vacia
total_above_average = []
for row in data:
    if int(row['Total']) > Total_media_int:
        count += 1
        # Añadimos los datos de los pokemon que estan por encima de la media a la lista anteriormente inicializada
        total_above_average.append(row)    
    else: 
        below_average +=1

print("------------Total------------")
print("pokemons por encima de la media ", count)
print("pokemons por debajo de la media ", below_average)
print("------------------------------")


#Initialize Above average list and above average count
above_average_pokemon = []
above_average_pokemon_count = 0
#HP,Attack,Defense,Sp. Atk,Sp. Def,Speed And non legendary
for row in data:
    if int(row['Generation']) == 1 and int(row['HP']) > HP_media and int(row['Defense']) > Defense_media and int(row['Sp. Atk']) > sp_attack_media and int(row['Sp. Def']) > sp_defense_media and int(row['Speed']) > speed_media:
        above_average_pokemon_count += 1
        above_average_pokemon.append(row)

#Final print
print("Pokemons above averaga ==> \n")
for pokemon in above_average_pokemon:
    print("====>",pokemon['Name'],"<====")
    print("Type 1: ", pokemon['Type 1'] + "      Type 2: ", pokemon['Type 2'] + "\n" +
            "Stats ==> " + "HP:" +  pokemon['HP'] + "   Attack:" + pokemon['Attack'] + "  Sp attack:" + pokemon['Sp. Atk'] + "   Sp Defense:" + pokemon['Sp. Def'] + "  Speed:" + pokemon['Speed'] )
    print("")
print("Above average pokemon count: ", above_average_pokemon_count)    

