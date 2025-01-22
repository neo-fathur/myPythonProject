from pathlib import Path
import shelve
import pprint
import os
os.system('cls' if os.name == 'nt' else 'clear')    #clear the screen

print(Path.home())                      # print the home directory
print(Path.cwd())                       # print the current working directory
print()

#===============================================================

path = Path.cwd() / 'days.txt'          # create a path object
print(path.read_text())                 # read the content of the file from a path object
print()

#==================================================================

path = os.path.abspath('./read.txt')    # get the absolute path of the file
fileObj = open(path,'a+')               # open the file in append mode
fileObj.write('\nPython is amazing.')   # write to the file
fileObj.close()                         # close the file

fileObj = open(path,'r+')               # open the file in read mode
content = fileObj.readlines()           # read the content of the file
pprint.pprint(content)                  # print the content of the file
fileObj.close()                         # close the file
print()

#==================================================================

# Open the shelf file in writeback mode to append new key-value pairs
shelfFile = shelve.open('animals_shelf.db', writeback=True)

shelfFile['Lion'] = {'habitat': 'Savanna', 'diet': 'Carnivore'}
shelfFile['Elephant'] = {'habitat': 'Forest', 'diet': 'Herbivore'}
shelfFile['Kangaroo'] = {'habitat': 'Grasslands', 'diet': 'Herbivore'}
shelfFile['Penguin'] = {'habitat': 'Antarctica', 'diet': 'Piscivore'}
shelfFile['Polar_Bear'] = {'habitat': 'Arctic', 'diet': 'Carnivore'}
print(type(shelfFile))      # print the type of the shelf file

fileObj = open('animals_data.py', 'w')  # open a file in write mode
for key, value in shelfFile.items():    # iterate through the shelf file items
    fileObj.write(f"{key} = {value}\n") # write the content of the shelf file to the file
fileObj.close()                         # close the file

shelfFile.close()                       # close the shelf file

import animals_data                     # import the file
print(animals_data.Lion)                # print the content of the file
print(animals_data.Penguin['habitat'])  # print the habitat of the penguin


