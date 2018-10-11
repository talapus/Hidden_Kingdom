# module imports are placed at the top
from random import randint
from random import choice
from time import sleep

# global variables go below that
primary = 'fists'
secondary = 'none'


# next define global functions. 

def character_name():   #allows player to choose their own name
    global player_name
    player_name = input('\nWhat is your name?')
    
    while True:
        if len(player_name) >= 2 and len(player_name) <= 15:
            print('\nHello ' + player_name + '.')
            break

        else:
            print ('\nYour name must be at least two characters and at most 15. ')
            player_name = input('\nWhat is your name?')
    return player_name

def character_class():  # returns a random word from the list when the function is called
    return choice(['warrior', 'wizard', 'thief', 'cleric', 'ranger', 'paladin', 'death knight', 'monk'])

def character_race():  # is a way to do what we did above without the 'choice' module
    races = ['human', 'elf', 'dwarf', 'halfling', 'gnome', 'kobold', 'halforc', 'halfelf', 'halfogre']
    return races[randint(0,len(races)-1)]  # Explanation: race[0] is 'human', race[1] is 'elf', etc.
                                           # "randint(0,10)" returns a number between one and 10
                                           # "len(races)" returns the length of the races list as a number
                                           # so, "races[randint(0,len(races)-1)]" returns a random list element


# then the main function. 

if __name__ == '__main__':   

    character_name() 

    print ('\nYour Main weaopon is ' + primary + '. And your secondary is ' + secondary)

    # '\n' is a 'newline'. Instead of a separate "print('')" statement, just add \n to your string wherever you want the 
    # new line. I did some of it for you. 
    # For example, if you wanted three newlines after "Hello!", it would be: print("Hello!\n\n\nGoodbye!")

    print('\nYou awake in a room...\nyou find a chest!')
    print('\nThe chest has 4 weapons, 2 main weapons and 2 secondary weapons!')
    print('\nthe 2 main weapons are a great sword and a magic staff...\nthe 2 secondarys are a bow and a bag of fairy dust...')

    chest_item1 = 'great sword'  # variable names should preferably always be lower case. I lowercased your names for you, 
    chest_item2 = 'magic staff'
    chest_item3 = 'bow'
    chest_item4 = 'fairy dust'
    
    primary = input('\nWhat\'s your main weapon? Great sword or magic staff? ')
    primary = primary.lower()

    if  primary == chest_item1 or primary == chest_item2:  
        print ('\nGreat!')  
                          
        secondary = input('What will you hold as a secondary? A bow or fairy dust? ')
        secondary = secondary.lower()

        if secondary == chest_item3 or secondary == chest_item4 :
                print ('\nnice choice!')

        else:
                print ('\nThats not in the chest try again')
                secondary = input('What will you hold as a secondary? A bow or fairy dust? ')

                if secondary == chest_item3 or secondary == chest_item4 :
                    print ('\nnice choice!')

                else:
                    print ('\nYour Greed and stupidity has betrayed you. Now you have nothing.')

    else:
        print ('\nThe chest does not contain these items try again\n')
        primary = input('Whats your main weapon? Great sword or magic staff? ')
        primary = primary.lower()

        if primary == chest_item1 or primary == chest_item2:
            print ('\ngreat')
            secondary = input('What will you hold as a secondary? A bow or fairy dust? ')
            secondary = secondary.lower()

            if secondary == chest_item3 or secondary == chest_item4 :
                print ('\nnice choice!')

            else:
                print ('\nThats not in the chest try again')
                secondary = input('What will you hold as a secondary? A bow or fairy dust? ')
                secondary = secondary.lower()

                if secondary == chest_item3 or secondary == chest_item4 :
                    print ('\nnice choice!')

                else:
                    print ('\nYour Greed and stupidity has betrayed you. Now you have nothing.')
                    primary = 'fists'
                    secondary = 'none'

        else:
            print('\nyour greed and stupidity has betrayed you. Now you have nothing')
            primary = 'fists'
            secondary = 'none'

    print('ok, here we go!')
    sleep(1.5)            # sleeps for 1.5 seconds
    print('\n' * 200)   # prints a newline 200 times
    print ('Your name is ' + player_name)
    print('You are a level {} {} {}'.format(randint(1,10), character_race(), character_class())) 
                                    # python3-style print statements usually utilize the .format idiom
                                    # it is used wherever strings are used, not just print statements
                                    # character_race() and character_class() are function calls
                                                            
    print ('\nyour main weapon is a %s and your secondary is %s' %(primary, secondary) )  # this is the python2 style way, still useful

    print('💀 ☠ 🔥 💪 💰 💡 💣 💥 🌞 🌠') # these are unicode characters. Think these might be useful to display your character?
                                       # visit https://unicode-table.com to peruse the whole unicode character set



# TODO:

# 1. Character names?
# 2. Can we give the character stats like STR, CON, DEX, INT, WIS, CHR, etc? Randomly generate them and print them out?
# 3. Once they have stats, we can generate armor class and hit points. 
# 4. once they have armor class and hit points, we can make them fight monsters or each other, gain xp, items, level up, etc. 