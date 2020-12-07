# Day 6 challenge : Custom Customs

Link to challenge : https://adventofcode.com/2020/day/6

## Best solution :

### Part 1 : 

In this part of the challenge, we want to calculate every unique "yes" answer for every group and sum them to get the total.

``` python
print("Part 1:",sum([len(set(d.replace('\n',''))) for d in allData]))
```

1. To do so, we create a for each loop to access to all group informations and later sum all yes answers.
2. There is still the carriage return `\n`, thus the `d.replace('\n')` to get rid of these two chars.
3. Then, we put it in a set to remove all duplicate values ([pydoc on set](https://docs.python.org/3/library/stdtypes.html#set) tells us that set automatically remove duplicate entries when adding elements).
4. We calculate the length of the now initialized set to see the number of unique "yes" answer for each group.
5. The length of these sets are put in an array (see the `[` and `]` around the loop ?) that is then summed with `sum`, we now have the total !

### Part 2 :

In this part of the challenge, we count only answers common to all member of the same group.


``` python
print("Part 2:", sum([len(set.intersection(*[set(item) for item in groupData])) for groupData in [d.split('\n') for d in allData]]))
```

1. We first make a for each loop on `allData` and split on `\n` to separate answers of each member of the group.
2. We loop on these members (`item`) to put them individually in a set, this will be useful for the next step.
3. These sets are all added to an array as an arg of [set.intersection](https://www.w3schools.com/python/ref_set_intersection.asp) function that return only the items common to all set in a new set.
4. We now have all the answer that are common to all member of the group. We just need to calculate the length of the set to get the number of common answer in each group.
5. The ``sum` function to sum up all common answer for every group, we have the total !