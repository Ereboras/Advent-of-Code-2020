import re

f = open('data.txt', 'r')
l = f.read().split('\n')

i = 0
passList = []
for element in l:
    if element != '':
        if i == len(passList):
            passList.append([])
        passList[i].append(element)
    else:
        i += 1

# Register each passport in passFinalList as a dictionnary with key/value for the subsequent fields :
# byr, iyr, eyr, hgt, hcl, ecl, pid, cid
passFinalList = []
for passport in passList:
    passDict = dict()
    for data in passport:
        assocs = data.split(' ')
        for keyVal in assocs:
            keyValList = keyVal.split(':')
            passDict[keyValList[0]] = keyValList[1]
    passFinalList.append(passDict)

def checkPassValidOld(passList, field):
    nbrValidPassport = 0
    for passport in passFinalList:
        passSize = len(passport)
        if passSize == 8 or (field not in passport and passSize == 7):
            nbrValidPassport += 1
    return nbrValidPassport

def checkPassValidNew(passList, field):
    nbrValidPassport = 0
    for passport in passFinalList:
        passSize = len(passport)

        if (passSize == 7 and field in passport) or passSize < 7:
            continue

        eyeColorValid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        
        if passport['byr'].isdigit() and (int(passport['byr']) < 1920 or int(passport['byr']) > 2002):
            continue
        elif passport['iyr'].isdigit() and (int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020):
            continue
        elif passport['eyr'].isdigit() and (int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030):
            continue
        elif passport['hgt'][:-2] == '' or ((passport['hgt'][-2:] == 'cm' and (int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193)) or (passport['hgt'][-2:] == 'in' and (int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76))):
            continue
        elif len(passport['hcl']) != 7 or passport['hcl'][0] != '#' or not re.search('[a-z0-9]+', passport['hcl']):
            continue
        elif passport['ecl'] not in eyeColorValid:
            continue
        elif len(passport['pid']) != 9:
            continue
        
        nbrValidPassport += 1

    return nbrValidPassport

print(checkPassValidOld(passFinalList, 'cid'))
print(checkPassValidNew(passFinalList, 'cid'))