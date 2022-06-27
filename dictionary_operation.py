myDict = {'one': 'Bill', 'two': 18, 'three': 'Smith', 'four': 'Dara', 'five': 21, 'six': 'Wilson'}
print(myDict);

print("\nAccess Dictionary : ")
print(myDict['one']);
print(myDict['two']);

print("\nAdd element in dictionary : ")
myDict['seven'] = 32;
print(myDict);

print("\nUpdate dictionary : ")
myDict['one'] = "Chinu";
myDict['five'] = "Champ";
print(myDict);

print("\nDelete element From Dictionary : ")
print(myDict.pop("two"));
print(myDict.pop("five"));
print(myDict);

print("\nLooping through dictionary : ")
for d in myDict:	
	print(myDict[d]);
