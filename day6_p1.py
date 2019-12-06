from collections import defaultdict

orbitDict = {}

file = open("day6_data.txt", "r")

while (1):
    data = file.readline()
    if not data:
        break
    orbitDict[data.split(")")[1][:-1]] = data.split(")")[0]

def calculateNumOrbits(orbitDict):
    depth = 0
    numOrbits = 0

    for object in orbitDict:
        currentObject = object
        while (currentObject != "COM"):
            currentObject = orbitDict[currentObject]
            depth += 1
        numOrbits += depth
        depth = 0

    return numOrbits


numOrbits = calculateNumOrbits(orbitDict)
print(numOrbits)
print(orbitDict)
