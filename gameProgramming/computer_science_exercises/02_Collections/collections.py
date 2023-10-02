# Collections Examples, Xavier Oliver, v0.4a

# LIST -- ORDERED, CHANGEABLE, ALLOWS DUPLICATE VALUES
breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk"]
# Each item of the list is known as an ELEMENT.
# The position in the for each is the INDEX.
# The element "BACON" is at index 0.
# Python Only: index -1, it is the last item on the list.
testScores = [95, 100, 25, 15, 27, 35]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

# Printing Contents of a List
#print(breakfastFoods)
#print(testScores)
#print(classGPA)

# Accessing Specific List Elements -- REMEMBER FIRST ELEMENT IS INDEX 0
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])

# Accessing Last Element in Lists
#print(breakfastFoods[-1])
#print(testScores[-1])
#print(classGPA[-1])

# WYOC Access the 3rd Element in Each List
#print(breakfastFoods[2])
#print(testScores[2])
#print(classGPA[2])

# Changing Items in a List
# breakfastFoods[0] = "Sausage"
# testScores[0] = 97
# classGPA[0] = 3.57
# print(breakfastFoods[0])
# print(testScores[0])
# print(classGPA[0])
# print(breakfastFoods)
# print(testScores)
# print(classGPA)

# WYOC Change 5th Element in Each List
# breakfastFoods[4] = "Orange Juice"
# testScores[4] = 50
# classGPA[4] = 4.30
# print(breakfastFoods[4])
# print(testScores[4])
# print(classGPA[4])
# print(breakfastFoods)
# print(testScores)
# print(classGPA)

# Adding and Inserting Items to a List
# .append() adds an item to the END of a list
# breakfastFoods.append("Hash Browns")
# print(breakfastFoods)
# testScores.append(99)
# print(testScores)
# classGPA.append(1.99)
# print(classGPA)

# .insert() allows you to place an item at a specific index in the list.
# breakfastFoods.insert(3, "Parfait")
# print(breakfastFoods)
# testScores.insert(3, 55)
# print(testScores)
# classGPA.insert(3, 0.0)
# print(classGPA)

# WYOC Appending to Lists
# print("APPENDS")
# breakfastFoods.append("Eggs")
# print(breakfastFoods)
# testScores.append(85)
# print(testScores)
# classGPA.append(1.24)
# print(classGPA)

# WYOC Inserting to Index 5
# print("INSERTS")
# breakfastFoods.insert(5, "Omelette")
# print(breakfastFoods)
# testScores.insert(5, 72)
# print(testScores)
# classGPA.insert(5, 1.62)
# print(classGPA)

# Deleting Items from a List
# Use .remove() to remove a specific item from the list.
# breakfastFoods.remove("Waffles")
# print(breakfastFoods)
# testScores.remove(100)
# print(testScores)
# classGPA.remove(2.25)
# print(classGPA)

# To delete using the index value we use .pop()
# breakfastFoods.pop(4)
# print(breakfastFoods)
# testScores.pop(4)
# print(testScores)
# classGPA.pop(4)
# print(classGPA)

# WYOC .pop 2nd element from each list
# print("Removal by Index")
# breakfastFoods.pop(2)
# print(breakfastFoods)
# testScores.pop(2)
# print(testScores)
# classGPA.pop(2)
# print(classGPA)

# WYOC .remove any item from the list
# print("Removal by Item")
# breakfastFoods.remove("Cereal")
# print(breakfastFoods)
# testScores.remove(27)
# print(testScores)
# classGPA.remove(1.99)
# print(classGPA)

# Determining List Length
# print(f"There are {len(breakfastFoods)} items in the breakfastFoods list.")
# print(f"There are {len(testScores)} items in the testScores list.")
# print(f"There are {len(classGPA)} items in the classGPA list.")

# List Methods -- Functions for working with lists. 
# Sorting Lists -- Alphanumerical -- Ascending -- Capital Letters before Lower Case Letters
print(f"The original breakfastFoods list is {breakfastFoods}.")
breakfastFoods.sort()
print(f"The sorted breakfastFoods list is {breakfastFoods}.")

print(f"The original testScores list is {testScores}.")
testScores.sort()
print(f"The sorted testScores list is {testScores}.")

print(f"The original classGPA list is {classGPA}.")
classGPA.sort()
print(f"The sorted classGPA list is {classGPA}.")