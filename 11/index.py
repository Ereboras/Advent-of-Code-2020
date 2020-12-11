from collections import defaultdict

f = open('data.txt', 'r')
lineGroup = f.read().split('\n')

def passengerWave(lineGroup):
    reconstructedList = []
    for i in range(0, len(lineGroup)):
        line = lineGroup[i]
        reconstructedList.append(lineGroup[i])
        for y in range(0, len(line)):
            seat = line[y]

            if seat == 'L':
                checkSeats = True
                if i > 0 and lineGroup[i-1][y] == '#': # Top
                    checkSeats = False
                if i > 0 and y < len(line) - 1 and lineGroup[i-1][y+1] == '#': # Top right
                    checkSeats = False
                if y < len(line) - 1 and lineGroup[i][y+1] == '#': # Right
                    checkSeats = False
                if i < len(lineGroup) - 1 and y < len(line) - 1 and lineGroup[i+1][y+1] == '#': # Bottom right
                    checkSeats = False
                if i < len(lineGroup) - 1 and lineGroup[i+1][y] == '#': # Bottom
                    checkSeats = False
                if i < len(lineGroup) - 1 and y > 0 and lineGroup[i+1][y-1] == '#': # Bottom left
                    checkSeats = False
                if y > 0 and lineGroup[i][y-1] == '#': # Left
                    checkSeats = False
                if i > 0 and y > 0 and lineGroup[i-1][y-1] == '#': # Top left
                    checkSeats = False

                if checkSeats:
                    reconstructedList[i] = reconstructedList[i][:y] + '#' + reconstructedList[i][y+1:]
            
            elif seat == '#':
                countOccupied = 0
                if i > 0 and lineGroup[i-1][y] == '#': # Top
                    countOccupied += 1
                if i > 0 and y < len(line) - 1 and lineGroup[i-1][y+1] == '#': # Top right
                    countOccupied += 1
                if y < len(line) - 1 and lineGroup[i][y+1] == '#': # Right
                    countOccupied += 1
                if i < len(lineGroup) - 1 and y < len(line) - 1 and lineGroup[i+1][y+1] == '#': # Bottom right
                    countOccupied += 1
                if i < len(lineGroup) - 1 and lineGroup[i+1][y] == '#': # Bottom
                    countOccupied += 1
                if i < len(lineGroup) - 1 and y > 0 and lineGroup[i+1][y-1] == '#': # Bottom left
                    countOccupied += 1
                if y > 0 and lineGroup[i][y-1] == '#': # Left
                    countOccupied += 1
                if i > 0 and y > 0 and lineGroup[i-1][y-1] == '#': # Top left
                    countOccupied += 1

                if countOccupied >= 4:
                    reconstructedList[i] = reconstructedList[i][:y] + 'L' + reconstructedList[i][y+1:]
    return reconstructedList

def seeNbrOccupiedSeat(lineGroup, i, y):
    #print('seeNbrOccupiedSeat : i:{}, y:{}'.format(i, y))
    countOccupied = 0

    topChecked = False
    topRightChecked = False
    topLeftChecked = False
    for x in range(i-1, -1, -1): # Top part

        yDiff = i - x

        yTopRight = y + yDiff
        if yTopRight >= len(lineGroup[i]):
            topRightChecked = True

        yTopLeft = y - yDiff
        if yTopLeft < 0:
            topLeftChecked = True

        if not topChecked and lineGroup[x][y] == '#': # Top
            countOccupied += 1
            topChecked = True
        elif not topChecked and lineGroup[x][y] == 'L':
            topChecked = True

        if not topRightChecked and lineGroup[x][yTopRight] == '#': # Right
            countOccupied += 1
            topRightChecked = True
        elif not topRightChecked and lineGroup[x][yTopRight] == 'L':
            topRightChecked = True

        if not topLeftChecked and lineGroup[x][yTopLeft] == '#': # Left
            countOccupied += 1
            topLeftChecked = True
        elif not topLeftChecked and lineGroup[x][yTopLeft] == 'L':
            topLeftChecked = True

        if topChecked and topRightChecked and topLeftChecked:
            break

    bottomChecked = False
    bottomRightChecked = False
    bottomLeftChecked = False
    for x in range(i+1, len(lineGroup)): # Bottom part

        yDiff = x - i

        yBottomRight = y + yDiff
        if yBottomRight >= len(lineGroup[i]):
            bottomRightChecked = True

        yBottomLeft = y - yDiff
        if yBottomLeft < 0:
            bottomLeftChecked = True

        if not bottomChecked and lineGroup[x][y] == '#': # Bottom
            countOccupied += 1
            bottomChecked = True
        elif not bottomChecked and lineGroup[x][y] == 'L':
            bottomChecked = True

        if not bottomRightChecked and lineGroup[x][yBottomRight] == '#': # Right
            countOccupied += 1
            bottomRightChecked = True
        elif not bottomRightChecked and lineGroup[x][yBottomRight] == 'L':
            bottomRightChecked = True

        if not bottomLeftChecked and lineGroup[x][yBottomLeft] == '#': # Left
            countOccupied += 1
            bottomLeftChecked = True
        elif not bottomLeftChecked and lineGroup[x][yBottomLeft] == 'L':
            bottomLeftChecked = True

        if bottomChecked and bottomLeftChecked and bottomRightChecked:
            break

    for z in range(y-1, -1, -1): # Left part
        if lineGroup[i][z] == '#':
            countOccupied += 1
            break
        elif lineGroup[i][z] == 'L':
            break

    for z in range(y+1, len(lineGroup[i])): # Right part
        if lineGroup[i][z] == '#':
            countOccupied += 1
            break
        elif lineGroup[i][z] == 'L':
            break
    #print('Counting {} seats occupied in the vision'.format(countOccupied))
    return countOccupied

def secondWave(lineGroup):
    reconstructedList = []
    for i in range(0, len(lineGroup)):
        line = lineGroup[i]
        reconstructedList.append(lineGroup[i])
        for y in range(0, len(line)):
            seat = line[y]

            if seat == 'L' and seeNbrOccupiedSeat(lineGroup, i, y) == 0:
                reconstructedList[i] = reconstructedList[i][:y] + '#' + reconstructedList[i][y+1:]

            elif seat == '#' and seeNbrOccupiedSeat(lineGroup, i, y) >= 5:
                reconstructedList[i] = reconstructedList[i][:y] + 'L' + reconstructedList[i][y+1:]

    return reconstructedList

# Return False if not the same
def compareTwoList(firstList, secondList):
    if len(firstList) != len(secondList):
        return False
    for i in range(0, len(firstList)):
        if firstList[i] != secondList[i]:
            return False
    return True

def displayList(lineGroup):
    for l in lineGroup:
        print(l)

def part1and2(lineGroup, part):
    total = 0
    lineGroupCopy = []
    #displayList(lineGroup)
    while not compareTwoList(lineGroup, lineGroupCopy):
        lineGroupCopy = lineGroup.copy()
        if part == 'part1':
            lineGroup = passengerWave(lineGroup)
        else:
            lineGroup = secondWave(lineGroup)
            #print('---------------')
        #displayList(lineGroup)
    for line in lineGroup:
        for seat in line:
            if seat == '#':
                total += 1
    return total

print(part1and2(lineGroup, 'part2'))