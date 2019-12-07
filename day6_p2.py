from collections import defaultdict

orbitDict = {}

file = open("day6_data.txt", "r")

while (1):
    data = file.readline()
    if not data:
        break
    orbitDict[data.split(")")[1][:-1]] = data.split(")")[0]

file.close()

def calculateOrbitalTransfer(orbitDict):
    youList = []
    sanList = []

    currentObject = "YOU"
    destinationObject = "SAN"

    while (currentObject != "COM"):
        youList.append(orbitDict[currentObject])
        currentObject = orbitDict[currentObject]

    while (destinationObject != "COM"):
        sanList.append(orbitDict[destinationObject])
        destinationObject = orbitDict[destinationObject]

    routeList  = []
    extList = []

    for obj in youList:
        if obj in sanList:

            currentObject = "YOU"
            destinationObject = "SAN"
            meetingObject = obj

            while (currentObject != meetingObject):
                routeList.append(orbitDict[currentObject])
                currentObject = orbitDict[currentObject]

            while (destinationObject != meetingObject):
                extList.append(orbitDict[destinationObject])
                destinationObject = orbitDict[destinationObject]

            extList = extList[::-1]
            totalList = routeList[:-1] + extList[1:]
            print(totalList)

            break

    return len(totalList)


numOrbitalTransfers = calculateOrbitalTransfer(orbitDict)
print(numOrbitalTransfers)
