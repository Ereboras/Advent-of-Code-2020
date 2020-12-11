from collections import defaultdict

f = open('data.txt', 'r')
lineGroup = f.read().split('\n')

def seeNeighborsOccupied(lineGroup, i, y):
    countOccupied = 0
    if i > 0 and lineGroup[i-1][y] == '#': # Top
        countOccupied += 1
    if i > 0 and y < len(lineGroup[i]) - 1 and lineGroup[i-1][y+1] == '#': # Top right
        countOccupied += 1
    if y < len(lineGroup[i]) - 1 and lineGroup[i][y+1] == '#': # Right
        countOccupied += 1
    if i < len(lineGroup) - 1 and y < len(lineGroup[i]) - 1 and lineGroup[i+1][y+1] == '#': # Bottom right
        countOccupied += 1
    if i < len(lineGroup) - 1 and lineGroup[i+1][y] == '#': # Bottom
        countOccupied += 1
    if i < len(lineGroup) - 1 and y > 0 and lineGroup[i+1][y-1] == '#': # Bottom left
        countOccupied += 1
    if y > 0 and lineGroup[i][y-1] == '#': # Left
        countOccupied += 1
    if i > 0 and y > 0 and lineGroup[i-1][y-1] == '#': # Top left
        countOccupied += 1
    return countOccupied
def firstPassengerWave(lineGroup):
    reconstructedList = []
    for i in range(0, len(lineGroup)):
        reconstructedList.append(lineGroup[i])
        for y in range(0, len(lineGroup[i])):
            if lineGroup[i][y] == 'L' and seeNeighborsOccupied(lineGroup, i, y) == 0:
                reconstructedList[i] = reconstructedList[i][:y] + '#' + reconstructedList[i][y+1:]
            elif lineGroup[i][y] == '#' and seeNeighborsOccupied(lineGroup, i, y) >= 4:
                reconstructedList[i] = reconstructedList[i][:y] + 'L' + reconstructedList[i][y+1:]
    return reconstructedList

def seeNbrOccupiedSeat(lineGroup, i, y):
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
    return countOccupied

def secondPassengerWave(lineGroup):
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
    while not compareTwoList(lineGroup, lineGroupCopy):
        lineGroupCopy = lineGroup.copy()
        if part == 'part1':
            lineGroup = firstPassengerWave(lineGroup)
        else:
            lineGroup = secondPassengerWave(lineGroup)
    for line in lineGroup:
        for seat in line:
            if seat == '#':
                total += 1
    return total

print(part1and2(lineGroup, 'part1'))
print(part1and2(lineGroup, 'part2'))