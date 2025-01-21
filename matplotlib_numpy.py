import os
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

os.system('cls' if os.name == 'nt' else 'clear')    #clear the screen

# Create an empty dictionary for associating radish names
# with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []

# Clean up (munge) a string so it's easy to match against other strings
def clean_string(s):
    return s.strip().capitalize().replace("  "," ")

# Check if someone has voted already and return True or False
def has_already_voted(name):
    if name in voted:
        print(name + " has already voted! Fraud!")
        return True
    else:
        return False

# Count a vote for the radish variety named 'radish'
def count_vote(radish):
    if not radish in counts:
        # First vote for this variety
        counts[radish] = 1
    else:
        # Increment the radish count
        counts[radish] = counts[radish] + 1


with open("radishsurvey.txt") as file:
    for line in file:
        line = line.strip() #If line was "Jin Li - White Icicle\n", this code strips the newline from the end so the value of line becomes "Jin Li - White Icicle"
        name, vote = line.split(" - ", 2) #“multiple assignment” technique only works when the number of elements being assigned on the left hand side of the “ = “ matches the number on the right
        name = clean_string(name)
        vote = clean_string(vote)

        if not has_already_voted(name):
            count_vote(vote)
        voted.append(name)

print()
print("Results:")
pprint(counts)

# Find the winner by finding the radish with the most votes
winner_name = ""
winner_votes = 0
for name in counts:
    if counts[name] > winner_votes:
        winner_votes = counts[name]
        winner_name = name
print()
print(f"The winner is: '{winner_name}' with {winner_votes} votes!")


names = []
votes = []
# Split the dictionary of name:votes into two lists, one for names and one for vote count
for radish in counts:
    names.append(radish)
    votes.append(counts[radish])

# The X axis can just be numbered 0,1,2,3...
x = np.arange(len(counts))

plt.bar(x, votes)
plt.xticks(ticks=x, labels=names, rotation=45, ha='right')
plt.ylabel("Votes")
plt.title('Radish Variety Votes')

plt.tight_layout()
plt.show()