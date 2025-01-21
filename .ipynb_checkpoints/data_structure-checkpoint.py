import os
os.system('cls' if os.name == 'nt' else 'clear')    #clear the screen

#add a list

shopping_list = []

shopping_list.append("milk")
shopping_list.append("cheese")
shopping_list.append("bread")
shopping_list.remove("milk")

if "eggs" not in shopping_list:
    shopping_list.append("eggs")

print(shopping_list)

if "milk" in shopping_list:
    print("Delicious!")

#================================================================================================

#add a dictionary

foods = {}

foods["banana"] = "A delicious and tasty treat!"
foods["dirt"]   = "Not delicious. Not tasty. DO NOT EAT!"

if "cheese" not in foods:
    foods["cheese"] = "Cheese is one of the known foods!"

del foods["dirt"]

print(foods)

#================================================================================================
#add a list to a dictionary:

ingredients = {}

ingredients["blt sandwich"] = ["bread", "lettuce", "tomato", "bacon"]

print(ingredients)

#================================================================================================
#add dictionaries to a list:

europe = []

europe.append({"name": "Germany", "population": 81000000})
europe.append({"name": "Luxembourg", "population": 512000})

print(europe)
