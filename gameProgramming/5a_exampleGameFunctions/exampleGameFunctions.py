# Example Game Functions Project, Xavier Oliver, v0.1
import random
movelist = ['Fireball', 'Ice Beam', 'Thunderbolt','Sword Slash', 'Kamikaze', 'Heal', 'Guard']
enemyList = ['Goblin', 'Goblin Soldier', 'Goblin Chief', 'Skeleton Knight', 'Haunted Armor', 'Undead Wizard', 'Dragon', 'Hydra']
def generateStats():
    i = 0
    while i < 4:
        strengthValue = random.randint(1, 30)
        speedValue = random.randint(1, 30)
        defenseValue = random.randint(1, 30)
        accuracyValue = random.randint(1, 30)
        if i == 0:
            print(f'Strength: {strengthValue}')
            i += 1
        elif i == 1:
            print(f'Speed: {speedValue}')
            i += 1
        elif i == 2:
            print(f'Defense: {defenseValue}')
            i += 1
        elif i == 3:
            print(f'Accuracy: {accuracyValue}')
            i += 1
        else:
            break
    return strengthValue, speedValue, defenseValue, accuracyValue
    
def functionTwo(param1):
    pass

def manaAmountCalc(manaCost, maxMana = 100):
    pass

def fuctionFour(param1, param2, param3):
    pass

generateStats()
