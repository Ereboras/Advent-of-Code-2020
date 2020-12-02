f = open('data.txt', 'r')
l = f.read().split('\n')


def find_valid_pass_old(data):
    nbrPasswordValid = 0
    for line in l:
        lineArray = line.split(' ')
        minOcc = int(lineArray[0].split('-')[0])
        maxOcc = int(lineArray[0].split('-')[1])
        letterOcc = lineArray[1][0]
        nbrOcc = lineArray[2].count(letterOcc)

        if nbrOcc >= minOcc and nbrOcc <= maxOcc:
            nbrPasswordValid += 1
    return nbrPasswordValid

def find_valid_pass_new(data):
    nbrPasswordValid = 0

    for line in l:
        lineArray = line.split(' ')
        firstPos = int(lineArray[0].split('-')[0])
        secondPos = int(lineArray[0].split('-')[1])
        letterOcc = lineArray[1][0]
        passw = lineArray[2]

        if (passw[firstPos-1] == letterOcc) ^ (passw[secondPos-1] == letterOcc):
            nbrPasswordValid += 1

    return nbrPasswordValid

print(find_valid_pass_old(l))
print(find_valid_pass_new(l))

