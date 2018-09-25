
Weapon_1 = 'Fists'
Sidearm = 'None'

print('')

print ('Your Main weaopon is ' + Weapon_1 + '. And your sidearm will be ' + Sidearm)

print('')

print('You awake in a room...')
print('')
print ('you find a chest!')
print('')
print ('The chest has 4 weapons, 2 main weapons and 2 sidearms!')
print('')
print ('the 2 main weapons are a great sword and a magic staff...')
print('')
print ('the 2 sidearms are a bow and a bag of fairy dust...')

chest_Item1 = 'great sword'
chest_Item2 = 'magic staff'
chest_Item3 = 'bow'
chest_Item4 = 'fairy dust'



print('') 
Weapon_1 = input('Whats your main weapon? Great sword or magic staff? ')
Weapon_1 = Weapon_1.lower()

if  Weapon_1 == chest_Item1 or Weapon_1 == chest_Item2: 
    print('')
    print ('Great!')
    Sidearm = input('What will you hold as a sidearm? A bow or fairy dust? ')
    Sidearm = Sidearm.lower()

    if Sidearm == chest_Item3 or Sidearm == chest_Item4 :
            print ('')
            print ('nice choice!')
    
            
    else:
            print ('')
            print ('Thats not in the chest try again')
            Sidearm = input('What will you hold as a sidearm? A bow or fairy dust? ')
            
            if Sidearm == chest_Item3 or Sidearm == chest_Item4 :
                print ('')
                print ('nice choice!')
    
            
            else:
                print ('')
                print ('Your Greed and stupidity has betrayed you. Now you have nothing.')

else:
    print('')
    print ('The chest does not contain these items try again')
    print('')
    Weapon_1 = input('Whats your main weapon? Great sword or magic staff? ')
    Weapon_1 = Weapon_1.lower()

    
    if Weapon_1 == chest_Item1 or Weapon_1 == chest_Item2:
        print('')
        print ('great')
        Sidearm = input('What will you hold as a sidearm? A bow or fairy dust? ')
        Sidearm = Sidearm.lower()

        if Sidearm == chest_Item3 or Sidearm == chest_Item4 :
            print ('')
            print ('nice choice!')
    
            
        else:
            print ('')
            print ('Thats not in the chest try again')
            Sidearm = input('What will you hold as a sidearm? A bow or fairy dust? ')
            Sidearm = Sidearm.lower()
            
            if Sidearm == chest_Item3 or Sidearm == chest_Item4 :
                print ('')
                print ('nice choice!')
    
            
            else:
                print ('')
                print ('Your Greed and stupidity has betrayed you. Now you have nothing.')
                Weapon_1 = 'Fists'
                Sidearm = 'none'


    else:
        print('')
        print('your greed and stupidity has betrayed you. Now you have nothing')
        Weapon_1 = 'Fists'
        Sidearm = 'none'

print ('')
print ('your main weapon is %s and your sidearm is %s' %(Weapon_1,Sidearm) )