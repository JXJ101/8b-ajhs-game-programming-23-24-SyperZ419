# Example Game Functions Project, Xavier Oliver, v0.2
import random
movelist = ['Fireball', 'Ice Beam', 'Thunderbolt','Sword Slash', 'Kamikaze', 'Heal', 'Guard']
enemyList = ['Goblin', 'Goblin Soldier', 'Goblin Chief', 'Skeleton Knight', 'Haunted Armor', 'Undead Wizard', 'Dragon', 'Hydra']
def generateStats(): # Generates player stats. No parameters required. Returns the stats list.
    stats = []
    stats.append(random.randint(1, 30)) # Attack
    stats.append(random.randint(1, 30)) # Defense
    stats.append(random.randint(1, 30)) # Speed
    stats.append(random.randint(1, 30)) # Accuracy
    print(stats)
    return stats
    
statsList = generateStats() # Outputs returned list to a new variable
#print(statsList[1])
def damageCalc(skillUsed, enemyAttackValue, defense = statsList[1]): # Calculates how much damage the player took. Requires the enemy's attack stat, the skill used by the player, and the player's defense value from the previous function.
    damageTaken = enemyAttackValue - defense
    if damageTaken <= 0:
        damageTaken = 0
        print('You took no damage.')
    elif skillUsed == 'Guard':
        guardActive = True
        if guardActive == True:
            damageTaken = damageTaken/2
        if type(damageTaken) == float:
            damageTaken = round(damageTaken)
            damageTaken = int(damageTaken)
            print(f'Since guard was active, you took {damageTaken} damage.')
    else:
        print(f'You took {damageTaken} damage.')
    return damageTaken
    
def enemySelect():
    for x in range(len(enemyList)):
        



def fuctionFour(param1, param2, param3):
    pass


#damageCalc('Guard', 56)
enemySelect()
