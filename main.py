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
BASEMAXDAMAGE = 5
BASEMINDAMAGE = 0
BASEARMORRATE = 0

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

def getWeapon(weapon, minDamage, maxDamage):
    randomWeapon = random.choice(wepList)
    atkRate = (randomWeapon['damage'])
    if atkRate <= minDamage:
        print('You find a ' + randomWeapon['name'] + ' while searching the room')
        time.sleep(1)
        print('This weapon is no better than the one you have. You toss it to the side')
        time.sleep(1)
    else:
        weapon = (randomWeapon['name'])
        time.sleep(1)
        print('You pick up a ' + weapon + '.')
        time.sleep(1)
        print(randomWeapon['description'])
        minDamage = BASEMINDAMAGE + atkRate
        maxDamage = BASEMAXDAMAGE + atkRate
    return weapon, minDamage, maxDamage

def getArmor(armor, armorRate):
    randomArmor = random.choice(armList)
    armRate = (randomArmor['arm'])
    time.sleep(1)
    print('You find some ' + randomArmor['name'] + ' lying on the floor.')
    time.sleep(1)
    if areRate <= armorRate:
        print('Upon inspection you realize that this armor is no better than what you are currently wearing.')
        time.sleep(1)
        print('You kick a piece of the armor into the corner.')
    else:
        armor = (randomArmor['name'])
        print('You don the ' + armor + ' you found.')
        armorRate = BASEARMORRATE + armRate
    return armor,armorRate

def getHeal(healthItem):
    healthItem = healthItem + 1
    time.sleep(1)
    print('You have found a healing potion to heal yourself with. You put this item in your pack.')
    return healthItem

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

def goodRoom():
    time.sleep()
    print('This is a seemingly quiet room and you decide to look around and rest.')
    autoHeal = random.randint(1,100)
    if autoHeal <= 10:
        healHP = random.randint(10,50)
        playerHP = playerHP + healHP
        maxHealth(playerHP, MAXPLAYERHP)
        time.sleep(1)
        print('In this calm peaceful place you are magically healed. You recover ' + str(healHP) + ' from this magic.')
        
    randomWeapon = random.randint(1,100)
    if randomWeapon <= 12:
        time.sleep(1)
        print('You have found a weapon to arm yourself with.')
        weapon,minDamage,maxDamage = getWeapon(weapon,minDamage,maxDamage)

    randomArmor = random.randint(1,100)
    if randomArmor <= 12:
        time.sleep(1)
        print('You have found some armor to help shield you on your journey.')
        armor,armorRate = getArmor(armor,armorRate)

    randomMed = random.randint(1,100)
    if randomMed <= 10:
        healthItem = getHeal(healthItem)

    randomGold = random.randint(1,100)
    if randomGold <= 7:
        goldAmount = random.randint(10,100)
        goldCollected = goldCollected + goldAmount
        time.sleep(1)
        print('You have found ' + str(goldAmount) + ' gold while searching this room.')

    healForGold = random.randint(1,100)
    if healForGold <= 20:
        print('You find a divine offering fountain.')
        time.sleep(1)
        print('By offering gold to the gods you have a chance to heal yourself.')
        time.sleep(1)
        print('The gods demand an offering of 5 gold pieces for every health point restored')
        time.sleep(1)
        print('Your current stats are...")
        time.sleep(1)
        stats()
        time.sleep(1)
        hp = input('How many HP would you like to restore?')
        if goldCollected < 5*int(hp):
              print('You do not have enough gold to do this.')
              time.sleep(1)
              print('You have angered the gods for trying to be deceitful... They will punish you by taking 10 gold and 5 HP from you.')
              goldCollected = goldCollected - 10
              if goldCollected < MINGOLD:
                  goldCollected = MINGOLD
              playerHP = playerHP - 5
        else:
            playerHP = playerHP + int(hp)
            goldCollected = goldCollected - 5*int(hp)
            playerHP = maxHealth(playerHP, MAXPLAYERHP)





def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def resetGame():
    print('Time to begin your journey..... again')
    time.sleep(1)
    goldCollected = 50
    playerHP = 100
    playerMP = 50
    weapon = 'Empty'
    armor = 'Empty'
    maxDamage = 5
    minDamage = 0
    armorRate = 0
    healthItem = 2
    playing = True

#========================
#     Main Game Loop
#========================
intro()
time.sleep(1)

name = getName(name)

playing = True
while playing:
    if health <= 0:
        print('You have died in the dungeon')
        time.sleep(1)
        if playagain():
            resetGame()
        else:
            print('GoodBye')
            time.sleep(2)
            break

        navigation()
        stats()
        getRoom()
        if roomType = 'good':
            





