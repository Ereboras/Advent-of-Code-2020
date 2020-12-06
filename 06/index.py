f = open('data.txt', 'r')
lineGroup = f.read().split('\n')
groupList = []

def part1(groupList):
    countTotal = 0
    i = 0

    for line in lineGroup:
        if line != '':
            if i == len(groupList):
                groupList.append('')
            groupList[i] += line
        else:
            i += 1

    for group in groupList:
        countTotal += len(set(group))

    return countTotal

def part2(lineGroup):
    countTotal = 0
    groups = []
    i = 0

    for line in lineGroup:
        if line != '':
            if i == len(groups):
                groups.append([])
            groups[i].append(line)
        else:
            i += 1

    for group in groups:
        for charToCheck in group[0]:
            charAllYes = True
            for person in group:
                if charToCheck not in person:
                    charAllYes = False
            if charAllYes:
                countTotal += 1            

    return countTotal

print(part1(groupList))
print(part2(lineGroup))