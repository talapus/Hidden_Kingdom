#first script for the Hidden_Kingdom combat system
from random import choice
from random import randint
from random import random
from random import uniform

player_names = ['Lydan', 'Syrin',  'Ptorik',  'Joz',  'Varog', 'Gethrod',  'Hezra', 'Feron', 'Ophni',  'Colborn', 
                'Fintis',  'Gatlin',  'Jinto',  'Hagalbar',  'Krinn',  'Lenox',  'Revvyn',  'Hodus', 'Dimian',
                 'Paskel',  'Kontas',  'Weston',   'Azamarr',  'Jather',  'Tekren',  'Jareth',  'Adon',  'Zaden',]

weapons = ['knife', 'short sword', 'club', 'spear']

armor = ['None', 'old shirt', 'rusty bucket', 'gold chestplate', 'a rock strapped to the chest']

Min_damage = 5
Max_damage = 15

Min_health = 75
Max_health = 100

Min_defense = 3
Max_defense = 5

weapon_damage1 = randint(Min_damage, Max_damage)
weapon_damage2 = randint(Min_damage, Max_damage)

while weapon_damage1 == weapon_damage2:
    weapon_damage2 = randint(Min_damage, Max_damage)


#defines critical hits
Min_crtical1 = 0
Max_critical1 = weapon_damage1 * 1

Min_crtical2 = 0
Max_critical2 = weapon_damage2 * 1

#defines players health
player_health1 = randint(Min_health, Max_health)
player_health2 = randint(Min_health, Max_health)

#defines player defense
player_defense1 = randint(Min_defense, Max_defense)
player_defense2 = randint(Min_defense, Max_defense)

#players stats
player_1 = {'Name':choice(player_names), 'Weapon':choice(weapons), 'Damage': weapon_damage1,
            'Armor': choice(armor), 'Health' : player_health1}
player_2 = {'Name':choice(player_names), 'Weapon':choice(weapons), 'Damage': weapon_damage2,
            'Armor': choice(armor), 'Health' : player_health2}


def player_start():
    print ('\n')
    for key, value in player_1.items():
        print (key, ':', value)
    print ('\n')
    for key, value in player_2.items():
        print (key, ':', value)
    print ('\n')

def game_start(player_OgHealth1, player_OgHealth2):
    global player_health1, player_health2
    global Min_crtical1, Min_crtical2, Max_critical1, Max_critical2

    player_start()
    # used for checking the half health if statments I dont know or dont remember if there is a way 
    # to add all these in the for loop alongside i 
    s = 0
    z = 0
    for i in range(0, 500):
        
        i += 1
        print ('Turn number: ', i )

        if i == 1:
            Max_critical2 = weapon_damage2 * 2
        else:
            Max_critical2 = weapon_damage2 * 1

        #player 1 deals damage
        Turn_damage1 = round(weapon_damage1 + uniform(Min_crtical1, Max_critical1)
         - player_defense2)
        Miss_number = randint(1, 10)
        if Miss_number == 5:
            print (player_1['Name'], 'completly missed!')
        elif Turn_damage1 == 0:
            print (player_2['Name'], ' wasnt even phased!')
        else:
            player_health2 -= Turn_damage1
            #makes sure health dosent display below 0 and checks if player is dead
            if player_health2 <= 0:
                player_health2 = 0
                print (player_1['Name'], 'just slayed',player_2['Name'], 'for',
                 Turn_damage1 , 'damage!')
                print (player_1['Name'], 'has defeated', player_2['Name'],'!')
                a = input('\npress any key to exit.')
                break
            elif s == 0 and player_health2 <= player_OgHealth2 / 2 :
                s += 1
                print (player_1['Name'], 'did', Turn_damage1 , 'damage!')
                print (player_2['Name'], 'is under half health!!')
            else:
                #prints outcome of turn
                print (player_1['Name'], 'did', Turn_damage1 , 'damage!')
                print (player_2['Name'], 'is now at', player_health2,'health!')
                print ('\n')
        a = input('press any key to continue.\n')
            
        # player 2 attacks
        Turn_damage2 = round(weapon_damage2 + uniform(Min_crtical2, Max_critical2) 
        - player_defense1)
        Miss_number = randint(1, 10)
        if Miss_number == 5:
            print ('The sun was in', player_2['Name'], 'eyes.')
        elif Turn_damage2 == 0:
            print (player_1['Name'], 'didnt even flinch!')
        else:
            player_health1 -= Turn_damage2
            if player_health1 <= 0:
                player_health1 = 0
                print (player_2['Name'], 'just slayed',player_1['Name'], 'for',
                 Turn_damage2 , 'damage!')
                print (player_2['Name'], 'has defeated', player_1['Name'], '!')
                a = input('\npress any key to exit.')
                break
            elif z==0 and player_health1 <= player_OgHealth1 / 2 :
                z += 1
                print (player_2['Name'], 'did', Turn_damage2 , 'damage!')
                print (player_1['Name'], 'is under half health!!')
            else:
                #prints outcome of turn
                print (player_2['Name'], 'did', Turn_damage2 , 'damage!')
                print (player_1['Name'], 'is now at', player_health1,'health!')
                print ('\n')
        a = input('press any key to continue.\n')
         
game_start(player_health1,player_health2)