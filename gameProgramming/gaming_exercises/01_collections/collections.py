# Collections Project, Xavier Oliver, v0.1
playerInventory = []
x1 = 0
while x1 < 10:
    playerInventory.append(input("Please type an item to add to your inventory, then press ENTER. \n"))
    x1 += 1
playerInventory.sort()
print(playerInventory)

