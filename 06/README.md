# Day 6 challenge : Custom Customs

Len du challenge : https://adventofcode.com/2020/day/6

## Best solution :

### Part 1 : 

``` python
print("Part 1:",sum([len(set(d.replace('\n',''))) for d in allData]))
```

In this challenge, we want to calculate every unique "yes" answer for every group and sum them to get the total.

1. To do so, we create a for each loop to access to all group informations and later sum all yes answers.
2. There is still the carriage return `\n`, thus the `d.replace('\n')` to get rid of these two chars.
3. Then, we put it in a set to remove all duplicate values ([pydoc on set](https://docs.python.org/3/library/stdtypes.html#set) tells us that set automatically remove duplicate entries when adding elements).
4. We calculate the length of the now initialized set to see the number of unique "yes" answer for each group.
5. The length of these sets are put in an array (see the `[` and `]` around the loop ?) that is then summed with `sum`, we now have the total !

### Part 2 :

``` python
print("Part 2:", sum([len(set.intersection(*[set(item) for item in groupData])) for groupData in [d.split('\n') for d in allData]]))
```

