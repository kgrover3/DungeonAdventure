#**********************************************************************************************************************************************************#
#===========================
#===========================                  Dungeon Adventure 
#===========================
#**********************************************************************************************************************************************************#
#
#**********************************************************************************************************************************************************#
#===========================                Code and Design by
#===========================                  Kenneth Grover
#===========================                    02-04-2018
#**********************************************************************************************************************************************************#


#=======================
#    Required Imports
#=======================
import sys
import random
import time
import lib.Weapons
import lib.Armor
import lib.Rooms
import lib.Traps
import lib.Monsters

#=======================
#Data Location Variables
#=======================
wepList = lib.Weapons.weaponList
armList = lib.Armor.armorList
rmList = lib.Rooms.roomList
trpList = lib.Traps.trapList
monList = lib.Monsters


#=======================
# Variables & Constants
#=======================

#===Game Variables===
playing = False
goldCollected = 50
MINGOLD = 0 #Keeps gold from going negative#
WINGOLD = 100000 #End Game Goal#
roomType = '' #Stores good or bad room type#
trap = {}
direction = '' #Player chosen direction#
roomType = '' #Stores Good or Bad Room

#===Player Constants===
MAXPLAYERHP = 100 #Players Max health#
MAXPLAYERMP = 50  #Players Max Magic#

#===Player Variables===
name = ""
playerHP = 100
playerMP = 50
weapon = 'Empty'
armor = 'Empty'
maxDamage = 5
minDamage = 0
armorRate = 0
healthItem = 2

#===Monster Variables===
monsterName = ''
monsterHP = 0

monsterAtkName1 = ''
monsterAtk1Min = 0
monsterAtk1Max = 0


#========================
#     Functions
#========================

def intro():
    print('Welcome to Dungeon Adventure')
    time.sleep(1)
    print('You must collect 100,000 gold pieces or remain in the dungeon for all eternity')
    time.sleep(1)
    print('It will not be easy.....')

def getName(name):
    name = input('What is your name adventurer?')
    time.sleep(1)
    print('Let your quest begin ' + name)
    time.sleep(1)
    return name

def stats():
    print()
    print(name + ' Health: ' + str(playerHP) + '/' + str(MAXPLAYERHP) + ' Gold: ' + str(goldCollected) + ' Armor: ' + armor + ' Weapon: ' + weapon + ' Healing Potions: ' + str(healthItem))
    
def maxHealth(playerHP, MAXPLAYERHP):
    if playerHP > MAXPLAYERHP:
        playerHP = MAXPLAYERHP
    return playerHP

def useHealItem(healthItem):
    healthItem = healthItem - 1
    return healthItem

def healFromItem(playerHP, MAXPLAYERHP):
    addHP = random.randint(25,50)
    playerHP = playerHP + addHP
    maxHealth(playerHP, MAXPLAYERHP)
    print('You drink the strange potion and feel a weird swirling inside you. You recover ' + str(addHP) + ' HP.')
    return playerHP

def navigation():
    dir = input('Choose a direction: ')
    if dir not in '8246':
        time.sleep(1)
        print('Not a valid direction. Choose a direction: ')
    else:
        randomRoom = random.choice(rmList)
        time.sleep(1)
        print (randomRoom['description'])
        time.sleep(1)
        return randomRoom

def trap(trap):
    randomTrap = random.choice(trpList)
    time.sleep(1)
    print (randomTrap['description'])
    time.sleep(1)
    return randomTrap

def trapDodge(trap, playerHP):
    dodge = random.randint(1,100)
    if dodge <34:
        time.sleep(1)
        print('You have managed to dodge the trap')
    else:
        playerHP = playerHP - trap['damage']
        time.sleep(1)
        print('You take ' + trap['damage'] + ' from getting caught in the trap')
    return playerHP

def getRoom(roomType):
    # Good Room: 25% 1-25
    # Bad Room: 75% 26-100
    roomNum = random.randint(1,100)
    if roomNum <26:
        roomType = 'good'

    else:
        roomType = 'bad'
    return roomType

#========================
#     Main Game Loop
#========================
intro()
name = getName(name)
playing = True
while playing:
    navigation()






