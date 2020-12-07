origData = open('data.txt', 'r').read()
allData = origData.split('\n\n')

print("Part 1:",sum([len(set(d.replace('\n',''))) for d in allData]))
print("Part 2:", sum([len(set.intersection(*[set(item) for item in groupData])) for groupData in [d.split('\n') for d in allData]]))