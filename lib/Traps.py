#=========================
#     Trap List
#=========================
import random

waterTrap = {'name':'Water Trap', 'damage':random.randint(1,4), 'description':'As you enter the room you hear a click. The room begins to fill with water, you scramble to find a way out.'}
pitTrap = {'name':'Pit Fall Trap', 'damage':random.randint(2,5), 'description':'Upon your first step into the room a trap door opens beneath you. You fall into a pit littered with bones.'}
arrowTrap = {'name':'Arrow Trap', 'damage':random.randint(2,7), 'description':'After walking a few steps you trip over something and suddenly realize a barrage of arrows is heading your way.'}
poisonTrap = {'name':'Poison Trap', 'damage':random.randint(3,6), 'description':'The door slams behind you and you begin to smell some sort of odor that in no way can be good for you.'}

trapList = [waterTrap, pitTrap, arrowTrap, poisonTrap]
