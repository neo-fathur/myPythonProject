import re
from pprint import pprint
import os
os.system('cls' if os.name == 'nt' else 'clear')    #clear the screen


phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') #\d is the regex for a numeric digit character. The parentheses () in the regex create groups.
mo = phoneNumRegex.search('My phone number is (415) 555-4242.') #search() method returns a Match object.
print('Phone number found: ' + mo.group()) #group() method returns the entire matched text.

areaCode, mainNumber = mo.groups() #groups() method returns a tuple of multiple values, one value per group.
print(areaCode)
print(mainNumber)
print()

#================================================================================================

phoneNumRegex = re.compile(r'''(                    # group 1: full phone number. The ( and ) create a group. 
    (?: \(* (\d{3}) \)* )?                          # group 2: optional area code. The question mark ? means the group preceding it is optional. The \(* and \)* match literal parentheses. 
    [\s \- \.]*                                     # optional separator. The [\s \- \.]* matches any whitespace, dash, or dot character, zero or more times.
    (\d{3} [\s\-\.]* \d{4})                         # group 3: main part of the phone number with optional separator. The \d{3} matches three numeric digits. The [\s\-\.] matches any whitespace, dash, or dot character. 
    (?: [\s\-\.]* (?:ext|x|ext\.) \s* (\d{2,5}) )?  # group 4: optional extension. The (?:...) is a non-capturing group. The \s* matches any whitespace character, zero or more times. The \d{2,5} matches two to five numeric digits.
    )''', re.VERBOSE | re.IGNORECASE | re.DOTALL)   # re.VERBOSE allows for multi-line regex, re.IGNORECASE ignores case, re.DOTALL allows the dot . to match all characters, including newlines.
text = """
Call me at 123-456-7890 or (123) 456-7890 or 123.456.7890 ext 1234.
You can also reach me at (123)456-7890x123.
"""
matches = phoneNumRegex.findall(text)
print([match[0] for match in matches])
phone_numbers = []
for match in matches:
    full_number = match[0]
    area_code = match[1]
    main_number = match[2]
    extension = match[3] if len(match) > 3 else None    # Handle optional extension
    phone_numbers.append((area_code, main_number, extension, full_number))
pprint(phone_numbers)
print()

#================================================================================================

emailRegex = re.compile(r'''(           # group 1: full email address. The ( and ) create a group. 
    ([a-zA-Z0-9._%+-]+)                 # group 2: username. The + means the group preceding it must appear at least once. The ., _, %, +, and - characters are allowed in the username. 
    @                                   # @ symbol. 
    ([a-zA-Z0-9.-]+ \. [a-zA-Z]{2,4})   # group 3: domain name. The . and - characters are allowed in the domain name. The {2,4} means the group must have between 2 and 4 alphabetic characters. 
    )''', re.VERBOSE | re.DOTALL)       # re.VERBOSE allows for multi-line regex, re.DOTALL allows the dot . to match all characters, including newlines.
text = """
You can contact me at example123@example.com or at john.doe@my-domain.co.uk.
Feel free to reach out to support@company123.org anytime.
"""
matches = emailRegex.findall(text)
print([match[0] for match in matches])
emails = []
for match in matches:
    full_email = match[0]
    username = match[1]
    domain = match[2]
    emails.append((domain, username, full_email))
pprint(emails)
print()

#================================================================================================

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #the pipe character | functions as an OR operator.
mo = batRegex.search('Batmobile lost a wheel') 
print(mo.group())
print(mo.group(1))
print()

#================================================================================================

batRegex = re.compile(r'Bat(wo)?man') #the question mark ? means the group preceding it is optional.
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print()

#================================================================================================

xmasRegex = re.compile(r'\d+\s\w+') #the plus + means the group preceding it must appear at least once.
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge') 
pprint(mo)
print()

#================================================================================================

consonantRegex = re.compile(r'[^aeiouAEIOU]') #the caret ^ at the start of a character class negates it.
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.') 
print(mo)
print()

#================================================================================================

atRegex = re.compile(r'.at') #the (.) is a wildcard character that matches 1 character (except newline).
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)
print()

#================================================================================================

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #the (.*) is a wildcard character that matches 0 or more characters.
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
First, Last = mo.groups()
print(First)
print(Last)
print()

#================================================================================================

greedyRegex = re.compile(r'<.*>') 
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

nongreedyRegex = re.compile(r'<.*?>') 
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
print()

#================================================================================================

noNewlineRegex = re.compile('.*') #the dot . matches any character except a newline.
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)

newlineRegex = re.compile('.*', re.DOTALL) #re.DOTALL as the second argument to re.compile() allows the dot . to match all characters, including newlines.
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)
print()

#================================================================================================

namesRegex = re.compile(r'Agent \w+') #\w is the regex for a word character. The plus + means the group preceding it must appear at least once.
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.') #sub() method returns a string with the substitutions made.
print(mo)

agentNamesRegex = re.compile(r'Agent (\w)\w*') #\w is the regex for a word character. The asterisk * means the group preceding it can appear any number of times.
mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.') #\1 refers to the first group in the regex.
print(mo)