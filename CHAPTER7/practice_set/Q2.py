nameList = ["Harry", "Soham", "Sachin", "Rahul"] 
listLen = len(nameList)

for i in range(listLen):
    if(nameList[i].startswith('S')):
        print(nameList[i])

# or

for name in nameList:
    if name.startswith('S'):
        print(name)