from pprint import pprint
import os
os.system('cls' if os.name == 'nt' else 'clear')    #clear the screen

#================================================================================================

#list
#use the backslash to break a long line of code into multiple lines.
supplies = \
'''pens
staplers
flamethrowers
binders'''.split('\n') #split() method returns a list of strings after breaking the given string by the specified separator. While join() method returns a string concatenated with the elements of an iterable.
supplies.append('pencils') if 'pencils' not in supplies else None
supplies.remove('flamethrowers') if 'flamethrowers' in supplies else None
for index, item in enumerate(supplies): #enumerate() function returns two values: the index of the item in the list, and the item in the list itself.
    #print(f"Index {index} in supplies is: {item}")
    print(("Index " + str(index) + " in supplies is").ljust(23) + item.rjust(10, "."))
print()

#================================================================================================

#dictionary
picnicItems = {'apples': 5, 'cups': 2}
print(f"I am bringing {picnicItems.get('cups', 0)} cups.") #if the key is in the dictionary, the get() method returns the value associated with that key.
print(f"I am bringing {picnicItems.get('pies', 0)} pies.") #if the key is not in the dictionary, the get() method returns the default value, 0.
print()

#another way to access the value of a key in a dictionary:
#use the backslash to break a long line of code into multiple lines.
message = \
'''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''' #triple quotes allow you to create a string that spans multiple lines.
print(message[:10]) #slice first 10 chars of the string
print(message[-14:]) #slice last 14 chars of the string
print()
count = {}
for character in message:
    count.setdefault(character, 0) #if the key is not in the dictionary, the setdefault() method adds the key to the dictionary with the value 0.
    count[character] = count[character] + 1
pprint(count)
print()

#================================================================================================

#nested dictionaries
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items(): #items() method returns a list of key-value pairs in a dictionary.
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(f" - Apples         {totalBrought(allGuests, 'apples')}")
print(f" - Cups           {totalBrought(allGuests, 'cups')}")
print(f" - Cakes          {totalBrought(allGuests, 'cakes')}")
print(f" - Ham Sandwiches {totalBrought(allGuests, 'ham sandwiches')}")
print(f" - Apple Pies     {totalBrought(allGuests, 'apple pies')}")
print()

#================================================================================================

#add dictionaries to a list:
europe = []

europe.append({"name": "Germany", "population": 81000000})
europe.append({"name": "Luxembourg", "population": 512000})

pprint(europe)
