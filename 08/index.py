f = open('data.txt', 'r')
lineGroup = f.read().split('\n')

def part1(instList, i, end, accumulator):
    if i == end:
        return accumulator
    
    if instList[i][2]:
        return accumulator
    else:
        instList[i][2] = True

    instruction = instList[i]

    if instruction[0] == 'nop':
            return part1(instList, i+1, end, accumulator)
    elif instruction[0] == 'acc':
        if instruction[1][0] == '+':
            accumulator += int(instruction[1][1:])
        else:
            accumulator -= int(instruction[1][1:])
        return part1(instList, i+1, end, accumulator)
    elif instruction[0] == 'jmp':
        if instruction[1][0] == '+':
            i += int(instruction[1][1:])
        else:
            i -= int(instruction[1][1:])
        return part1(instList, i, end, accumulator)

def findPartToChange(instList, i, end):
    if i == end:
        return True

    instruction = instList[i]
    
    if instruction[2]:
        return False
    else:
        instruction[2] = True

    if instruction[0] == 'nop':
        return findPartToChange(instList, i+1, end)
    elif instruction[0] == 'acc':
        return findPartToChange(instList, i+1, end)
    elif instruction[0] == 'jmp':
        if instruction[1][0] == '+':
            i += int(instruction[1][1:])
        else:
            i -= int(instruction[1][1:])
        return findPartToChange(instList, i, end)

def resetInstList(instList):
    for item in instList:
        item[2] = False

def part2(instList, i, end, accumulator):
    for i in range (0, len(instList)):
        if instList[i][0] == 'nop':
            instList[i][0] = 'jmp'
            if findPartToChange(instList, 0, len(instList)):
                resetInstList(instList)
                return part1(instList, 0, end, accumulator)
            else:
                instList[i][0] = 'nop'
        elif instList[i][0] == 'jmp':
            instList[i][0] = 'nop'
            if findPartToChange(instList, 0, len(instList)):
                resetInstList(instList)
                return part1(instList, 0, end, accumulator)
            else:
                instList[i][0] = 'jmp'
        resetInstList(instList)

instList = []
for line in lineGroup:
    lineList = line.split(' ')
    lineList.append(False)
    instList.append(lineList)

print(part2(instList, 0, len(instList), 0))