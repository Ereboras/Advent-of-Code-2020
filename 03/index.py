f = open('data.txt', 'r')
l = f.read().split('\n')


def find_nbr_tree(data, nbrLine, xStep, yStep):
    nbrTree = 0
    nbrColumn = len(data[0])
    x = xStep

    for y in range(yStep, nbrLine, yStep):
        if x >= nbrColumn:
            x = x - nbrColumn
        if data[y][x] == '#':
            nbrTree += 1
        x += xStep

    return nbrTree

a = find_nbr_tree(l, len(l), 1, 1)
b = find_nbr_tree(l, len(l), 3, 1)
c = find_nbr_tree(l, len(l), 5, 1)
d = find_nbr_tree(l, len(l), 7, 1)
e = find_nbr_tree(l, len(l), 1, 2)
print(a*b*c*d*e)