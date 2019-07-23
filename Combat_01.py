#first script for the Hidden_Kingdom combat system
from random import choice, randint, uniform, sample

player_names = ['Lydan', 'Syrin',  'Ptorik',  'Joz',  'Varog', 'Gethrod',  'Hezra', 'Feron', 'Ophni',  'Colborn', 
                'Fintis',  'Gatlin',  'Jinto',  'Hagalbar',  'Krinn',  'Lenox',  'Revvyn',  'Hodus', 'Dimian',
                 'Paskel',  'Kontas',  'Weston',   'Azamarr',  'Jather',  'Tekren',  'Jareth',  'Adon',  'Zaden',]

weapons = ['knife', 'short sword', 'club', 'spear']

armor = ['None', 'old shirt', 'rusty bucket', 'gold chestplate',
        'a pan strapped to the chest']

#I asked a question on stack overflow to prevent duplicates in lists
#I dont quite understand it but it works as needed
player_name1, player_name2 = sample(player_names, 2)

weapon1, weapon2 = sample(weapons, 2)

armor1, armor2 = sample(armor, 2)

Min_damage = 5
Max_damage = 10

Min_health = 50
Max_health = 70

Min_defense = 2
Max_defense = 4

#weapon damage chosen at random based on min and max values for damage
weapon_damage1 = randint(Min_damage, Max_damage)
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
player_1 = {'Name': player_name1, 'Weapon':weapon1, 'Damage': weapon_damage1,
            'Armor': armor1, 'Health' : player_health1}
player_2 = {'Name': player_name2, 'Weapon':weapon2, 'Damage': weapon_damage2,
            'Armor': armor2, 'Health' : player_health2}

#checkes and replaces duplicates in values such as weapon damage
def check_duplicates():
    global weapon_damage1, weapon_damage2
    global Min_damage, Max_damage

    while weapon_damage1 == weapon_damage2:
        weapon_damage2 = randint(Min_damage, Max_damage)
        

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
    check_duplicates()
     
    over_half2 = True
    over_half1 = True
    for i in range(0, 500):
        
        print ('Turn number:', i + 1 )

        if i == 0:
            Max_critical2 = weapon_damage2 * 2
        else:
            Max_critical2 = weapon_damage2 * 1

        #player 1 attacks
        Turn_damage1 = round(weapon_damage1 + uniform(Min_crtical1, Max_critical1)
         - player_defense2)
        Miss_number = randint(1, 10)
        if Miss_number == 5:
            print (player_1['Name'], 'completly missed!')
            print('\n')
        elif Turn_damage1 == 0:
            print (player_2['Name'], ' wasnt even phased!')
            print('\n')
        else:
            player_health2 -= Turn_damage1
            #makes sure health dosent display below 0 and checks if player is dead
            if player_health2 <= 0:
                player_health2 = 0
                print (player_1['Name'], 'just slayed',player_2['Name'], 'for',
                 Turn_damage1 , 'damage!')
                print (player_1['Name'], 'has defeated', player_2['Name'],'!')
                print('\n')
                a = input('\npress any key to exit.')
                break
            elif over_half2 and player_health2 <= player_OgHealth2 / 2 :
                over_half2 = False
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
            print('\n')
        elif Turn_damage2 == 0:
            print (player_1['Name'], 'didnt even flinch!')
            print ('\n')
        else:
            player_health1 -= Turn_damage2
            if player_health1 <= 0:
                player_health1 = 0
                print (player_2['Name'], 'just slayed',player_1['Name'], 'for',
                 Turn_damage2 , 'damage!')
                print (player_2['Name'], 'has defeated', player_1['Name'], '!')
                a = input('\npress any key to exit.')
                break
            elif over_half1 and player_health1 <= player_OgHealth1 / 2 :
                over_half1 = False
                print (player_2['Name'], 'did', Turn_damage2 , 'damage!')
                print (player_1['Name'], 'is under half health!!')
            else:
                #prints outcome of turn
                print (player_2['Name'], 'did', Turn_damage2 , 'damage!')
                print (player_1['Name'], 'is now at', player_health1,'health!')
                print ('\n')
        a = input('press any key to continue.\n')
         
game_start(player_health1,player_health2)