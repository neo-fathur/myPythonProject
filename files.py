path = 'days.txt'
myFile = open(path, 'r')

print(myFile.read())
print()

myFile.close()

#==================================================================

path = 'read.txt'
myFile = open(path,'a+')
myFile.write('\nPython is amazing.')
myFile.close()

myFile = open(path,'r+')
data = myFile.readlines()
print(data)
print('')
myFile.close()