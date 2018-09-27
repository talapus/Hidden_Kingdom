# module imports are placed at the top
from random import randint
from random import choice
from time import sleep

# global variables go below that
weapon_1 = 'Fists'
sidearm = 'None'

# next define global functions. 

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

    print ('\nYour Main weaopon is ' + weapon_1 + '. And your sidearm will be ' + sidearm)

    # '\n' is a 'newline'. Instead of a separate "print('')" statement, just add \n to your string wherever you want the 
    # new line. I did some of it for you. 
    # For example, if you wanted three newlines after "Hello!", it would be: print("Hello!\n\n\nGoodbye!")

    print('\nYou awake in a room...\nyou find a chest!')
    print('\nThe chest has 4 weapons, 2 main weapons and 2 sidearms!')
    print('\nthe 2 main weapons are a great sword and a magic staff...\nthe 2 sidearms are a bow and a bag of fairy dust...')

    chest_item1 = 'great sword'  # variable names should preferably always be lower case. I lowercased your names for you, 
    chest_item2 = 'magic staff'
    chest_item3 = 'bow'
    chest_item4 = 'fairy dust'
    
    weapon_1 = input('\nWhat\'s your main weapon? Great sword or magic staff? ')
    weapon_1 = weapon_1.lower()

    if  weapon_1 == chest_item1 or weapon_1 == chest_item2: 
        print('')  # delete this line
        print ('Great!')  # change this to:  print ('\nGreat!')
                          # do the same thing for the others below, then delete these comments
        sidearm = input('What will you hold as a sidearm? A bow or fairy dust? ')
        sidearm = sidearm.lower()

        if sidearm == chest_item3 or sidearm == chest_item4 :
                print ('')
                print ('nice choice!')

        else:
                print ('')
                print ('Thats not in the chest try again')
                sidearm = input('What will you hold as a sidearm? A bow or fairy dust? ')

                if sidearm == chest_item3 or sidearm == chest_item4 :
                    print ('')
                    print ('nice choice!')

                else:
                    print ('')
                    print ('Your Greed and stupidity has betrayed you. Now you have nothing.')

    else:
        print ('\nThe chest does not contain these items try again\n')
        weapon_1 = input('Whats your main weapon? Great sword or magic staff? ')
        weapon_1 = weapon_1.lower()

        if weapon_1 == chest_item1 or weapon_1 == chest_item2:
            print ('\ngreat')
            sidearm = input('What will you hold as a sidearm? A bow or fairy dust? ')
            sidearm = sidearm.lower()

            if sidearm == chest_item3 or sidearm == chest_item4 :
                print ('\nnice choice!')

            else:
                print ('\nThats not in the chest try again')
                sidearm = input('What will you hold as a sidearm? A bow or fairy dust? ')
                sidearm = sidearm.lower()

                if sidearm == chest_item3 or sidearm == chest_item4 :
                    print ('\nnice choice!')

                else:
                    print ('\nYour Greed and stupidity has betrayed you. Now you have nothing.')
                    weapon_1 = 'Fists'
                    sidearm = 'none'

        else:
            print('\nyour greed and stupidity has betrayed you. Now you have nothing')
            weapon_1 = 'Fists'
            sidearm = 'none'

    print('ok, here we go!')
    sleep(1)            # sleeps for 1 second
    print('\n' * 200)   # prints a newline 200 times
    print('You are a level {} {} {}'.format(randint(1,10), character_race(), character_class())) 
                                    # python3-style print statements usually utilize the .format idiom
                                    # it is used wherever strings are used, not just print statements
                                    # character_race() and character_class() are function calls
                                                            
    print ('\nyour main weapon is %s and your sidearm is %s' %(weapon_1, sidearm) )  # this is the python2 style way, still useful
