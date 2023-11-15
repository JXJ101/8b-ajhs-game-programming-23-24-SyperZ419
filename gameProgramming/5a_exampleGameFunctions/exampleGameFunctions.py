# Example Game Functions Project, Xavier Oliver, v0.1
import random
movelist = ['Fireball', 'Ice Beam', 'Thunderbolt','Sword Slash', 'Kamikaze', 'Heal', 'Guard']
enemyList = ['Goblin', 'Goblin Soldier', 'Goblin Chief', 'Skeleton Knight', 'Haunted Armor', 'Undead Wizard', 'Dragon', 'Hydra']
def generateStats():
    stats = []
    stats.append(random.randint(1, 30))
    stats.append(random.randint(1, 30))
    stats.append(random.randint(1, 30))
    stats.append(random.randint(1, 30))
    print(stats)
    return stats
    
def functionTwo(param1):
    pass

statsList = generateStats()
print(statsList[1])
def damageCalc(skillUsed, enemyAttackValue, defense = statsList[1]):
    damageTaken = enemyAttackValue - defense
    if skillUsed == 'Guard':
        damageTaken = damageTaken/2
        print(f'Since guard was active, you took {damageTaken} damage.')
        if damageTaken < 0:
            damageTaken = 0
        elif .5 in damageTaken:
            damageTaken = damageTaken.round(>0.5)
    else:
        print(f'You took {damageTaken} damage.')
    return damageTaken
    

def fuctionFour(param1, param2, param3):
    pass



damageCalc('Guard', 24)