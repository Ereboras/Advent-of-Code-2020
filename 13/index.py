import math

f = open('data.txt', 'r')
busList = f.read().split('\n')

def part1(busList):

    earlyDepart = int(busList[0])
    boutchou = []

    for id in busList[1].split(','):
        if id != 'x':
            patachon = math.ceil(earlyDepart / int(id))
            boutchou.append([int(id), patachon*int(id)])

    earliest = None
    for bout in boutchou:
        if not earliest:
            earliest = bout
        elif bout[1] < earliest[1]:
            earliest = bout
    
    return ((earliest[1] - earlyDepart) * earliest[0])

print(part1(busList))