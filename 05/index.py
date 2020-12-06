import math

def findHighestSeatId(bpList, seatIdList):
    seatId = 0

    for boardPass in bpList:
        
        startRow = 0
        endRow = 127

        for i in range(0, 7):
            if boardPass[i] == 'F':
                endRow -= math.ceil((endRow - startRow) / 2)
            else:
                startRow += math.ceil((endRow - startRow) / 2)
            
        if startRow != endRow:
            print('There is a problem with rows man...')
            print('startRow : ' + str(startRow) + ' | endRow : ' + str(endRow))

        startClmn = 0
        endClmn = 7

        for i in range(7, 10):
            if boardPass[i] == 'L':
                endClmn -= math.ceil((endClmn - startClmn) / 2)
            else:
                startClmn += math.ceil((endClmn - startClmn) / 2)
        
        if startClmn != endClmn:
            print('There is a problem with columns man...')
            print('startClmn : ' + str(startClmn) + ' | endClmn : ' + str(endClmn))

        provSeatId = startRow * 8 + startClmn
        if provSeatId > seatId:
            seatId = provSeatId
        seatIdList.append(provSeatId)
    return seatId

def findMissingSeat(seatIdList, minId, maxId):
    seatIdList.sort()
    for i in range(minId, maxId):
        if i not in seatIdList and i+1 in seatIdList and i-1 in seatIdList:
            return i
    return -1

f = open('data.txt', 'r')
bpList = f.read().split('\n')
seatIdList = []

print(findHighestSeatId(bpList, seatIdList))
print(findMissingSeat(seatIdList, 0, 1000))