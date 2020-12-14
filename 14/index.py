from collections import defaultdict
from itertools import product 

def modifyBit(nbr, pos, value):
    mask = 1 << pos
    return (nbr & ~mask) | ((value << pos) & mask)

def part1(lines):

    mask = []
    memory = defaultdict(int)
    for line in lines:
        
        # Manage new mask
        if line[0:4] == 'mask':
            mask = []
            for idx, char in enumerate(line.split(' ')[2]):
                if char.isdigit():
                    mask.append([idx, int(char)])
            continue

        memAdress = int(line.split(']')[0][4:])
        memValue = int(line.split(' ')[2])
        memValue = '{0:036b}'.format(memValue)
        
        for bit in mask:
            memValue = memValue[0:bit[0]] + str(bit[1]) + memValue[bit[0]+1:]
        memory[memAdress] = int(memValue, 2)

    total = 0
    for addr, val in memory.items():
        total += val

    return total

def modifyBitAddr(addr, mask):
    addresses = []

    for idx, char in enumerate(mask):
        if char != '0' and addr[idx] != char:
            addr = addr[0:idx] + str(char) + addr[idx+1:]

    indices = [ i for i, c in enumerate(addr) if c is 'X' ]
    
    pd = list(addr)
    for cb in product('01', repeat=len(indices)):
        for i, c in zip(indices, cb):
            pd[i] = c
        addresses.append(''.join(pd))
    
    return addresses

def part2(lines):
    mask = ''
    memory = defaultdict(int)
    for line in lines:
        
        if line[0:4] == 'mask':
            mask = line.split(' ')[2]
            continue

        memAdress = int(line.split(']')[0][4:])
        memValue = int(line.split(' ')[2])
        memValue = '{0:036b}'.format(memValue)
        memAdress = '{0:036b}'.format(memAdress)
        
        memAdresses = modifyBitAddr(memAdress, mask)
        for memAd in memAdresses:
            memory[int(memAd, 2)] = int(memValue, 2)
        
    total = 0
    for addr, val in memory.items():
        total += val

    return total

f = open('data.txt', 'r')
lines = f.read().split('\n')

print(part2(lines))