from collections import defaultdict
import operator

def part1(nbrList, limit):

    nbrDict = defaultdict(int)
    
    for i in range(0, len(nbrList)):
        nbrDict[nbrList[i]] = i+1

    lastValue = max(nbrDict.items(), key=operator.itemgetter(1))[0]

    for i in range(len(nbrList)+1, limit+1):
        #print('Turn {} | lastValue {}'.format(i, lastValue))

        if lastValue not in nbrDict:
            #print('New value {} at turn {}'.format(lastValue, i))
            nbrDict[lastValue] = i-1
            lastValue = 0
        else:
            #print('Value {} spoken turn {} was already spoken at turn {}'.format(lastValue, i-1, nbrDict[lastValue]))
            tempTurn = (i-1) - nbrDict[lastValue]
            nbrDict[lastValue] = i-1
            lastValue = tempTurn

    return lastValue

f = open('data.txt', 'r')
nbr = [int(n) for n in f.read().split(',')]

print(part1(nbr, 2020))
print(part1(nbr, 30000000))