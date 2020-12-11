from collections import defaultdict

f = open('data.txt', 'r')
lineGroup = f.read().split('\n')

def part2(nbrList):
    return 0

def part1(nbrList):
    myDict = defaultdict(int)
    nbrList.sort()
    for i in range (0, len(nbrList)-1):
        myDict[nbrList[i+1] - nbrList[i]] += 1

    return (myDict[1]+1)*(myDict[3]+1)

nbrList = [int(n) for n in lineGroup]
print(part1(nbrList))
print(part2(nbrList))