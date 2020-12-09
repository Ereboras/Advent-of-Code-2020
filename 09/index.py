f = open('data.txt', 'r')
lineGroup = f.read().split('\n')

def testTwoNumSum(nbrList, nbrToFind):
    for nbr in nbrList:
        tempNbrFind = nbrToFind - nbr
        if tempNbrFind in nbrList:
            return True
    return False

def findContiguous(nbrList, nbrToFind):
    for i in range(0, len(nbrList)):
        nbrAdded = nbrList[i]
        contiguousList = []
        contiguousList.append(nbrList[i])
        for y in range(i+1, len(nbrList)):
            nbrAdded += nbrList[y]
            contiguousList.append(nbrList[y])
            if nbrAdded == nbrToFind:
                return min(contiguousList) + max(contiguousList)
    return 0

def part1(nbrList, size):
    foundNumber = -1

    for i in range(size, len(nbrList)):
        check = testTwoNumSum(nbrList[i-size:i], nbrList[i])
        if not check:
            return nbrList[i]

    return foundNumber

nbrList = [int(n) for n in lineGroup]
print(part1(nbrList, 25))
print(findContiguous(nbrList, part1(nbrList, 25)))