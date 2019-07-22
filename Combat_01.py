from random import choice
from random import randint
from random import random
from random import uniform

player_names = ['Lydan', 'Syrin',  'Ptorik',  'Joz',  'Varog', 'Gethrod',  'Hezra', 'Feron', 'Ophni',  'Colborn', 
                'Fintis',  'Gatlin',  'Jinto',  'Hagalbar',  'Krinn',  'Lenox',  'Revvyn',  'Hodus', 'Dimian',
                 'Paskel',  'Kontas',  'Weston',   'Azamarr',  'Jather',  'Tekren',  'Jareth',  'Adon',  'Zaden',]

weapon = ['knife', 'short sword', 'club', 'spear']

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
player_1 = {'Name':choice(player_names), 'Weapon':choice(weapon), 'Weapon damage': weapon_damage1, 'Armor': choice(armor),
        'Health' : player_health1}
player_2 = {'Name':choice(player_names), 'Weapon':choice(weapon), 'Weapon damage': weapon_damage2, 'Armor': choice(armor), 
        'Health' : player_health2}


def player_start():
    for key, value in player_1.items():
        print (key, ':', value)
    print ('\n')
    for key, value in player_2.items():
        print (key, ':', value)
    print ('\n')

def game_start():
    for i in range (0, 500):
        global player_health1, player_health2
        global Min_crtical1, Min_crtical2, Max_critical1, Max_critical2
        
        i += 1
        print ('Turn number: ', i )

        if i == 1:
            Max_critical2 = weapon_damage2 * 2
        else:
            Max_critical2 = weapon_damage2 * 1

        #player 1 deals damage
        round_damage1 = round(weapon_damage1 + uniform(Min_crtical1, Max_critical1)
         - player_defense2)
        if round_damage1 == 0:
            print (player_2['Name'], ' wasnt even phased!')
        else:
            player_health2 -= round_damage1
            #makes sure health dosent display below 0
            if player_health2 < 0:
                player_health2 = 0
            #prints outcome of first turn
            print (player_1['Name'], 'did', round_damage1 , 'damage!')
            print (player_2['Name'], 'is now at', player_health2,'health!')
            print ('\n')
        #checks to see if player 2 is dead
        if player_health2 == 0:
            print (player_1['Name'], 'has won!')
            a = input('\npress any key to exit.')
            break
        a = input('press any key to continue.\n')
            
        # player 2 attacks
        round_damage2 = round(weapon_damage2 + uniform(Min_crtical2, Max_critical2) 
        - player_defense1)
        if round_damage2 == 0:
            print (player_1['Name'], 'didnt even flinch!')
        else:
            player_health1 -= round_damage2

            if player_health1 < 0:
                player_health1 = 0
            #displays outcome
            print (player_2['Name'], 'did', round_damage2 , 'damage!')
            print (player_1['Name'], 'is now at', player_health1,'health!')
            print ('\n')
        #checks to see if player 1 is dead
        if player_health1 == 0:
            print (player_2['Name'], 'has won!')
            a = ('press any key to exit.')
            break
        a = input('press any key to continue.\n')
         
player_start()
game_start()