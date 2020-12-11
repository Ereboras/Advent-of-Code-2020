from itertools import groupby
from collections import Counter
from functools import reduce
from operator import mul

str_ = open('data.txt', 'r').read()
l = map(int,str_.split())
l_sorted = sorted(l)
l_sorted = [0] + l_sorted + [max(l_sorted)+3]

c = Counter(b-a for a,b in zip(l_sorted,l_sorted[1:]))
print (c[3]*c[1])

def n_cut(l_sorted):
    diff=  (b-a for a,b in zip(l_sorted,l_sorted[1:]) )
    size = (len(list(g)) for k, g in groupby(diff) if k == 1)
    # Equivalent to: 1 + len(combinaison(1),n-1) + len(combinaison(2),n-1) 
    # or maximal number of pieces formed when slicing a pancake with n cuts.  (A000124)
    perm = ((n-1)*n//2 + 1 for n in size) 
    return reduce(mul, perm)

print (n_cut(l_sorted))