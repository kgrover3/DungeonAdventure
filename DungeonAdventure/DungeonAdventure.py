#RPG Again
import random
import time
import Weapons


#Game Variables
playing = False
goldCollected = 50
MINGOLD = 0 #Keeps gold from going negative#
WINGOLD = 100000 #End Game Goal#
roomType = '' #Stores good or bad room type#
direction = '' #Player chosen direction#

#Player Constants
MAXPLAYERHP = 100 #Players Max health#
MAXPLAYERMP = 50  #Players Max Magic#

#Player Variables
name = ""
playerHP = 100
playerMP = 50
weapon = 'Empty'
armor = 'Empty'
maxDamage = 5
minDamage = 0
armorRate = 0
healthItem = 2

#Monster Variables
monsterName = ''
monsterHP = 0

monsterAtkName1 = ''
monsterAtk1Min = 0
monsterAtk1Max = 0



#Functions

def getName(name):
    name = input("Please enter your name: ")
    return name



#Main Game Loop

name = getName(name);
print('hello ' + name + ' are you ready to play?')
randWep = random.choice(Weapons.weaponList)
print (randWep)






