# Collections Project, Xavier Oliver, v0.2
# Adding Items
playerInventory = []
while len(playerInventory) < 10:
    playerInventory.append(input("Please type an item to add to your inventory, then press ENTER. \n"))
playerInventory.sort()
print(playerInventory)

# Removing Items
while len(playerInventory) > 5:
    playerInventory.remove(input("Please type an item to remove from your inventory, then press ENTER. \n"))
playerInventory.sort()
print(playerInventory)