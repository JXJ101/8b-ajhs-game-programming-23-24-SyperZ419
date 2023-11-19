# Example Game Functions Project, Xavier Oliver, v0.3
import random
skillList = ['fireball', 'icebeam', 'thunderbolt','sword slash', 'kamikaze', 'heal', 'guard']
enemyList = ['Goblin', 'Goblin Soldier', 'Goblin Chief', 'Skeleton Knight', 'Haunted Armor', 'Undead Wizard', 'Dragon', 'Hydra']
playerHealth = 150
def generatePlayerStats(): # Generates player stats. No parameters required. Returns the stats list.
    stats = []
    stats.append(random.randint(1, 30)) # Attack
    stats.append(random.randint(1, 30)) # Defense
    stats.append(random.randint(1, 30)) # Speed
    stats.append(random.randint(1, 30)) # Accuracy
    print(stats)
    return stats
    
statsList = generatePlayerStats() # Outputs returned list to a new variable
#print(statsList[1])
def damageCalc(skillUsed, enemyAttackValue, defense = statsList[1]): # Calculates how much damage the player took. Requires the enemy's attack stat, the skill used by the player, and the player's defense value from the previous function.
    damageTaken = enemyAttackValue - defense
    if damageTaken <= 0:
        damageTaken = 0
        print('You took no damage.')
    elif skillUsed == 'guard':
        guardActive = True
        if guardActive == True:
            damageTaken /= 2
        if type(damageTaken) == float:
            damageTaken = round(damageTaken)
            damageTaken = int(damageTaken)
            print(f'Since guard was active, you took {damageTaken} damage.')
    else:
        print(f'You took {damageTaken} damage.')
    return damageTaken # Returns player's health.
    
def enemySelect(): # Chooses a random enemy and amount of enemies. No parameters required.
    i = random.randint(0, len(enemyList) - 1)
    enemyAmount = random.randint(1, 5)
    enemy = enemyList[i]
    if enemyAmount == 1:
        print(f'You encountered {enemyAmount} {enemy}.')
    else:
        print(f'You encountered {enemyAmount} {enemy}s.')
    
        
def playerName(): # Obtains character's name from user input. No parameters. Returns name of character.
    name = input('Name your character.')
    nameConfirm = int(input(f'Your input name is {name}, correct? \nPlease input either yes(1) or no(2).'))
    if nameConfirm == 1:
        print('Character name confirmed.')
    else:
        nameConfirm = input('Please re-input the name of your character.')
        print('Character name confirmed.')
    return name


# def playerTurn(playerCurrentHealth = playerHealth): # Determines if the player can make their turn, then sees what skill they use. Requires player health. Returns skill used.
#     while playerHealth > 0:
#         print(skillList)
#         skill = input('Please select an action from your skill list.').lower
#         if skill in skillList == True:
#             print(f'You used {skill}.')
#             break
#         else:
#             skill = input('Chosen skill not found. Please choose a skill from your skill list.').lower
#             break
#     return skill




playerName()
enemySelect()
skillUsed = playerTurn()
playerDamage = damageCalc(skillUsed, 45)
playerHealth -= playerDamage