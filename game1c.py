
def choice2(Item1, Item2, Item3, Item4, I):
    
        #This function chooses between two new and one existing option
        #The item that is being assigned this option will be Item1
        #The new items that can be selected are Item2 and Item3
        #The existing old value in Item1 is Item4
        #I is just a counter that will assing Item4 to Item1 when I has a value of 2
        #If I starts at 1 then the user has two tries to type in a correct answer.
        
    print("\nWhat's your ",Item1,"? ",Item2," or ",Item3,"?",sep ='')
    I1 = input()
    I1 = I1.lower()

    if  (I1 == Item2 or I1 == Item3 ): 
        print ('\nGreat!')
        
    elif (I == 1):
        print ("That item is not in the chest")
        I1 = choice2 (Item1,Item2,Item3,Item4,I+1)
        
    else:
        if  (I1 == Item2 or I1 == Item3):
            print ('\nGreat!')
        else:
            print("Your Greed and stupidity has betrayed you.  Your ",Item1,"will be ",Item4)
            I1=Item4
    return I1


#main
Weapon_1 = 'Fists'
Sidearm = 'None'

print ('\nYour Main weapon is ' + Weapon_1 + '. And your sidearm will be ' + Sidearm)

print('\nYou awake in a room...\nyou find a chest!')
print ('\nThe chest has 4 weapons, 2 main weapons and 2 sidearms!')
print ('the 2 main weapons are a great sword and a magic staff...')
print ('the 2 sidearms are a bow and a bag of fairy dust...')

chest_Item1 = 'great sword'
chest_Item2 = 'magic staff'
chest_Item3 = 'bow'
chest_Item4 = 'fairy dust'

Weapon_1 = choice2 ("Main weapon",chest_Item1,chest_Item2,Weapon_1,1)
Sidearm = choice2 ("Sidearm",chest_Item3,chest_Item4,Sidearm,1)
       
print ('\n\nyour main weapon is %s and your sidearm is %s' %(Weapon_1,Sidearm) )
a = input("Press any key to exit")
