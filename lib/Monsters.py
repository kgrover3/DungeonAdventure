#=========================
#     Monster List
#=========================
import random
#=====Weak monsters=====

slug = {'name':'Slug', 'mHP':random.randint(25,40), 'mAtkName1':'Slime', 'mAtk1Min':1, 'mAtk1Max':3}
skeletalRemains = {'name':'Skeletal Remains', 'mHP':random.randint(30,60), 'mAtkName1':'Bone Bash', 'mAtk1Min':2, 'mAtk1Max':5}
giantRat = {'name':'Giant Rat', 'mHP':random.randint(25,45), 'mAtkName1':'Bite', 'mAtk1Min':2, 'mAtk1Max':4}
moaningSpector = {'name':'Moaning Spector', 'mHP':random.randint(25,50), 'mAtkName1':'Deafening Howl', 'mAtk1Min':3, 'mAtk1Max':5}
youngTroll = {'name':'Young Troll', 'mHP':random.randint(40,60), 'mAtkName1':'Pummel', 'mAtk1Min':3, 'mAtk1Max':7}
smellyOrk = {'name':'Smelly Ork', 'mHP':random.randint(35,55), 'mAtkName1':'strike', 'mAtk1Min':3, 'mAtk1Max':6}

weakEnemyList = [slug, skeletalRemains, giantRat, moaningSpector, youngTroll, smellyOrk]


#=====Strong monsters=====

skeletalWarrior = {'name':'Skeletal Warrior', 'mHP':random.randint(35,65), 'mAtkName1':'Skull Crush', 'mAtk1Min':6, 'mAtk1Max':10}
babyDragon = {'name':'Baby Dragon', 'mHP':random.randint(50,75), 'mAtkName1':'Fiery Sneeze', 'mAtk1Min':7, 'mAtk1Max':12}
darkPhantom = {'name':'Dark Phantom', 'mHP':random.randint(65,90), 'mAtkName1':'Bleeding Shriek', 'mAtk1Min':9, 'mAtk1Max':12}
giantTrollBrute = {'name':'Giant Troll Brute', 'mHP':random.randint(75,95), 'mAtkName1':'Club Smash', 'mAtk1Min':10, 'mAtk1Max':14}
orkWarrior = {'name':'Ork Warrior', 'mHP':random.randint(80,100), 'mAtkName1':'Heavy Slash', 'mAtk1Min':12, 'mAtk1Max':17}

strongEnemyList = [skeletalWarrior, babyDragon, darkPhantom, giantTrollBrute, orkWarrior]


#=====Epic monsters=====

iceDragon = {'name':'Ice Dragon', 'mHP':random.randint(100,150), 'mAtkName1':'Icy Blast', 'mAtk1Min':12, 'mAtk1Max':18}
fireDragon = {'name':'Fire Dragon', 'mHP':random.randint(100,150), 'mAtkName1':'Burning Breath', 'mAtk1Min':12, 'mAtk1Max':18}
blackDragon = {'name':'Black Dragon', 'mHP':random.randint(150,200), 'mAtkName1':'Demons Wind', 'mAtk1Min':15, 'mAtk1Max':20}

epicEnemyList = [iceDragon, fireDragon, blackDragon]
