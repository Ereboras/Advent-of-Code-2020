f = open('data.txt', 'r')
instList = f.read().split('\n')

class Ship:

    def __init__(self):
        self.facing = 'E'
        self.posShip = {'X': 0, 'Y': 0}
        self.waypoint = {'X': 10, 'Y': 1}

    def move_part1(self, inst):
        instD, instV = inst[0], int(inst[1:])
        
        if instD == 'N':
            self.posShip['Y'] += instV
        elif instD == 'S':
            self.posShip['Y'] -= instV
        elif instD == 'E':
            self.posShip['X'] += instV
        elif instD == 'W':
            self.posShip['X'] -= instV
        elif instD == 'F':
            self.move_part1(self.facing + str(instV))
        elif instD == 'R':
            self.turnShip(instD, instV)
        elif instD == 'L':
            self.turnShip(instD, instV)
    
    def turnShip(self, turnD, value):
        dList = ['N', 'E', 'S', 'W']
        ind = dList.index(self.facing)

        if turnD == 'R':
            nbr = (value / 90) + ind
            nbr = nbr if nbr <= 3 else nbr % len(dList)
        else:
            nbr = ind - (value / 90)
            nbr = nbr if nbr > -4 else nbr % len(dList)

        self.facing = dList[int(nbr)]

    def move_part2(self, inst):

        if inst == 'R270':
            inst = 'L90'
        elif inst == 'L270':
            inst = 'R90'
        
        instD, instV = inst[0], int(inst[1:])

        if instD == 'N':
            self.waypoint['Y'] += instV
        elif instD == 'S':
            self.waypoint['Y'] -= instV
        elif instD == 'E':
            self.waypoint['X'] += instV
        elif instD == 'W':
            self.waypoint['X'] -= instV
        elif instD == 'F':
            self.posShip['X'] += self.waypoint['X']*instV
            self.posShip['Y'] += self.waypoint['Y']*instV
        elif instD == 'R' or instD == 'L':
            self.turnWaypoint(instD, instV)

    def turnWaypoint(self, turnD, value):
        x = self.waypoint['X']
        y = self.waypoint['Y']

        if value == 90:
            tempNbr = self.waypoint['Y']
            self.waypoint['Y'] = self.waypoint['X']
            self.waypoint['X'] = tempNbr
            if turnD == 'R':
                if (x > 0 and y > 0) or (x < 0 and y < 0):
                    self.waypoint['Y'] = -self.waypoint['Y']
                elif (x > 0 and y < 0) and (x < 0 and y > 0):
                    self.waypoint['X'] = -self.waypoint['X']
            else:
                if (x > 0 and y > 0) or (x < 0 and y < 0):
                    self.waypoint['X'] = -self.waypoint['X']
                elif (x > 0 and y < 0) and (x < 0 and y > 0):
                    self.waypoint['Y'] = -self.waypoint['Y']
        else:
            self.waypoint['X'] = -self.waypoint['X']
            self.waypoint['Y'] = -self.waypoint['Y']

    def getManhattanDist(self):
        return abs(self.posShip['X']) + abs(self.posShip['Y'])

def part1(instList):
    myShip = Ship()
    
    for inst in instList:
        myShip.move_part1(inst)

    return myShip.getManhattanDist()

def part2(instList):
    myShip = Ship()
    
    for inst in instList:
        myShip.move_part2(inst)

    return myShip.getManhattanDist()

print(part2(instList))