# Collections Project, Xavier Oliver, v0.1
# Adding Items
playerInventory = []
while len(playerInventory) < 10:
    playerInventory.append(input("Please type an item to add to your inventory, then press ENTER. \n"))
playerInventory.sort()
print(playerInventory)

